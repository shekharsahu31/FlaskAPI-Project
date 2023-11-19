from flask import Flask,request # request lib will be used to check the request made is get or post
from flask import render_template # render_temp lib will be used to display a whole webpage in a get method function 
                                  # put the webpage in templates named folder.
                                  # can also we used to pass variable internally
from flask import redirect, url_for # used for redirect to a internal URL
from flask import jsonify # used to convert anything we give it to JSON format.

app=Flask(__name__)

@app.route("/" , methods = ["GET"])
def welcome():
    return "Welcome to Main Page" 

@app.route("/index" , methods = ["GET"])
def index():
    return "Welcome to Index Page" 

'''@app.route("/success/<score>" , methods = ["GET"])
def success(score):
    return "The score is "+ score  ''' # To make variable - use <a>

@app.route("/success/<int:score>" , methods = ["GET"])
def success(score):
    return "The score is "+ str(score)

@app.route("/fail/<int:score>" , methods = ["GET"])
def fail(score):
    return "The score is "+ str(score)   # WE can use this score as a header/ url information in function to use if/else  
                                         # or mapping to do a specific task related to the values of score.

@app.route("/result/<int:score>" , methods = ["GET"])
def result(score):
    if score > 50:
        return "You are PASS and your score is " + str(score)
    else:
        return "You are; FAIL and your score is " + str(score)
    

@app.route("/form" , methods= ["GET" , "POST"])    
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths']) #float as the incoming value is str, request.form['maths'] form me se maths name ki field ki value.
        science = float(request.form['science'])
        history = float(request.form['history'])

        average = (maths+science+history)/3

        '''if average > 50:
            return "You are PASS and your avg. score is " + str(average)
        else:
            return "You are FAIL and your avg. score is " + str(average)'''
        
        # return render_template('form.html' , score=average) #using jinja2 engine we are able to send dynamic variable here and there.

        res=""
        if average>50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res , score=average))
    
@app.route("/api" , methods=["POST"])
def cal_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    sum = a_val + b_val
    return jsonify(sum) # now will use POSTMAN To read this API , IN url put /api vali puri URL
                                # body - raw - json -> put simple json like test.json and go for it.

if __name__ == "__main__":
    app.run(debug=True)