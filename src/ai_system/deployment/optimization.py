```python
import tensorflow as tf

def optimize_for_latency(model):
    """
    Function to optimize the model for latency.
    """
    # Convert the model to a TensorFlow Lite model.
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_LATENCY]
    
    # Convert the model
    tflite_model = converter.convert()
    
    return tflite_model

def save_optimized_model(tflite_model, filename):
    """
    Function to save the optimized model.
    """
    with open(filename, 'wb') as f:
        f.write(tflite_model)
```
