from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template ( "index.html", title='О сайте', tit='Главная страница', menu='Weather', menu2='Communication', menu3='News')

@app.route('/w')
def w():
    return render_template ('weathers.html', weather = 'Погода!', )

@app.route('/n')
def a():
    return render_template ('news.html', news='Новости!')

@app.route('/c')
def c():
    return render_template ('communication.html',  tele = 'Курсы валют!')

 
if __name__ == "__main__":
   app.run(debug=True)