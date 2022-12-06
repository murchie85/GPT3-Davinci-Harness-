import os
import openai


# CLEAR OUT CONVO FILE
open('conversation.txt','w')


# Load your API key from an environment variable or secret management service
keyFile = open('.KEY.txt','r')
openai.api_key = keyFile.read()

history = []
exit = False
while not exit:
    question = input("Ask your question \n")
    history.append({'prompt': question})
    history_str = "\n".join([h['prompt'] for h in history])
    response = openai.Completion.create(model="text-davinci-003", prompt=history_str, temperature=0, max_tokens=4000)

    #print(response)
    print('\n\n\n')

    for c in response['choices']:
        print(c['text'])

    print('\n')
