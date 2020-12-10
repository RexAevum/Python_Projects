"""
virtualenv - virtual enviornment 
"""
# Using flask to build a very basic website
from flask import Flask, render_template

# instantiate the Flask class to store the flask object
app = Flask(__name__)

# The Flask().route() is the file path from the root folder of the app 
# @app.rout('/') -> localhost:5000/
# @app.rout('/about/') -> localhost:5000/about/
@app.route('/')
# this will be run once user is at the specified directory
# FIXME - when using the render_templates function, the templates need to be stored in a folder called - templates
# otherwise you will get an error
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

# When you run a python script, the file that serves as the main script (the one you call python __fileName__.py)
#  will get the __name__ == '__main__'
if __name__ == "__main__":
    app.run(debug=True)

# If it is not the main file that is ran, instead the __name__ == "__fileName__.py"
# This is done so that a sertain section of code is only run when the script is called by the user