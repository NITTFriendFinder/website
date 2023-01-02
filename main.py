from wsgiref.simple_server import make_server
from flask import Flask, jsonify, make_response, render_template, request, request_started
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')



'''
@app.route('/put')
def function():
    if request.args:
        req = request.args
        return " ".join(f"{k} : {v}" for k, v in req.items())
    return "nothing"


content = {
    "bruh" : {
        "key1" : "value1",
        "key2" : "value2"
    }
}
@app.route('/content')
def content():
    response = make_response(jsonify(content), 200)
    return response

content = {
    "bruh1" : {
        "key1" : "value1",
        "key2" : "value2"
    },
    "bruh2" : {
        "key1" : "value1",
        "key2" : "value2"
    }
}
@app.route("/content/<contentid>")
def orderid(contentid):
    if contentid in content:
        response = make_response(jsonify(content[contentid]), 200)
        return response
    return "order not found"

@app.route("/content/<contentid>", methods=["POST"])
def post_order_details(contentid):
    req = request.get_json()
    if contentid in content:
        response = make_response(jsonify({"error" : "content id already exists"}), 400)
        return response
    content.update({contentid:req})
    response = make_response(jsonify({"message" : "new content created"}), 201)
    return response


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp
    return "no cookie found"

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'
'''


if __name__ == '__main__':
    app.run()