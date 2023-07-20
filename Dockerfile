FROM python:3.8

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN python -c 'from sentence_transformers import SentenceTransformer; model = SentenceTransformer("distiluse-base-multilingual-cased-v1"); model.save("models")'

COPY . .

EXPOSE 5000

CMD ["python", "/app.py"]
