```python
import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split

class DataCollector:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self, filename):
        with open(os.path.join(self.data_dir, filename), 'r') as file:
            data = json.load(file)
        return data

    def split_data(self, data, test_size=0.2, random_state=42):
        train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
        return train_data, test_data

    def save_data(self, data, filename):
        with open(os.path.join(self.data_dir, filename), 'w') as file:
            json.dump(data, file)

    def collect_data(self):
        # Load conversational datasets
        conversation_data = self.load_data('conversations.json')

        # Load positive and negative response examples
        positive_responses = self.load_data('positive_responses.json')
        negative_responses = self.load_data('negative_responses.json')

        # Load common use cases and real user transcripts
        use_cases = self.load_data('use_cases.json')
        user_transcripts = self.load_data('user_transcripts.json')

        # Combine all data
        all_data = conversation_data + positive_responses + negative_responses + use_cases + user_transcripts

        # Split data into training and testing sets
        train_data, test_data = self.split_data(all_data)

        # Save training and testing data
        self.save_data(train_data, 'train_data.json')
        self.save_data(test_data, 'test_data.json')

if __name__ == "__main__":
    data_collector = DataCollector('data')
    data_collector.collect_data()
```