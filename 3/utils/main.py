import werkzeug.utils

filename = "file name.txt"
# Output phiên bản an toàn của 1 file name
## Chỉ chứa các kí tự ASCII, tránh các lỗi trong file path
filename = werkzeug.utils.secure_filename(filename)
# out: file_name.txt
