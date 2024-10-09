# train_model.py

import tensorflow as tf
from model.cnn_lstm_model import build_cnn_lstm_model
from src.data.load_data import load_train_data

def train_model():
    """
    Train the CNN + LSTM model on deepfake dataset.
    
    Returns:
    history: Model training history.
    """
    X_train, y_train, X_val, y_val = load_train_data()
    input_shape = X_train.shape
    
    model = build_cnn_lstm_model(input_shape)
    
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
    model.save('deepfake_detection_model.h5')
    
    return history
