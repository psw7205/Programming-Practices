from flaskr import blog
from flaskr import auth
import os

from flask import Flask

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev',
    # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

app.register_blueprint(auth.bp)

app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


app.run(host="127.0.0.1", port="5000", debug=True)
