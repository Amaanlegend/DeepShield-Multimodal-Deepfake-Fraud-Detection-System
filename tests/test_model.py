# test_model.py

import pytest
from tensorflow.keras.models import load_model
from src.model.cnn_lstm_model import build_cnn_lstm_model

def test_model_build():
    input_shape = (10, 64, 64, 3)  # Example input shape
    model = build_cnn_lstm_model(input_shape)
    
    assert model is not None
    assert len(model.layers) > 0

def test_model_prediction():
    model = load_model('deepfake_detection_model.h5')
    fake_input = np.random.rand(1, 10, 64, 64, 3)
    prediction = model.predict(fake_input)
    
    assert prediction.shape == (1, 1)
    assert 0 <= prediction[0][0] <= 1
