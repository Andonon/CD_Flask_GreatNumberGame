'''This is the great number game assignment
Coding Dojo, Python and Flask fundamentals. Studying session data.
Troy Center troycenter1@gmail.com June 2017'''
#pylint: disable=c0111,c0103
from flask import Flask, render_template, session, request

app = Flask(__name__)

app.secret_key = 'a456lkas-049amp08a349u#$%ams'

def getrandomnum():
    import random
    return random.randint(1, 100)

@app.route('/')
def greatnumbergame():
    windisplay = "none"
    lowdisplay = "none"
    highdisplay = "none"
    result = "none"
    return render_template('gng.html', result=result, windisplay=windisplay, 
                           lowdisplay=lowdisplay, highdisplay=highdisplay)

@app.route('/checknumbers', methods=['post'])
def checknumbers():
    print "===line 21 got post info==="
    print "=== line 22 ===", request.form
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
        response = "win"
        windisplay = "block"
        lowdisplay = "none"
        highdisplay = "none"
        return render_template('gng.html', response=response,
                               windisplay=windisplay, lowdisplay=lowdisplay,
                               highdisplay=highdisplay)
    elif random > guess:
        print "===line 43 random is===: ", random
        print "===line 44 guess is ===: ", guess
        print "===line 45 I see you're too low==="
        response = "low"
        windisplay = "none"
        lowdisplay = "block"
        highdisplay = "none"
        return render_template('gng.html', response=response,
                               windisplay=windisplay, lowdisplay=lowdisplay,
                               highdisplay=highdisplay)
    elif random < guess:
        print "===line 47 random is===: ", random
        print "===line 48 guess is ===: ", guess
        print "===line 49 I see you're too high.==="
        response = "high"
        windisplay = "none"
        lowdisplay = "none"
        highdisplay = "block"
        return render_template('gng.html', response=response,
                               windisplay=windisplay, lowdisplay=lowdisplay,
                               highdisplay=highdisplay)

app.run(debug=True)