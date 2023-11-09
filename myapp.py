from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/produk")
def produk():
    return render_template('produk.html')

@app.route("/GIFT")
def GIFT():
    return render_template('GIFT.html')

@app.route("/CONTACT")
def CONTACT():
    return render_template('CONTACT.html')    

if __name__ == "__main__":
    app.run(debug = True)