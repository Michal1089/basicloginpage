from flask import Flask,request, render_template,redirect,url_for,session

app = Flask(__name__)
app.secret_key = 'Dima to pidor'
users ={
    'user1':'password123',
    'admin1':'admin123'
}


@app.route("/",methods=["GET","POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            error = "Nieprawidłowe hasło lub nazwa użytkownika"

    return render_template('index.html',error = error)

@app.route('/welcome')
def welcome():
    if 'username'not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('main.html',username=username)
    

if __name__ =='__main__':
    app.run(debug=True)

