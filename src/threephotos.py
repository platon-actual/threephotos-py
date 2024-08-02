# Ramiro Iván Ríos (2024)

from flask import Flask, request, render_template, url_for
import os

IMAGES_FOLDER = 'static/downloads/images/'

app = Flask(__name__)

@app.route('/')
def show_images():
    return render_template('index.html', image='la_imagen.jpg')

@app.route('/post_image', methods=['POST'])
def upload_image():
    file = request.files['image']
    #uploaded_image =
    file.save(os.path.join(app.root_path, IMAGES_FOLDER + "la_imagen.jpg"))
    return url_for('show_images')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)