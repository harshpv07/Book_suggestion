from flask import Flask,render_template,jsonify,flash
app=Flask(__name__)
@app.route('/')
def profile():
    flash("hello frinds",)
    return render_template('profile.html')
@app.errorhandler(404)
def page_not_found():

    return ("Page not found")

if __name__=="__main__":
    app.run(debug=True)

