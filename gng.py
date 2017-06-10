'''This is the great number game assignment
Coding Dojo, Python and Flask fundamentals. Studying session data.
Troy Center troycenter1@gmail.com June 2017'''
#pylint: disable=c0111,c0103
from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = 'a456lkas-049amp08a349u#$%ams'

def getrandomnum():
    import random
    random_num = random.randint(1, 100)
    return 'random_num'

@app.route('/')
def greatnumbergame():
    return render_template('gng.html')

@app.route('/checknumbers', methods=['post'])
def checknumbers():
    print "got post info"
    print request.form
    session['guess'] = guess
    #get a number
    highlowwin = ""
    itsnumber = getrandomnum()
    guess = session['guess']
    if itsnumber == guess:
        highlowwin = "win"
    elif guess < itsnumber:
        highlowwin = "high"
    elif guess < itsnumber:
        highlowwin = "low"
    return redirect('/', highlowwin)


app.run(debug=True)