```python
import tensorflow as tf

class BatchingCaching:
    def __init__(self, batch_size, buffer_size):
        self.batch_size = batch_size
        self.buffer_size = buffer_size

    def batch_and_cache(self, dataset):
        """
        This function takes a dataset, shuffles it and batches it.
        Caching is done to store the dataset in memory or in a file for faster access.
        """
        return dataset.shuffle(self.buffer_size).batch(self.batch_size).cache()

# Usage
# Assuming we have a dataset 'ds'
# batch_cache = BatchingCaching(batch_size=64, buffer_size=10000)
# ds = batch_cache.batch_and_cache(ds)
```