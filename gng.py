'''This is the great number game assignment
Coding Dojo, Python and Flask fundamentals. Studying session data.
Troy Center troycenter1@gmail.com June 2017'''
#pylint: disable=c0111,c0103
from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = 'a456lkas-049amp08a349u#$%ams'

def getrandomnum():
    import random
    return random.randint(1, 100)

@app.route('/')
def greatnumbergame():
    return render_template('gng.html')

@app.route('/checknumbers', methods=['post'])
def checknumbers():
    print "===line 21 got post info==="
    print "=== line 22 ===",request.form
    guess = 0
    random = 0
    guess = int(request.form['guess'])
    print "==line 26 Guess is==", guess

    if session['npcnum'] == 0:
        print "=== line 29 npcnum0=== ", session['npcnum']
        session['npcnum'] = getrandomnum()
        print "===line 31 npcnum1=== ", session['npcnum']
        random = session['npcnum']
        print "===line 33 npcnum2=== ", session['npcnum']
        print "===line 34 random0=== ", session['npcnum']
    else:
        random = session['npcnum']
        print "===line 28 did not run==="

    print "==line 39 Randomnum is==", session['npcnum']

    if random == guess:
        print "===line 39 random is===: ", random
        print "===line 40 guess is ===: ", guess
        print "===line 41 I see a win==="
        return redirect('/')
    elif random > guess:
        print "===line 43 random is===: ", random
        print "===line 44 guess is ===: ", guess
        print "===line 45 I see you're too low==="
        return redirect('/')
    elif random < guess:
        print "===line 47 random is===: ", random
        print "===line 48 guess is ===: ", guess
        print "===line 49 I see you're too high.==="
        return redirect('/')

app.run(debug=True)