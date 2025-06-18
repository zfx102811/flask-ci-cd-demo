from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Docker!"


# 关键在这里：Flask 启动服务
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
