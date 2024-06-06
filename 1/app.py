from flask import Flask, render_template
import flask

# Init Flask server obj
## Address __name__ đến file hiện tại nơi chứa server
app = Flask(__name__)


@app.route("/")
def index():
    # Hàm python giúp render và return file HTML
    ## Hàm biết tự động tìm đến folder templates
    return render_template("index.html")


@app.route("/file.txt")
def response_file():
    # Response to client a file located in a directory
    return flask.send_from_directory("document", "file.txt")


if __name__ == "__main__":
    # Khởi động server, bật debug mode (nếu có lỗi sẽ popup lên màn hình)
    app.run(debug=True)
