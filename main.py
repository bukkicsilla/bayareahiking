
#source activate mynewflaskenv
#export FLASK_APP=app.py (MacOS, Limux)
#set FLASK_APP=app.py (windows)
#flask db init
#flask db migrate -m "message"
#flask db upgrade


from hiking import app
from flask import render_template
#from random import choice

@app.route('/')
def index():
    return render_template('home.html')
    #return '<h1> Welcome </h1>'


#if __name__ == '__main__':
#    app.run(debug=True)
app.run(host='0.0.0.0', port=8080)