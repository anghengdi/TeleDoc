from flask import Blueprint, render_template, request, url_for
import os

views = Blueprint(__name__, "views")

# @views.route("/home")
# def home():
#     return render_template("home.html")

# @views.route("/profile")
# def profile() :
#     return render_template("index.html")

# @views.route("/")
# def login() :
#     return render_template("login.html")

# @views.route("/bookappointment")
# def bookappointment() :
#     return render_template("bookappointment.html")

# @views.route("/videocall") 
# def videocall() :
#     return render_template("videocall.html")

# @views.route("/scan")
# def scan() :
#     return render_template("scan.html")

# ####Image upload
# def validate_image(stream):
#     header = stream.read(512)  # 512 bytes should be enough for a header check
#     stream.seek(0)  # reset stream pointer
#     format = imghdr.what(None, header)
#     if not format:
#         return None
#     return '.' + (format if format != 'jpeg' else 'jpg')

# @views.route('/uploadimagescan')
# def index():
#     files = os.listdir(app.config['UPLOAD_PATH'])
#     return render_template('uploadimagescan.html', files=files)

# @views.route('/uploadimagescan', methods=['POST'])
# def upload_files():
#     uploaded_file = request.files['file']
#     filename = secure_filename(uploaded_file.filename)
#     if filename != '':
#         file_ext = os.path.splitext(filename)[1]
#         if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
#                 file_ext != validate_image(uploaded_file.stream):
#             abort(400)
#         uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
#     return redirect(url_for('uploadimagescan'))

# @views.route('/uploads/<filename>')
# def upload(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)
###
# @views.route("/uploadimagescan")
# def uploadimagescan() :
#     return render_template("uploadimagescan.html")