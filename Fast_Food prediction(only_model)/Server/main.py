from flask import Flask,request,render_template,redirect,url_for
from util import predict_item

app=Flask(__name__)

@app.route('/')
def index(r=''):
    return render_template('index.html',result=r)

@app.route('/result',methods=["POST",'GET'])
def result():

    calories=request.form.get('calories')
    fat=request.form.get('fat')
    sugar=request.form.get('sugar')
    protein=request.form.get('protein')

    result=predict_item(calories,fat,sugar,protein)

    return  render_template('index.html',result=result)








if __name__=='__main__':
    app.run(debug=True)