from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'yo this is sneakky'


# Routing
@app.route('/')
def main():
    '''
    renders the biz
    '''
    # have i been here yet?
    if 'counter' in session:
        print 'you have been here!'
        session['counter'] += 314
    else:
        print 'you havent sessioned yet'
        session['counter'] = 100
    return render_template('index.html', counter=session['counter'])

@app.route('/clickify')
def clicked():
    '''
    processes the clicking
    '''
    session['counter'] = session['counter'] + 87
    return redirect('/')

app.run(debug=True)
