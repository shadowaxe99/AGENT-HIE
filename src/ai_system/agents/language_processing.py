```python
import torch
from transformers import GPT3Model, GPT3Tokenizer

class LanguageProcessingAgent:
    def __init__(self, model_name='gpt-3', device='cuda'):
        self.tokenizer = GPT3Tokenizer.from_pretrained(model_name)
        self.model = GPT3Model.from_pretrained(model_name).to(device)
        self.device = device

    def process(self, text):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        outputs = self.model(**inputs)
        return outputs

    def generate_response(self, text):
        processed = self.process(text)
        response = self.tokenizer.decode(processed, skip_special_tokens=True)
        return response
```
