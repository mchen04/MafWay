import tensorflow as tf
import numpy as np
from PIL import Image
import os
import argparse
import sys

def find_model():
    """Find the model file by searching in different possible locations."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    possible_locations = [
        os.path.join(project_root, 'model.h5'),  # Project root
        os.path.join(os.path.dirname(script_dir), 'model.h5'),  # projectsite directory
        'model.h5',  # Current directory
    ]
    
    for location in possible_locations:
        if os.path.exists(location):
            return location
    
    return None

def setup_model():
    try:
        # Find model file
        model_path = find_model()
        if not model_path:
            print("Error: Could not find model.h5 file. Please ensure it exists in the project directory.", 
                  file=sys.stderr)
            sys.exit(1)
            
        print(f"Loading model from: {model_path}", file=sys.stderr)
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {str(e)}", file=sys.stderr)
        sys.exit(1)

# Load the class labels
class_labels = ['!', '(', ')', '+', ',', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=',
              'A', 'alpha', 'ascii_124', 'b', 'beta', 'C', 'cos', 'd', 'Delta', 
              'div', 'e', 'exists', 'f', 'forall', 'forward_slash','G', 'gamma', 'geq', 'gt', 'H', 
              'i', 'in', 'infty', 'int', 'j', 'k', 'l', 'lambda', 'ldots', 'leq', 'lim', 'log', 'lt', 
              'M', 'mu', 'N', 'neq', 'o', 'p', 'phi', 'pi', 'pm', 'prime', 'q', 'R', 'rightarrow', 
              'S', 'sigma', 'sin', 'sqrt', 'sum','T', 'tan', 'theta', 'times', 'u', 'v', 'w', 'X', 
              'y', 'z', '[', ']', '{', '}']

def process_image(image_path):
    try:
        # Convert relative path to absolute path if necessary
        if not os.path.isabs(image_path):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            project_dir = os.path.dirname(os.path.dirname(script_dir))
            if os.path.exists(image_path):  # If file exists in current directory
                image_path = os.path.abspath(image_path)
            else:  # Try project directory
                image_path = os.path.join(os.path.dirname(script_dir), image_path)

        print(f"Looking for image at: {image_path}", file=sys.stderr)
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"Error: Image file not found at {image_path}", file=sys.stderr)
            sys.exit(1)

        print(f"Processing image: {image_path}", file=sys.stderr)
        # Open the image file
        image = Image.open(image_path)

        # Convert to grayscale and resize to 45x45
        image = image.convert('L').resize((45, 45))

        # Convert to numpy array and normalize
        image_array = np.array(image)
        image_array = image_array / 255.0
        image_array = np.reshape(image_array, (1, 45, 45, 1))

        return image_array
    except Exception as e:
        print(f"Error processing image: {str(e)}", file=sys.stderr)
        sys.exit(1)

def predict_symbol(model, image_path):
    try:
        # Process the image
        processed_image = process_image(image_path)

        print("Making prediction...", file=sys.stderr)
        # Make prediction
        predictions = model.predict(processed_image, verbose=0)
        predicted_class_index = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_index])
        predicted_class_label = class_labels[predicted_class_index]

        return predicted_class_label, confidence
    except Exception as e:
        print(f"Error making prediction: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Predict mathematical symbol from image')
        parser.add_argument('--image', type=str, help='Path to the image file', required=True)
        args = parser.parse_args()

        print(f"Starting prediction for image: {args.image}", file=sys.stderr)
        
        # Load model
        model = setup_model()

        # Make prediction
        prediction, confidence = predict_symbol(model, args.image)
        
        # Print results
        print(f"Predicted class for {os.path.basename(args.image)}: {prediction}")
        print(f"Confidence: {confidence:.4f}")
    except Exception as e:
        print(f"Error in main execution: {str(e)}", file=sys.stderr)
        sys.exit(1)
