from flask import Flask, request, abort

app = Flask(__name__)

from event_handler import bandwidth_handler

if __name__ == '__main__':
    app.run() 