from flask import Flask, g, render_template, url_for
from redis import Redis

from app.common.app_logger import AppLogger

logger = AppLogger().get_logger()

app = Flask(__name__,
            static_url_path='',
            static_folder="static")


@app.route('/')
@app.route('/login')
def login():

    logger.info("Got the login page.")
    return render_template("login.html")


@app.route('/index')
def index():

    return render_template("index.html")