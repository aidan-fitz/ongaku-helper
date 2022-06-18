from flask import Flask, request

from furigana import to_html, to_plaintext

app = Flask(__name__)


@app.route("/furigana", methods=["POST"])
def get_furigana():
    # For simplicity, get the entire request body as a string
    request_body = request.data.decode(
        request.mimetype_params.get("charset", "utf-8")
    )
    # Generate furigana in the format requested by the client
    # (HTML if possible, plaintext otherwise)
    if request.accept_mimetypes.accept_html:
        return to_html(request_body)
    else:
        return to_plaintext(request_body)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
