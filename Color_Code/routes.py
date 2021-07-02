from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')



@app.route('/Colorcode.html')
def Colorcode():
    return render_template('Colorcode.html') 



if __name__ == '__main__':
    app.run(debug=True)

    
