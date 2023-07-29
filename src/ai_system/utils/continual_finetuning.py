```python
import torch
from torch.optim import Adam
from src.ai_system.training.model_architecture import TransformerModel

class ContinualFineTuning:
    def __init__(self, model, learning_rate=0.001):
        self.model = model
        self.optimizer = Adam(self.model.parameters(), lr=learning_rate)

    def fine_tune(self, data_loader):
        self.model.train()
        total_loss = 0
        for batch in data_loader:
            inputs, targets = batch
            self.optimizer.zero_grad()
            outputs = self.model(inputs)
            loss = self.calculate_loss(outputs, targets)
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item()
        return total_loss / len(data_loader)

    @staticmethod
    def calculate_loss(outputs, targets):
        return torch.nn.functional.cross_entropy(outputs, targets)

if __name__ == "__main__":
    model = TransformerModel()
    fine_tuner = ContinualFineTuning(model)
    # Assume data_loader is defined and provides the training data
    loss = fine_tuner.fine_tune(data_loader)
    print(f"Training loss: {loss}")
```