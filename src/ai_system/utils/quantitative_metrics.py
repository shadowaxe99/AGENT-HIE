```python
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score

def calculate_precision(y_true, y_pred):
    """
    Function to calculate precision
    """
    return precision_score(y_true, y_pred, average='weighted')

def calculate_recall(y_true, y_pred):
    """
    Function to calculate recall
    """
    return recall_score(y_true, y_pred, average='weighted')

def calculate_f1(y_true, y_pred):
    """
    Function to calculate F1 score
    """
    return f1_score(y_true, y_pred, average='weighted')

def calculate_metrics(y_true, y_pred):
    """
    Function to calculate all metrics
    """
    precision = calculate_precision(y_true, y_pred)
    recall = calculate_recall(y_true, y_pred)
    f1 = calculate_f1(y_true, y_pred)

    return {"precision": precision, "recall": recall, "f1": f1}
```