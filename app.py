from flask import Flask, request, redirect, render_template, jsonify, flash, url_for, abort, \
    send_from_directory 
# from views import *
# from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename
import os 
import imghdr


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static/uploads'

# app.register_blueprint(views, url_prefix="/")


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/profile")
def profile() :
    return render_template("index.html")

@app.route("/")
def login() :
    return render_template("login.html")

@app.route("/bookappointment")
def bookappointment() :
    return render_template("bookappointment.html")

@app.route("/videocall") 
def videocall() :
    return render_template("videocall.html")

@app.route("/scan")
def scan() :
    return render_template("scan.html")

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

####Image upload
def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/uploadimagescan')
def uploadimagescan():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('uploadimagescan.html', files=files)

@app.route('/uploadimagescan', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('uploadimagescan'))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == '__main__' :
    app.run(debug=True, port=8000)