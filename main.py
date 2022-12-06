from flask import Flask, request,render_template
import openai

app = Flask(__name__)

# CLEAR OUT CONVO FILE
open('conversation.txt','w')

# Load your API key from an environment variable or secret management service
keyFile = open('.KEY.txt','r')
openai.api_key = keyFile.read()

history = []


#  POST CONVERSATION
@app.route('/conversation', methods=['POST'])
def conversation():
    question = request.form['question']
    history.append({'prompt': question})
    history_str = "\n".join([h['prompt'] for h in history])

    response = openai.Completion.create(model="text-davinci-003", prompt=history_str, temperature=0, max_tokens=3000)

    with open('conversation.txt', 'a') as f:
        f.write(f"{question}\n")
        for c in response['choices']:
            f.write(f"{c['text']}\n")

    return response

#  CHAT
@app.route('/chat')
def chat():
    return render_template('chat.html')


#  SHUTDOWN
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run()
