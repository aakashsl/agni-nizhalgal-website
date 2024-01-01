from flask import Flask, render_template,request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404 

bot_token = 'xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxx' #your Telegram Bot Code
chat_ids =['xxxxxxxxxx','xxxxxxxxx','xxxxxxxxx'] #your telegram chat ID

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    telegram_message = f'Name : {name} \n Email : {email} \n Message : {message}'
    for chat_id in chat_ids:
            requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage',
                        data={'chat_id': chat_id, 'text': telegram_message})
    return redirect("/") 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')