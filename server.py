from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)
#To set up the server run the following commands in the terminal (make sure you are on the folder that contains the server.py file):
#set FLASK_APP=server.py (no spaces around the Equal sign)
#set FLASK_ENV=development (no spaces around the Equal sign)
#flask run

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:html>')
def link(html):
    return render_template(html)



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'something went wrong. Try again!'


def write_to_file(data):
    with open('database.txt', 'a') as editor:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        editor.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as editor2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(editor2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])