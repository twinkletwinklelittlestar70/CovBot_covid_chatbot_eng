"""
    Single instance of fake detector
"""
import torch
from transformers import BertTokenizer
import os
import numpy as np

class FakeNewsEngine():

  def __init__(self):
    # Load the model
    model_path = os.path.join(os.getcwd(), 'models', 'fake_model')
    print('Loading fake news model from base path: ', model_path)
    self.model = torch.load(model_path, map_location='cpu')
    self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
    print('Model loaded successfully')
    pass

  def preprocess (self, text):
    token_text = self.tokenizer(list([text]), 
                          max_length = 128,           # Pad & truncate all sentences.
                          padding = 'max_length',
                          truncation=True,
                          return_attention_mask = True,   # Construct attn. masks.
                          return_tensors = 'pt'     # Return pytorch tensors.
    )
    seq = torch.tensor(token_text['input_ids']).to('cpu')
    mask = torch.tensor(token_text['attention_mask']).to('cpu')

    return seq, mask
  
  def predict (self, text):
    seq, mask = self.preprocess(text)
    with torch.no_grad():
      outputs = self.model(seq, mask)
      pred_proba = outputs[0].detach().cpu().numpy()
    
    preds = np.argmax(pred_proba, axis = 1)
    print('fake predict result', preds)
    
    return bool(preds[0])


fake_detector = FakeNewsEngine()