```python
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class HumanEvaluation:
    def __init__(self, model, human_eval_data):
        self.model = model
        self.human_eval_data = human_eval_data

    def get_model_predictions(self):
        predictions = []
        for data in self.human_eval_data:
            prediction = self.model.predict(data['input'])
            predictions.append(prediction)
        return predictions

    def get_human_labels(self):
        return [data['label'] for data in self.human_eval_data]

    def evaluate(self):
        model_predictions = self.get_model_predictions()
        human_labels = self.get_human_labels()

        accuracy = accuracy_score(human_labels, model_predictions)
        precision = precision_score(human_labels, model_predictions, average='weighted')
        recall = recall_score(human_labels, model_predictions, average='weighted')
        f1 = f1_score(human_labels, model_predictions, average='weighted')

        return {
            'accuracy': np.round(accuracy, 3),
            'precision': np.round(precision, 3),
            'recall': np.round(recall, 3),
            'f1_score': np.round(f1, 3)
        }
```