from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
#GET from SG to US, and POST is US to SG
def index():
        return(render_template("index.html"))
#Run in the cloud. #__name__ is to confirm that this is the application to run.
if __name__=="__main__":
    app.run()   #If run, then it is to open in browser