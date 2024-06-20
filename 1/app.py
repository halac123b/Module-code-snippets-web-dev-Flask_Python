from flask import Flask, render_template
import flask

# Init Flask server obj
## Address __name__ đến file hiện tại nơi chứa server
app = Flask(__name__)

# Config cho server app
## TESTING là 1 built-in config: nếu bật các exception sẽ đc throw ngay chứ k đc handle. giúp dễ phát hiện hơn
## Ngoài ra có thể config các giá trị custom khác
app.config["TESTING"] = True


@app.route("/")
# Các hàm bên dưới decorator này là hàm view
## Value return từ hàm này chính là nội dung phần view đc render bên phía browser
def index():
    # Hàm python giúp render và return file HTML
    ## Hàm biết tự động tìm đến folder templates
    return render_template("index.html")


@app.route("/file.txt")
def response_text():
    # Response to client a file located in a directory
    return flask.send_from_directory("document", "file.txt")


# <path:filename>: url pattern, cho phép chứa biến đc dùng làm arg cho hàm view
## path: data type (cũng là string, nhưng cho phép chứa slash)
## filename: tên biến, cũng là arg trong hàm view
@app.route("/download/<path:filename>")
def response_file(filename):
    # Response to client a file located in a directory
    return flask.send_from_directory("document", filename)


@app.route("/responseJson")
def response_file():
    respone = {"str1": "conga", "str2": "convit"}
    # Return a dictionary as JSON
    return flask.jsonify(respone)


if __name__ == "__main__":
    # Khởi động server, bật debug mode (nếu có lỗi sẽ popup lên màn hình)
    app.run(debug=True)
