from flask import Flask, request, Response
import openai
import datetime
import os

app = Flask(__name__)

@app.route('/api/answer', methods=['POST'])
def generate_ai_response():
    # Validate the request body
    if not request.json or 'question' not in request.json:
        return Response("Bad Request: Missing 'question' in request body", status=400)

    question = request.json['question']

    try:
        # Generate the answer using GPT-3.5-turbo
        stream = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=1000,
            stream=True,
        )
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)

    def generate():
        # Stream the response back to the client
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content
        print(f"Finished at {datetime.datetime.now()}")

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run()