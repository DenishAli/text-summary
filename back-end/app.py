from flask import Flask, request, jsonify
from textSummary import summrization
from pegasusSummary import summaryGen
from spacySummary import text_summarization
from flask_cors import CORS


app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/genereate_summary', methods=['POST'])
def genereate_summary():
    data = request.get_json()
    text = data.get('text', '')
    processed_text = summrization(text)
    # processed_text = summaryGen(text)
    # processed_text = text_summarization(text)

    
    # # Perform your data processing here
    # processed_text = text.upper()  # Example: Convert text to uppercase
    return jsonify({'processed_text': processed_text})

if __name__ == '__main__':
    app.run(debug=True)
