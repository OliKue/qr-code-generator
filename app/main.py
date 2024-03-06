from flask import Flask, send_file, jsonify
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/generate_qrcode/<data>')
def generate_qrcode(data):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an in-memory bytes stream to store the QR code image
    qr_img_stream = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_img_stream, 'PNG')
    qr_img_stream.seek(0)

    # Return the QR code image via REST
    return send_file(qr_img_stream, mimetype='image/png')


@app.route("/hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Hello from Flask"})


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=8080, debug=True)