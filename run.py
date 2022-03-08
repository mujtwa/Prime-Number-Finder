import constants as const
from logic import *
from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/find',methods=['GET','POST'])
def finder_funcion():
    try:
        list_val=[int(value) for value in request.form.values()]
        result=calculate_prime(list_val[0],list_val[-1])
        return render_template('result.html',value=result)
    except:
        print("Error Occurred : In finder function")
if __name__=='__main__':
    app.run(debug=True)