from flask import Flask, request, jsonify
from flask_cors import CORS
from classifier import classify_article

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define API endpoint for text classification
@app.route('/classify', methods=['POST'])
def classify_text():
    # Parse input data
    data = request.json
    text = data['text']
    categories = data['categories']

    result = classify_article(text, categories)

    # Return predicted category as JSON response
    response = {'category': result['labels'][0]}
    return jsonify(response)

# Run Flask app
if __name__ == '__main__':
    app.run()