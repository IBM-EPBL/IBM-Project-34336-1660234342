from flask import Flask,render_template,request
#from flask import Flask,render_template,request
app = Flask(__name__,template_folder='templates')
@app.route('/')



@app.route('/test/<user>')
def test_html():
    return render_template("chatbot.html")


if __name__ =='__main__':
    app.run(debug=True)
