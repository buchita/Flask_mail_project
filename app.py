from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bgitchamnan@gmail.com'
app.config['MAIL_PASSWORD'] = 'Yutaphong_123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    # dict = {'phy': 50, 'che': 60, 'maths': 70}
    # return render_template('main_page.html', result=dict)
    msg = Message('Hello', sender='bgitchamnan@gmail.com', recipients=['buchita.gitchamnan@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)
