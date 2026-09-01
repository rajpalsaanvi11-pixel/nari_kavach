from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import io

from full_cloak import cloak_face  # importing your function, not rewriting it

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "Server is running!"


@app.route('/cloak', methods=['POST'])
def cloak_endpoint():
    if 'photo' not in request.files:
        return {"error": "No photo uploaded."}, 400

    file = request.files['photo']
    img = Image.open(file.stream).convert('RGB')

    result_img = cloak_face(img)

    if result_img is None:
        return {"error": "No face detected in the photo."}, 400

    img_bytes = io.BytesIO()
    result_img.save(img_bytes, format='JPEG', quality=95)
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True, port=5000)