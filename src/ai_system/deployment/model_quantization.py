```python
import tensorflow as tf
from tensorflow import keras

def load_model(model_path):
    """
    Load the trained model from the specified path
    """
    model = keras.models.load_model(model_path)
    return model

def quantize_model(model):
    """
    Quantize the model to reduce its size and latency
    """
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    quantized_model = converter.convert()

    return quantized_model

def save_quantized_model(quantized_model, path):
    """
    Save the quantized model to the specified path
    """
    with open(path, 'wb') as f:
        f.write(quantized_model)

def model_quantization_pipeline(model_path, quantized_model_path):
    """
    Pipeline to load, quantize and save the model
    """
    model = load_model(model_path)
    quantized_model = quantize_model(model)
    save_quantized_model(quantized_model, quantized_model_path)

if __name__ == "__main__":
    model_path = "path_to_your_model.h5"
    quantized_model_path = "path_to_save_quantized_model.tflite"
    model_quantization_pipeline(model_path, quantized_model_path)
```