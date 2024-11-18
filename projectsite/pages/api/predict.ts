import type { NextApiRequest, NextApiResponse } from 'next';
import type { Fields, Files, File, Options } from 'formidable';
import formidable from 'formidable';
import fs from 'fs/promises';
import path from 'path';
import { spawn } from 'child_process';
import { existsSync, mkdirSync } from 'fs';

export const config = {
  api: {
    bodyParser: false,
  },
};

interface PredictionResponse {
  prediction: string;
  confidence?: number;
  error?: string;
  details?: any;
}

interface FileTypeInfo {
  mimetype?: string;
}

const ensureDirectoryExists = (dir: string) => {
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }
};

const saveBase64Image = async (base64Data: string, uploadDir: string): Promise<string> => {
  const matches = base64Data.match(/^data:image\/([A-Za-z-+\/]+);base64,(.+)$/);
  if (!matches || matches.length !== 3) {
    throw new Error('Invalid base64 image data');
  }

  const buffer = Buffer.from(matches[2], 'base64');
  const fileName = `drawing-${Date.now()}.png`;
  const filePath = path.join(uploadDir, fileName);
  
  // Convert Buffer to Uint8Array
  const uint8Array = new Uint8Array(buffer.buffer, buffer.byteOffset, buffer.byteLength);
  await fs.writeFile(filePath, uint8Array);
  return filePath;
};

const isValidImageType = (file: File): boolean => {
  // Check file extension
  const fileExtension = path.extname(file.originalFilename || '').toLowerCase();
  const validExtensions = ['.jpg', '.jpeg', '.png', '.gif'];

  if (!validExtensions.includes(fileExtension)) {
    return false;
  }

  // Check MIME type
  const mimeType = (file.mimetype || '').toLowerCase();
  const validMimeTypes = [
    'image/jpeg',
    'image/jpg',
    'image/png',
    'image/gif',
    'image/pjpeg',  // Progressive JPEG
    'image/x-png'   // Older PNG type
  ];

  return validMimeTypes.includes(mimeType);
};

const parseFormData = async (req: NextApiRequest): Promise<[Fields, Files]> => {
  return new Promise((resolve, reject) => {
    const uploadDir = path.join(process.cwd(), 'user_inputs');
    ensureDirectoryExists(uploadDir);

    const formOptions: Options = {
      uploadDir,
      keepExtensions: true,
      maxFileSize: 5 * 1024 * 1024, // 5MB
      filter: function ({ mimetype }: FileTypeInfo) {
        return (mimetype || '').toLowerCase().startsWith('image/');
      },
    };

    const form = formidable(formOptions);

    form.parse(req, (err: Error | null, fields: Fields, files: Files) => {
      if (err) reject(err);
      resolve([fields, files]);
    });
  });
};

const parseJsonRequest = async (req: NextApiRequest): Promise<{ image?: string }> => {
  const chunks: Uint8Array[] = [];
  
  for await (const chunk of req) {
    chunks.push(chunk);
  }
  
  const data = JSON.parse(Buffer.concat(chunks).toString('utf8'));
  return data;
};

const runPythonScript = async (imagePath: string): Promise<{ prediction: string; confidence?: number }> => {
  return new Promise((resolve, reject) => {
    console.log('Running Python script with image path:', imagePath);
    const pythonProcess = spawn('python3', [
      path.join(process.cwd(), 'src', 'predict.py'),
      '--image', imagePath
    ]);

    let stdout = '';
    let stderr = '';

    pythonProcess.stdout.on('data', (data) => {
      stdout += data.toString();
      console.log('Python stdout:', data.toString());
    });

    pythonProcess.stderr.on('data', (data) => {
      stderr += data.toString();
      console.error('Python stderr:', data.toString());
    });

    pythonProcess.on('close', (code) => {
      console.log('Python process closed with code:', code);
      console.log('Full stdout:', stdout);
      console.log('Full stderr:', stderr);

      if (code !== 0) {
        return reject(new Error(`Python process exited with code ${code}\nError: ${stderr}`));
      }

      const predictionMatch = stdout.match(/Predicted class for .+: (.+)/);
      const confidenceMatch = stdout.match(/Confidence: ([\d.]+)/);
      
      if (!predictionMatch) {
        return reject(new Error('Could not parse prediction from output'));
      }

      resolve({
        prediction: predictionMatch[1].trim(),
        confidence: confidenceMatch ? parseFloat(confidenceMatch[1]) : undefined
      });
    });
  });
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<PredictionResponse>
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ prediction: '', error: 'Method not allowed' });
  }

  const uploadDir = path.join(process.cwd(), 'user_inputs');
  ensureDirectoryExists(uploadDir);

  // Clean up old files
  try {
    const files = await fs.readdir(uploadDir);
    await Promise.all(
      files.map((file) => fs.unlink(path.join(uploadDir, file)))
    );
  } catch (error) {
    console.error('Error cleaning up directory:', error);
  }

  try {
    let imagePath: string;

    // Check if the request contains base64 image data
    const contentType = req.headers['content-type']?.toLowerCase() || '';
    if (contentType.includes('application/json')) {
      const data = await parseJsonRequest(req);
      
      if (!data.image) {
        return res.status(400).json({ prediction: '', error: 'No image data provided' });
      }

      imagePath = await saveBase64Image(data.image, uploadDir);
    } else {
      // Handle multipart form data
      const [_, files] = await parseFormData(req);
      const file = files.image as File;

      if (!file) {
        return res.status(400).json({ prediction: '', error: 'No image uploaded' });
      }

      if (!isValidImageType(file)) {
        return res.status(400).json({ 
          prediction: '', 
          error: 'Invalid file type. Please upload a JPG, JPEG, PNG, or GIF image.' 
        });
      }

      imagePath = file.filepath;
    }

    console.log('Image path before prediction:', imagePath);

    try {
      const result = await runPythonScript(imagePath);
      return res.status(200).json(result);
    } finally {
      // Clean up the uploaded file
      try {
        await fs.unlink(imagePath);
      } catch (error) {
        console.error('Error removing uploaded file:', error);
      }
    }
  } catch (error) {
    console.error('Error processing request:', error);
    return res.status(500).json({ 
      prediction: '', 
      error: 'Internal server error', 
      details: error instanceof Error ? error.message : String(error)
    });
  }
}
