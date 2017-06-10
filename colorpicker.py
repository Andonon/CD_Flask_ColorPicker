'''Coding Dojo Assignment, Flask Fundamentals, "Color Picker"
    by Troy Center June 2017, troycenter1@gmail.com
'''
#pylint: disable=C0103

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    '''Home page'''
    print request.form
    
    redcolor = request.form['red']
    greencolor = request.form['green']
    bluecolor = request.form['blue']

    return render_template('colorpicker.html', redcolor=redcolor,
                           bluecolor=bluecolor, greencolor=greencolor)

app.run(debug=True)
