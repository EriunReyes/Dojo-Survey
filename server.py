from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secretkey'
@app.route('/')
def index():
    return render_template('/index.html')



@app.route('/form', methods=['POST'])
def form():
    session['k_name'] = request.form['k_name']
    session['k_location'] = request.form['k_location']
    session['k_favorite'] = request.form['k_favorite']
    session['k_comments'] = request.form['k_comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('/results.html')
@app.route('/reset')
def reset():
    sesion.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)