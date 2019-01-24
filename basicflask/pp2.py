from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def conn():
    sname="prati"
    a='A'
    b='B'
    list=[1,2,3,4,5]
    dic={"sona","mona"}
    return render_template('prati.html',sname=sname,list=list,dic=dic)
    
if __name__=='__main__':
    app.run(debug=True)
