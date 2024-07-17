import openai
from flask import Flask, request, jsonify

# Initialize OpenAI
openai.api_key = "your_openai_api_key"

# Create Flask app
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)