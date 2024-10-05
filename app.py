from flask import Flask, render_template, request #flask is a web framework for Python that allows one to build web application.
#Create model for faq
import google.generativeai as genai
import os

model = genai.GenerativeModel ("gemini-1.5-flash")
api=os.getenv("MAKERSUITE") #hide api (like a private key/ pw)
genai.configure(api_key= "AIzaSyCFAOkFd5qjen2xJmfrQjbYAq4pb9oz7fI")

app = Flask(__name__) #create an instance of the web framework for python, where name = root path of the application
@app.route("/",methods=["GET","POST"]) #use flask to map to root URL endpoint denoted by "/". #GET = retrieve from server when URL is accessed, #POST = submit a form
#GET from SG to US, and POST is US to SG
def index(): #when "/" is called, generate function called index
        return(render_template("index.html")) # Flask function will look to index.html under templates for the generation

@app.route("/prediction_DBS",methods=["GET","POST"]) 
def prediction_DBS(): #when "/prediction_DBS" function is called
        return(render_template("prediction_DBS.html")) #Flask function will look to "prediction_DBS.html" under templates to generate

#Setting up the Results Page
@app.route("/prediction_result_DBS",methods=["GET","POST"])
def prediction_result_DBS():
        q=float(request.form.get("q")) # wsgi is text by default, therefore to force to float, where q is the variable
        r=(-50.6*q)+90.2
        return(render_template("prediction_result_DBS.html",r=r)) #synchronise front and back-end.

#Function to run the Button at the Front End
@app.route("/faq",methods=["GET","POST"])
def faq():
        return(render_template("faq.html")) #synchronise front and back-end.

#Setting up Reply page for the 2 questions button
@app.route("/q1",methods=["GET","POST"])
def q1():
        r= model.generate_content ("How should I diversify my investment portfolio")
        return(render_template("q1_reply.html",r=r)) #synchronise front and back-end.

@app.route("/q2",methods=["GET","POST"])
def q2():
        q=request.form.get("q")
        r= model.generate_content(q)
        return(render_template("q2_reply.html",r=r)) #synchronise front and back-end.

#Function to run the Button at the Front End
@app.route("/predictcreditability",methods=["GET","POST"])
def predictcreditability():
        return(render_template("predictcreditability.html")) #synchronise front and back-end.

#Setting up the Predict Credibility Result Page
@app.route("/predictcreditability_result",methods=["GET","POST"])
def predictcreditability_result():
        q=float(request.form.get("q")) # wsgi is text by default, therefore to force to float, where q is the variable
        r=(-0.00011807*q)+1.20396988
        return(render_template("predictcreditability_result.html",r=r)) #synchronise front and back-end.
          
#Run in the cloud. #__name__ is to confirm that this is the application to run.
if __name__=="__main__":
    app.run()   #If run, then it is to open in browser
