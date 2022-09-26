from flask import request, Flask

app = Flask(__name__)

from src import routes
