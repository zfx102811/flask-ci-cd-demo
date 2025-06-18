FROM registry.cn-hangzhou.aliyuncs.com/dockerhub_library/python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
