from flask import Flask, render_template, request
import openai

openai.api_key = 'YOUR_API_KEY'


app = Flask(__name__)

# Set up your ChatGPT API credentials
openai.api_key = 'YOUR_API_KEY'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    condition = request.form['condition']
    severity = request.form['severity']
    message = request.form['message']

    # Combine condition, severity, and message into a single prompt
    prompt = f"Condition: {condition}\nSeverity: {severity}\n\n{message}"

    # Call the ChatGPT API
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Get the generated reply from the API response
    reply = response.choices[0].text.strip()

    return render_template('index.html', reply=reply)


if __name__ == '__main__':
    app.run()

