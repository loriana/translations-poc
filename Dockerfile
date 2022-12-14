FROM python:3.8


RUN pip install flask

COPY app.py /app.py

EXPOSE 5000

CMD ["python", "/app.py"]
