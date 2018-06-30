FROM python:3
MAINTAINER Tom Bescherer "tbescherer@gmail.com"
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["app.py"]
