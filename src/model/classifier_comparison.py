# classifier_comparison.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from model.evaluate_model import evaluate_model

def compare_classifiers(X_train, y_train, X_test, y_test):
    """
    Compare CNN + LSTM model with traditional classifiers (Random Forest, SVM).
    
    Parameters:
    X_train (array): Training data.
    y_train (array): Training labels.
    X_test (array): Test data.
    y_test (array): Test labels.
    
    Returns:
    dict: Comparison results for each classifier.
    """
    results = {}
    
    # Random Forest Classifier
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    results['RandomForest'] = evaluate_model(y_test, y_pred_rf)
    
    # SVM Classifier
    svm = SVC()
    svm.fit(X_train, y_train)
    y_pred_svm = svm.predict(X_test)
    results['SVM'] = evaluate_model(y_test, y_pred_svm)
    
    return results
