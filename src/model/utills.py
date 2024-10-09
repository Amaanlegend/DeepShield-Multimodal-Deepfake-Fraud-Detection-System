import numpy as np
from sklearn.utils import shuffle
import cv2
import random

def data_augmentation(images):
    """
    Augments the dataset by applying random transformations to images.
    
    Args:
        images (list): List of images to augment.

    Returns:
        augmented_images (list): List of augmented images.
    """
    augmented_images = []
    for img in images:
        # Randomly flip the image horizontally
        if random.random() > 0.5:
            img = cv2.flip(img, 1)

        # Randomly adjust brightness
        brightness = random.uniform(0.5, 1.5)
        img = cv2.convertScaleAbs(img, alpha=brightness, beta=0)

        # Randomly rotate the image
        angle = random.randint(-15, 15)
        M = cv2.getRotationMatrix2D((img.shape[1] // 2, img.shape[0] // 2), angle, 1)
        img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

        augmented_images.append(img)
    
    return augmented_images

def shuffle_data(X, y):
    """
    Shuffle the dataset.

    Args:
        X (np.array): Feature data.
        y (np.array): Labels.

    Returns:
        tuple: Shuffled feature data and labels.
    """
    X, y = shuffle(X, y)
    return X, y
