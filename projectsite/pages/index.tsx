import { useState, useRef, useEffect } from 'react';
import styles from '../styles/Home.module.css';

interface SymbolInfo {
  prediction: string;
  confidence?: number;
  description?: string;
}

type InputMethod = 'upload' | 'draw';
type Theme = 'light' | 'dark';

export default function Home() {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [prediction, setPrediction] = useState<SymbolInfo | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isDrawing, setIsDrawing] = useState(false);
  const [activeTab, setActiveTab] = useState<InputMethod>('draw');
  const [theme, setTheme] = useState<Theme>('light');
  const [error, setError] = useState<string | null>(null);
  const [brushSize, setBrushSize] = useState(3);
  const [canPredict, setCanPredict] = useState(false);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const contextRef = useRef<CanvasRenderingContext2D | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const lastPosRef = useRef<{ x: number; y: number } | null>(null);
  const hasDrawnRef = useRef(false);

  useEffect(() => {
    console.log('Setting up canvas...');
    const canvas = canvasRef.current;
    if (!canvas) return;

    // Set canvas size to match its display size
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.height;
    
    const context = canvas.getContext('2d');
    if (!context) return;
    
    context.fillStyle = theme === 'light' ? '#ffffff' : '#1a1a1a';
    context.fillRect(0, 0, canvas.width, canvas.height);
    context.strokeStyle = theme === 'light' ? '#000000' : '#ffffff';
    context.lineWidth = brushSize;
    context.lineCap = 'round';
    context.lineJoin = 'round';
    contextRef.current = context;
    console.log('Canvas setup complete with dimensions:', { width: canvas.width, height: canvas.height });
  }, [theme, brushSize]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  const getCanvasCoordinates = (e: React.MouseEvent<HTMLCanvasElement>): { x: number; y: number } => {
    const canvas = canvasRef.current;
    if (!canvas) return { x: 0, y: 0 };

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // Log coordinates for debugging
    console.log('Raw coordinates:', { clientX: e.clientX, clientY: e.clientY });
    console.log('Canvas rect:', rect);
    console.log('Calculated coordinates:', { x, y });

    return { x, y };
  };

  const handleMouseDown = (e: React.MouseEvent<HTMLCanvasElement>) => {
    e.preventDefault();
    if (!contextRef.current) return;

    const coords = getCanvasCoordinates(e);
    console.log('Mouse down at:', coords);
    
    setIsDrawing(true);
    hasDrawnRef.current = false;
    lastPosRef.current = coords;
    
    contextRef.current.beginPath();
    contextRef.current.moveTo(coords.x, coords.y);
    setError(null);
  };

  const handleMouseMove = (e: React.MouseEvent<HTMLCanvasElement>) => {
    e.preventDefault();
    if (!isDrawing || !contextRef.current || !lastPosRef.current) return;

    const coords = getCanvasCoordinates(e);
    console.log('Drawing to:', coords);

    contextRef.current.lineTo(coords.x, coords.y);
    contextRef.current.stroke();
    lastPosRef.current = coords;
    hasDrawnRef.current = true;
    setCanPredict(true);
  };

  const handleMouseUp = () => {
    setIsDrawing(false);
    lastPosRef.current = null;
  };

  const handleMouseLeave = () => {
    if (isDrawing) {
      handleMouseUp();
    }
  };

  const handleImageUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    // Get file extension and convert to lowercase
    const fileExtension = file.name.split('.').pop()?.toLowerCase() || '';
    const validExtensions = ['jpg', 'jpeg', 'png', 'gif'];
    
    // Check file extension
    if (!validExtensions.includes(fileExtension)) {
      setError('Please upload a JPG, JPEG, PNG, or GIF file');
      return;
    }

    // Check MIME type (as additional validation)
    const validMimeTypes = [
      'image/jpeg',
      'image/jpg',
      'image/png',
      'image/gif',
      // Add lowercase variations
      'image/pjpeg', // Progressive JPEG
      'image/x-png'  // Older PNG type
    ];
    
    if (!validMimeTypes.includes(file.type.toLowerCase())) {
      setError('Please upload a valid image file');
      return;
    }

    // Check file size (max 5MB)
    if (file.size > 5 * 1024 * 1024) {
      setError('File size should be less than 5MB');
      return;
    }

    setSelectedImage(URL.createObjectURL(file));
    setError(null);
    setPrediction(null);
    setCanPredict(true);
  };

  const predict = async () => {
    if (activeTab === 'draw' && !hasDrawnRef.current) {
      setError('Please draw something first');
      return;
    }

    if (activeTab === 'upload' && !selectedImage) {
      setError('Please upload an image first');
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      let response;
      
      if (activeTab === 'draw') {
        const canvas = canvasRef.current;
        if (!canvas) return;
        
        const dataUrl = canvas.toDataURL('image/png');
        response = await fetch('/api/predict', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ image: dataUrl }),
        });
      } else {
        const formData = new FormData();
        const file = fileInputRef.current?.files?.[0];
        if (!file) return;
        
        formData.append('image', file);
        response = await fetch('/api/predict', {
          method: 'POST',
          body: formData,
        });
      }
      
      const data = await response.json();
      if (data.error) {
        setError(data.error);
        return;
      }

      setPrediction({
        prediction: data.prediction,
        confidence: data.confidence,
        description: getSymbolDescription(data.prediction)
      });
    } catch (error) {
      setError('Error processing request. Please try again.');
      console.error('Error predicting:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const clearCanvas = () => {
    console.log('Clearing canvas');
    if (!contextRef.current || !canvasRef.current) return;
    contextRef.current.fillStyle = theme === 'light' ? '#ffffff' : '#1a1a1a';
    contextRef.current.fillRect(0, 0, canvasRef.current.width, canvasRef.current.height);
    contextRef.current.strokeStyle = theme === 'light' ? '#000000' : '#ffffff';
    setPrediction(null);
    hasDrawnRef.current = false;
    setError(null);
    setCanPredict(false);
  };

  const clearUpload = () => {
    setSelectedImage(null);
    setPrediction(null);
    setError(null);
    setCanPredict(false);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const getSymbolDescription = (symbol: string): string => {
    const descriptions: Record<string, string> = {
      'alpha': 'First letter of the Greek alphabet (α)',
      'beta': 'Second letter of the Greek alphabet (β)',
      'pi': 'Mathematical constant pi (π), ratio of circle\'s circumference to diameter',
      'sigma': 'Greek letter sigma (Σ), often used for summation',
      'theta': 'Greek letter theta (θ), often used for angles',
      'integral': '∫ symbol used for integration in calculus',
      'sum': 'Σ symbol used for summation in mathematics',
      // Add more descriptions as needed
    };
    return descriptions[symbol.toLowerCase()] || `Mathematical symbol: ${symbol}`;
  };

  return (
    <div className={`${styles.container} ${styles[theme]}`}>
      <header className={styles.header}>
        <h1 className={styles.title}>Math Symbol Predictor</h1>
        <button onClick={toggleTheme} className={styles.themeToggle}>
          {theme === 'light' ? '🌙' : '☀️'}
        </button>
      </header>

      <main className={styles.main}>
        <div className={styles.tabs}>
          <button
            className={`${styles.tab} ${activeTab === 'draw' ? styles.active : ''}`}
            onClick={() => {
              setActiveTab('draw');
              setPrediction(null);
              setError(null);
              setCanPredict(hasDrawnRef.current);
            }}
          >
            Draw Symbol
          </button>
          <button
            className={`${styles.tab} ${activeTab === 'upload' ? styles.active : ''}`}
            onClick={() => {
              setActiveTab('upload');
              setPrediction(null);
              setError(null);
              setCanPredict(!!selectedImage);
            }}
          >
            Upload Image
          </button>
        </div>

        <div className={styles.content}>
          <div className={styles.inputSection}>
            {activeTab === 'draw' ? (
              <div className={styles.drawingTools}>
                <div className={styles.brushControls}>
                  <label>Brush Size:</label>
                  <div className={styles.brushSizes}>
                    {[2, 3, 5].map(size => (
                      <button
                        key={size}
                        className={`${styles.brushSize} ${brushSize === size ? styles.active : ''}`}
                        onClick={() => setBrushSize(size)}
                      >
                        {size === 2 ? 'S' : size === 3 ? 'M' : 'L'}
                      </button>
                    ))}
                  </div>
                </div>
                <div className={styles.canvasContainer}>
                  <canvas
                    ref={canvasRef}
                    onMouseDown={handleMouseDown}
                    onMouseMove={handleMouseMove}
                    onMouseUp={handleMouseUp}
                    onMouseLeave={handleMouseLeave}
                    className={styles.canvas}
                  />
                  <button onClick={clearCanvas} className={styles.clearButton}>
                    Clear Canvas
                  </button>
                </div>
              </div>
            ) : (
              <div className={styles.uploadSection}>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept=".jpg,.jpeg,.png,.gif,image/jpeg,image/jpg,image/png,image/gif,image/pjpeg,image/x-png"
                  onChange={handleImageUpload}
                  className={styles.fileInput}
                  style={{ display: 'none' }}
                />
                <div 
                  className={styles.uploadArea}
                  onClick={() => fileInputRef.current?.click()}
                  onDragOver={(e) => e.preventDefault()}
                  onDrop={(e) => {
                    e.preventDefault();
                    const file = e.dataTransfer.files[0];
                    if (file) {
                      const input = fileInputRef.current;
                      if (input) {
                        const dataTransfer = new DataTransfer();
                        dataTransfer.items.add(file);
                        input.files = dataTransfer.files;
                        input.dispatchEvent(new Event('change', { bubbles: true }));
                      }
                    }
                  }}
                >
                  {selectedImage ? (
                    <img src={selectedImage} alt="Uploaded" className={styles.preview} />
                  ) : (
                    <div className={styles.uploadPrompt}>
                      <svg className={styles.uploadIcon} viewBox="0 0 24 24">
                        <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
                      </svg>
                      <p>Drag image here or click to upload</p>
                      <span className={styles.supportedFormats}>
                        Supports JPG, JPEG, PNG, GIF
                      </span>
                    </div>
                  )}
                </div>
                {selectedImage && (
                  <button onClick={clearUpload} className={styles.clearButton}>
                    Clear Upload
                  </button>
                )}
              </div>
            )}

            {error && (
              <div className={styles.error}>
                ⚠️ {error}
              </div>
            )}

            <button 
              onClick={predict} 
              className={styles.predictButton}
              disabled={isLoading || !canPredict}
            >
              {isLoading ? (
                <>
                  <div className={styles.spinner} />
                  Processing...
                </>
              ) : (
                'Predict Symbol'
              )}
            </button>
          </div>

          <div className={styles.resultSection}>
            {prediction && (
              <div className={styles.prediction}>
                <h2>Prediction: {prediction.prediction}</h2>
                {prediction.confidence && (
                  <div className={styles.confidenceBar}>
                    <div 
                      className={styles.confidenceFill}
                      style={{ width: `${prediction.confidence * 100}%` }}
                    />
                    <span>{(prediction.confidence * 100).toFixed(1)}% Confidence</span>
                  </div>
                )}
                {prediction.description && (
                  <p className={styles.description}>
                    {prediction.description}
                  </p>
                )}
              </div>
            )}
          </div>
        </div>
      </main>

      <footer className={styles.footer}>
        <a href="#" className={styles.footerLink}>Feedback</a>
        <span className={styles.footerDivider}>•</span>
        <a href="#" className={styles.footerLink}>About</a>
      </footer>
    </div>
  );
}
