from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap

app = Flask(__name__)
mail = Mail(app)
Bootstrap(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bgitchamnan@gmail.com'
app.config['MAIL_PASSWORD'] = '***'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('mail_form.html')




@app.route('/mail', methods=['POST', 'GET'])
def detail():
   if request.method == 'POST':
       # detail = request.form
       heading = request.form.get("heading")
       reciever = request.form.get("recipient")
       massage = request.form.get("message")

       msg = Message(heading, sender='buchita.gitchamnan@gmail.com', recipients=[reciever])
       msg.body = massage

       mail.send(msg)
       return "Sent"


       # return render_template("main_page.html", detail=detail)


if __name__ == '__main__':
    app.run(debug=True)
