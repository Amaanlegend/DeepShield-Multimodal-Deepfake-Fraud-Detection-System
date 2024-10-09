# evaluate_model.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(y_true, y_pred):
    """
    Evaluate the model using accuracy, precision, recall, and F1-score.
    
    Parameters:
    y_true (array): True labels.
    y_pred (array): Predicted labels.
    
    Returns:
    dict: Evaluation metrics (accuracy, precision, recall, F1).
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
