## Python Flask Harness for GPT-3 Chat

This is a `simple Flask` application that allows users to chat with GPT-3 using the `text-davinci-003` model. The application has a chat page that takes user input and generates a response from GPT-3, and it also stores the conversation data in a file for later analysis.

The code uses the [OpenAI](https://openai.com/) Python library to interact with the GPT-3 model and generate responses.

To use the application, you will need to set up your OpenAI API key and install the required dependencies. See the instructions below for details.

### Installation

1. Clone the repository and navigate to the project directory:

    ```
    git clone https://github.com/amcmurchie/gpt3-chat.git
    cd gpt3-chat
    ```

2. Create a file called `.KEY.txt` in the project directory and add your OpenAI API key to the file.

3. Install the required dependencies using `pip`:

    ```
    pip install -r requirements.txt
    ```

4. Run the Flask app using the following command:

    ```
    python app.py
    ```

5. Open `http://127.0.0.1:5000/chat` in your web browser to access the chat page.

### Terminal-only version

In addition to the Flask app, this code also includes a terminal-only version that can be run by calling the `conversation()` function directly, without using the Flask app or the `/conversation` route. This allows you to test the conversation functionality without running the web application.

To use the terminal-only version, you can run the following command in the project directory:

```shell
python -c "from app import conversation; conversation()"
```


This will start a conversation with GPT-3 and print the responses to the terminal. The conversation data will also be written to the `conversation.txt` file in the project directory.




