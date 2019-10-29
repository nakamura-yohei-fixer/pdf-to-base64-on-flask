from flask import Flask, jsonify, request
from io import BytesIO
import json
import base64
from pdf2image import convert_from_path
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "route get. Hello!"


@app.route("/pdf", methods=['GET'])
def pdf():
    images = convert_from_path('sample.pdf')
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


@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "route post. keyword is %s!\n" % data["keyword"]
    result = {
        "Content-Type": "application/json",
        "Answer": {"Text": answer}
    }
    # return answer
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
