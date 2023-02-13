from flask import Flask, render_template,request
import qrcode

from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process_input", methods=["POST"])
def qr():
    data = request.get_json()["input"]

    img = qrcode.make(data)
    img.save("static/qr.png")

    return render_template("index.html")
    


if __name__ == '__main__':
    app.run(debug=True)
  