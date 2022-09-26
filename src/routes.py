from . import app


@app.route('/healthcheck', strict_slashes=False)
def healthcheck():
    return 'All good'


@app.route('/', strict_slashes=False)
def index():
    return 'First page'
