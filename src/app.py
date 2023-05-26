from flask import Flask, request, jsonify
from flask_cors import CORS
from classifier import classify_article
from summarizer import summarize_article

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define API endpoint for text classification
@app.route('/classify', methods=['POST'])
def classify_text():
    # Parse input data
    data = request.json
    text = data['text']

    result = classify_article(text)

    # Return predicted category as JSON response
    response = {'category': result['labels'][0]}
    return jsonify(response)

@app.route('/summarize', methods=['POST'])
def summarize_text():
    # Parse input data
    data = request.json
    text = data['text']

    result = summarize_article(text)

    # Return predicted category as JSON response
    response = {'summary': result[0]['summary_text']}
    return jsonify(response)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)