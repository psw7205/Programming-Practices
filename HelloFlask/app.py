from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/route1')
def route_test():
    return render_template('route1.html')


@app.route('/form')
def form_test():
    return render_template('form.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    print(request.method)
    return render_template('result.html')


if __name__ == '__main__':
    app.run()
