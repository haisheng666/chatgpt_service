from flask import Flask, request

app = Flask(__name__)


@app.route("/read_asset", methods=["POST"])
def read_asset():
    # 获取普通参数
    print(f"request.values: {request.values}")
    print(f"request.values.get('name''): {request.values.get('name')}")

    # 获取文件类型的参数
    print(f"request.files: {request.files}")
    print(f"request.files.get('file_name'): {request.files.get('file_name')}")
    # 获取上传文件的二进制流
    print(f"request.files.get('file_name').read(): {request.files.get('file_name').read()}")
    return "got"


if __name__ == '__main__':
    app.run()
