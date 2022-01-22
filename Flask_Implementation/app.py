from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import urllib
import os

app = Flask(__name__)

data = {}

#########################SQL Alchemy Configuration#############

basedir=os.path.abspath(os.path.dirname(__file__))
print(basedir)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)
Migrate(app,db)
##############################################################
######################Create a model #########################
class Shorten_Url(db.Model):
    __tablename__='shorten_urls'
    id=db.Column(db.Integer,primary_key=True,)
    website=db.Column(db.Text)
    short_web=db.Column(db.Integer)

    def __init__(self,website,short_web):
        self.website=website
        self.short_web=short_web
    
    def __repr__(self):
        return "{} = {}".format(self.website,self.short_web)
###############################################################

@app.route('/')
def home_get():
    return render_template('index.html')

@app.route('/', methods=["GET","POST"])
def home_post():
    if request.method=="POST":
        original_url = request.form.get('in_1')
        shorten_url = random.randint(1000, 9999)
        data[shorten_url] = original_url
        web_with_short=Shorten_Url(original_url,shorten_url)
        db.session.add(web_with_short)
        db.session.commit()

    return render_template('index.html')

@app.route('/history')
def history_get():
    short_tr=Shorten_Url.query.all()
    return render_template('history.html',short_tri=short_tr)

@app.route('/sh/<url>')
def fun(url):
    if int(url) in data:
        return "Redirecting to {}".format(data[int(url)])
        
    return "Incorrect URL"
######################################

if __name__ == "__main__":
    app.run(debug=True)