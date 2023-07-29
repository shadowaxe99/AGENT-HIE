```python
import tensorflow as tf
from tensorflow.keras import models
from src.ai_system.training.model_architecture import TransformerModel

class ArchitectureExplorer:
    def __init__(self, model: models.Model):
        self.model = model

    def explore_architecture(self):
        print(self.model.summary())

    def compare_with_transformer(self):
        transformer = TransformerModel()
        print("Current Model Architecture:")
        self.explore_architecture()
        print("\nTransformer Model Architecture:")
        transformer.explore_architecture()

    def modify_architecture(self, layers_to_add: list):
        for layer in layers_to_add:
            self.model.add(layer)
        print("Modified Model Architecture:")
        self.explore_architecture()

if __name__ == "__main__":
    model = tf.keras.models.Sequential()
    explorer = ArchitectureExplorer(model)
    explorer.compare_with_transformer()
    layers_to_add = [
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ]
    explorer.modify_architecture(layers_to_add)
```