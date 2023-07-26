import logging
from flask import Flask

from logconfig import LOGGING
from logging import config

config.dictConfig(LOGGING)
log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def hello_world():
    log.info("Hello World was called")
    log.error("Hello World was called error")
    return "<p>Hello, World!</p>"