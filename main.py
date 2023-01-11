from flask import Flask, request,render_template
from shutil import copyfile
from datetime import datetime
import json

import openai

app = Flask(__name__)

# CLEAR OUT CONVO FILE
open('conversations.txt','w')

# Load your API key from an environment variable or secret management service
keyFile = open('.KEY.txt','r')
openai.api_key = keyFile.read()

history = []


# ----------POST CONVERSATION

@app.route('/conversation', methods=['POST'])
def conversation():
    question = request.form['question']
    history.append({'prompt': question})
    history_str = "\n".join([h['prompt'] for h in history])
    
    # code-davinci-002
    #response = openai.Completion.create(model="code-davinci-002", prompt=history_str, temperature=0, max_tokens=4000)
    response = openai.Completion.create(model="text-davinci-003", prompt=history_str, temperature=0, max_tokens=3000)
    

    with open('conversations.txt', 'a') as f:
        f.write("Question \n" + str(question) + '\n')
        for c in response['choices']:
            f.write(c['text'] + '\n')


    response['formatted'] = [x['text'] + ' \n ' for x in response['choices']]
    response['formatted'] = ' '.join(response['formatted'])
    print("formatted " + response['formatted'] )
    formattedResponse = response['formatted'].replace('\n','<br>')
    formattedResponse = formattedResponse.replace('\r','<br>')

    response['formatted'] = '<br> <b>Response</b> <br> ' + formattedResponse + '<br>'

    return response








# ---------- CHAT

@app.route('/chat')
def chat():
    return render_template('chat.html')


# ---------- SAVE TO FILE

@app.route('/save', methods=['POST'])
def Save():
    if request.method == 'POST':
        # Get the name entered by the user
        name = request.form['name']
        # Generate the filename by appending the current date and time to the name
        filename = f'{name}_{datetime.now().strftime("%Y%m%d%H%M%S")}'
        # Copy the file "conversations.txt" to the "savedConversations" folder
        # with the generated filename
        copyfile('/Users/adammcmurchie/code/tools/davinci/conversations.txt', f'/Users/adammcmurchie/code/tools/davinci/savedConversations/{filename}')
    return('http://127.0.0.1:5000/chat')


# ----------SHUTDOWN

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

# ---------- SHUTDOWN ROUTE

@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run()
