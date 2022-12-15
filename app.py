from flask import Flask, request
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
def rank_suggestions(suggestions, en_original):
    model = SentenceTransformer('distiluse-base-multilingual-cased-v1')
    embedded_en = model.encode(en_original).reshape(1,-1)
    embedded_suggestions = [model.encode(s).reshape(1, -1) for s in suggestions]
    def cos_sim(a, b):
        return np.round(cosine_similarity(a, b)[0][0], 4)
    suggestions_scores = [cos_sim(embedded_en, e_s) for e_s in embedded_suggestions]
    sug_sim_df = pd.DataFrame({"suggestion":suggestions, "sim_to_english":suggestions_scores}).sort_values(by="sim_to_english", ascending=False).reset_index(drop=True)
    return sug_sim_df.to_dict()

# Create a Flask app
app = Flask(__name__)

@app.route('/translations', methods=['GET'])
def handle_suggestions():
  body = request.get_json()
  suggestions = body['suggestions']
  en_original = body['en_original']
  return rank_suggestions(suggestions, en_original)

# Run the app
if __name__ == '__main__':
  app.run()