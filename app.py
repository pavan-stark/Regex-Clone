from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def index_page():
    
    if request.method == 'POST':
        #Capturing the data from the frontend
        reg_exp = request.form['reg_exp']  
        txt = request.form['txt']
        c = 0
        matches = []

        for i in re.finditer(reg_exp,txt):
            st = ""
            c = c+1
            st = st+"Match {} for '{}': Start index {} and End index {}".format(c,i.group(),i.start(),i.end())
            matches.append(st) 

        #returning the variables from the backend so that we can display it back to the frontend
        return render_template('index.html', count = c, matches = matches, t = txt, reg = reg_exp)
    return render_template('index.html', count = -1)


if __name__ == '__main__':
    app.run(debug=True)
