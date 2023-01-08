from flask import Flask,render_template

#create a flask instance(Sub dir)

app=Flask(__name__)

# create  a route  decorator 

@app.route('/')
# def index():
#     return "<h1>Hello World! </h1>"

def index():
    first_name="shivam is good Men "

    fav_pizza=["pizza","burger"]

    return render_template("index.html",first_name=first_name,fav_pizza=fav_pizza)

@app.route('/user/<name>')
def user(name):
    # return "<h1>hello {} </h1>".format(name)
    return render_template("user.html",user_name=name)


#create custom error page and 
#1 invalid url error 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


#2 internal server error 
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500
