from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    # Replace this with the actual API endpoint of the Groq AI llama-3.1-8b-instant model
    groq_api_url = 'https://api.groq.ai/llama3.1-8b-instant'

    # Make a request to the Groq AI model
    response = requests.post(groq_api_url, json={'prompt': user_message})
    
    if response.status_code == 200:
        result = response.json()
        bot_message = result.get('response')
        return jsonify({'response': bot_message}), 200
    else:
        return jsonify({'error': 'Failed to get response from Groq AI model.'}), 500

if __name__ == '__main__':
    app.run(debug=True)