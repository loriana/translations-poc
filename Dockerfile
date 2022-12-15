FROM python:3.8

RUN pip3 install -r requirements.txt

COPY app.py /app.py

EXPOSE 5000

CMD ["python", "/app.py"]
