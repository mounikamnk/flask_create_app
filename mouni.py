from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/wish')
def wish():
    return '<center><h1>Hi how are you<h1></center>'
@FAI.route('/first')
def first():
    return render_template('first.html',name='mouni',age=24)

if __name__=='__main__':
    FAI.run(debug=True)
