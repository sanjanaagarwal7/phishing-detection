import sys
import pickle
import os

def main():
    # Check if URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python predictor.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]

    # Get current script directory
    current_dir = os.path.dirname(__file__)
    # Go up two folders (from backend/python to project root), then into train_model folder
    model_path = os.path.join(current_dir, '..', '..', 'train_model', 'phishing_model.pkl')
    model_path = os.path.abspath(model_path)  # get absolute path

    # Load the saved model and vectorizer
    with open(model_path, 'rb') as f:
        classifier, vectorizer = pickle.load(f)

    # Vectorize the input URL
    url_vector = vectorizer.transform([url])

    # Predict using the loaded model
    prediction = classifier.predict(url_vector)

    # Print 0 for Good, 1 for Bad URL
    print(int(prediction[0]))

if __name__ == "__main__":
    main()
