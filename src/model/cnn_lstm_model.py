# cnn_lstm_model.py

import tensorflow as tf
from tensorflow.keras import layers, models

def build_cnn_lstm_model(input_shape):
    """
    Builds the CNN + LSTM model for deepfake detection.
    
    Parameters:
    input_shape (tuple): Shape of the input video frames (e.g., (sequence_length, height, width, channels)).
    
    Returns:
    model: Compiled CNN + LSTM model.
    """
    cnn_model = models.Sequential()
    
    # CNN for spatial features
    cnn_model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape[1:]))
    cnn_model.add(layers.MaxPooling2D((2, 2)))
    cnn_model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    cnn_model.add(layers.MaxPooling2D((2, 2)))
    cnn_model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    
    # Flatten and LSTM for temporal features
    cnn_model.add(layers.Flatten())
    cnn_model.add(layers.RepeatVector(input_shape[0]))  # Repeat for each time step
    cnn_model.add(layers.LSTM(128, return_sequences=False))
    
    # Output layer with softmax for binary classification
    cnn_model.add(layers.Dense(1, activation='sigmoid'))
    
    cnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return cnn_model
