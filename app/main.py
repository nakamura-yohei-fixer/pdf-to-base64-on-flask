from flask import Flask, jsonify, request
from io import BytesIO
import json
import base64
from pdf2image import convert_from_bytes
app = Flask(__name__)


# File => PNG Image => Base64
# @app.route("/pdf", methods=['POST'])
# def pdf():
#     pdf = request.files["file"]
#     images = convert_from_bytes(pdf.read())
#     base64_list = []
#     for image in images:
#         buffer = BytesIO()
#         image.save(buffer, format="PNG")
#         base64Img = base64.b64encode(
#             buffer.getvalue()).decode().replace("'", "")
#         base64_list.append(base64Img)
#     result = {
#         "Content-Type": "application/json",
#         "Base64Images": base64_list
#     }
#     return jsonify(result)


# Base64(PDF) => File => PNG Image => Base64
@app.route("/pdf", methods=["POST"])
def pdf():
    request_data = json.loads(request.data)
    pdf = base64.b64decode(request_data["pdf"])
    images = convert_from_bytes(pdf)
    base64_list = []
    for image in images:
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        base64Img = base64.b64encode(
            buffer.getvalue()).decode().replace("'", "")
        base64_list.append(base64Img)
    result = {
        "Content-Type": "application/json",
        "Base64Images": base64_list
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
