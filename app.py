from flask import Flask, request, abort

app = Flask(__name__)

from event_handler import user_handler

if __name__ == '__main__':
    app.run() 