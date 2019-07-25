from flask import Flask, render_template, request
import db

app = Flask(__name__)


@app.route('/')
def root_route():
    return render_template('index.html', list=db.get_list())


@app.route('/result', methods=['get'])
def result_route():
    data = request.args['code']
    return render_template('index.html', data=db.find_list(data))


if __name__ == '__main__':
    app.run(debug=True)
