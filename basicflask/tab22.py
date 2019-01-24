from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def conn():
    
    dic={"prati":100,"teju":100}
    print(dic)
    return render_template('tab2.html',conn=dic)
    
if __name__=='__main__':
    app.run(debug=True)
