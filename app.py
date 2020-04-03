from flask import Flask, request
import os

app = Flask(__name__)
@app.route('/', methods=['GET'])
def receive_message():
    print(os.environ['url'])
    return ";)"

if __name__ == '__main__':
    app.run()
