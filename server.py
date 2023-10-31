from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'martina'


@app.route('/')         
def index():
    if "visitas" not in session:
        session["visitas"] = 0
    else:
        session["visitas"] += 1
    return render_template("index.html", visitas= session["visitas"])

@app.route('/destroy_session')
def destruir ():
    session.clear()
    return redirect("/")




if __name__=="__main__":   
    app.run(debug=True)