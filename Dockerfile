FROM python:3.10-slim
WORKDIR /Desktop/py_app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
EXPOSE 8090
CMD ["python","app.py"]
