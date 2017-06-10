'''This is the great number game assignment
Coding Dojo, Python and Flask fundamentals. Studying session data.
Troy Center troycenter1@gmail.com June 2017'''
#pylint: disable=c0111,c0103
from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def greatnumbergame():
    print "hello"
    return render_template('gng.html')
    
