from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
#GET from SG to US, and POST is US to SG
def index():
        return(render_template("index.html"))

@app.route("/prediction_DBS",methods=["GET","POST"])
def prediction_DBS():
        return(render_template("prediction_DBS.html"))

@app.route("/prediction_result_DBS",methods=["GET","POST"])
def prediction_result_DBS():
        q=float(request.form.get("q")) # wsgi is text by default, therefore to force to float, where q is the variable
        r=(-50.6*q)+90.2
        return(render_template("prediction_result_DBS.html",r=r)) #synchronise front and back-end.
                              
#Run in the cloud. #__name__ is to confirm that this is the application to run.
if __name__=="__main__":
    app.run()   #If run, then it is to open in browser