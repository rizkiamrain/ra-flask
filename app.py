from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']

    suhu = 13
    return render_template('index.html',items = hari, suhu = suhu, judul = 'Home')


@app.route('/variabel')
def variabel():
    hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']

    suhu = 13
    return render_template('variabel.html',hari = hari, suhu = suhu, judul = 'Variabel')

@app.route('/profil')
def profil():
    return render_template('profil.html', judul = 'Profil')

@app.route('/contact')
def contact():
    return render_template('contact.html', judul = 'Contact')

@app.route("/redirect-profil")
def ra_redirect_profil():
    return redirect(url_for('profil'))

if __name__=='__main__':
    app.run(debug=True, port=5001)