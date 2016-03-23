from flask import Flask, abort

app = Flask(__name__)

ages = {
    'bob': '43',
    'alice': '29'
}

@app.route('/users/<user>')
def users(user):
    age = ages.get(user)
    if age:
        return '%s is %s years old' % (user,age)
    else:
        abort(404)


@app.route('/')
def hello_world():
    return 'Hello Worlds!'


if __name__ == '__main__':
    app.run(debug=True)
