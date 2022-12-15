from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask
from flask import request
import numpy as np
import pandas as pd

model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

#this is a list of suggestions that should come with the req
suggestions = ["¿Qué sucede cuando aplicamos <code>display: flex;</code> para los elementos de bloque?",
    "¿Qué sucede cuando aplicamos <code>display: flex;</code> para bloquear elementos?",
    "¿Qué sucede cuando aplicamos <code>display: flex;</code> para joder elementos?",
    "¿Qué sucede cuando aplicamos <code>display: flex;</code> para elementos bloqueados?"]
# the original that should come with the request
en_original = "Where does the <code>display: flex;</code> property go?"

embedded_en = model.encode(en_original).reshape(1,-1)
embedded_suggestions = [model.encode(s).reshape(1, -1) for s in suggestions]


def cos_sim(a, b):
    return np.round(cosine_similarity(a, b)[0][0], 4)

suggestions_scores_1 = [cos_sim(embedded_en, e_s) for e_s in embedded_suggestions]

sug_sim_df = pd.DataFrame({'suggestion':suggestions, 'sim_to_english':suggestions_scores_1}).sort_values(by='sim_to_english', ascending=False).reset_index(drop=True)
# this is what you should return
sug_sim_df

@app.route('/translations', methods=['GET'])
def rank_suggestions(function_name: str):
    data = request.json
    print(data)
    # return function_to_call(body)