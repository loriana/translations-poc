FROM python:3.8

RUN pip install sentence_transformers sklearn.metrics.pairwise numpy pandas

COPY app.py /app.py

EXPOSE 5000

CMD ["python", "/app.py"]
