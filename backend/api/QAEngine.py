"""
    Single instance of fake detector
"""
import os
import numpy as np
import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

COS_NO_ANSWER_THRESHOLD = 0.6
COS_NOT_SURE_THRESHOLD = 0.75

class QAEngine():

  def __init__(self):
    # Load the data and models
    json_path = os.path.join(os.getcwd(), 'models', 'covid_kaggle_answer_from_qa.json')
    print('Loading QA json from path: ', json_path)
    
    origin_data=json.load(open(json_path))
    (question_list, answer_list) = self.reshapeData(origin_data)

    print('JSON data loaded successfully')
    print('Start loading model...')
    
    self.model = SentenceTransformer('bert-base-nli-mean-tokens')
    self.sen_embeddings = self.model.encode(question_list)
    self.question_list = question_list
    self.answer_list = answer_list

    print('All data prepared')

    pass

  def reshapeData (self, origin_json):
    question_list = []
    answer_list = []
    
    for doc in origin_json['data']:
        for question in doc['questions']:
            question_list.append(question['question'])
            answer_list.append(question['results'][0]['context'])

    return question_list, answer_list
  
  def predict (self, question):
    embedded = self.model.encode([question])
    
    cos_list = cosine_similarity(
      embedded,
      self.sen_embeddings)
    cos_list = cos_list[0]
    
    max_cos = np.where(cos_list==np.max(cos_list))

    index = max_cos[0][0]
    cos_value = cos_list[index]
    
    if cos_value < COS_NO_ANSWER_THRESHOLD:
        ans = "Sorry. I don't known the answer."
    elif cos_value < COS_NOT_SURE_THRESHOLD:
        ans = "Sorry. I don't understand. Are you asking '{}'".format(self.question_list[index])
    else:
        ans = self.answer_list[index]    
    
    return ans


qa_engine = QAEngine()