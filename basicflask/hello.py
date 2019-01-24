from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
        return 'Hello Pratiksha'

@app.route("/about")
def index1():
        return 'python workshop'
@app.route("/hi/<name>")
def index2(name):
    return 'hello '+name
@app.route("/hii/<int:num><float:num2>")
def index3(num,num2):
    return 'number is %d float num is %f' %num,%num2
if __name__=="__main__":
    app.run(debug=True)
