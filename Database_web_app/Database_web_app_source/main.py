"""
    This web app will allow users to enter their email, height and age, which will be added to a database. if the entry is accepted (not duplicat)
    the user will receive a dynamicaly generated email that shows the values they have entered, as well as the average height and age
    of all the survery participants.

    Used technology: Flask, SQLAlchemy, postgres2
"""
import flask
from flask import Flask, render_template, request
# For SQLAlchemy to work with postgres, need to install posgres2
from flask_sqlalchemy import SQLAlchemy 
from send_email import send_email # script will send email
from sqlalchemy.sql import func # to querry averages

# Create a flask app and connecting it to a db
app = Flask(__name__)
#URI ==> {server used}://{username}:{password}@{server IP}/{DB Name}
#####> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin2020@localhost:5432/STATISTICS'
DATABASE_URI = "postgres://tsebefzqhmwuid:e8908ecc5b419e4d6cffdc77bd27fe5426b192ce3bf038741363e2f1268c0057@ec2-52-203-182-92.compute-1.amazonaws.com:5432/da2po38ucb5m9c?sslmode=require"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

# create a table in the db
class Data(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(150), unique=True)
    height_ = db.Column(db.Integer)
    age_ = db.Column(db.Integer)

    def __init__(self, email, height, age):
        self.email_ = email
        self.height_ = height
        self.age_ = age


@app.route('/') # by efault this is a GET method
def index():
    return render_template('index.html')

@app.route('/success/', methods=['POST']) # if you want to specify another method
def success():
    if request.method == 'POST':
        #print(request.form)
        # get values from 
        email = request.form['userEmail'] # the defined name= variable in html is what you add here
        height = request.form['userHeight']
        age = request.form['userAge']
        # make sure no duplicates by counting instances of email in the db
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            # FIXME - important
            # create an instance of our table object
            data = Data(email, height, age)
            # add to db
            db.session.add(data)
            # commit to db
            db.session.commit()

            # get avg height and age from db
            avgHeight = db.session.query(func.avg(Data.height_)).scalar() # generates sql statement without .scalar()
            avgAge = db.session.query(func.avg(Data.age_)).scalar()
            # Format float
            avgHeight = round(avgHeight, 1)
            avgAge = round(avgAge, 1)
            # Get participant count
            participants = db.session.query(Data).count()
            # send the email
            send_email(email, height, age, avgHeight, avgAge, participants)
            # if everything went ok, move to the got_data.html screen
            return render_template('got_data.html')
        return render_template('index.html',
         text="Email address already registered. Please use a different email.")



# Check if file is main (the executed script)    
if __name__=='__main__':
    app.debug = True
    #db.create_all() #only needed first time
    app.run(port=5000)
    db.close_all_sessions()