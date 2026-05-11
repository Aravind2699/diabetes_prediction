import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

# Global variables to store trained models
LR_MODEL = None
RF_MODEL = None
SCALER = None
MODELS_LOADED = False
X_TEST = None
Y_TEST = None
MODEL_METRICS = None

def train_models():
    """Train and cache the ML models"""
    global LR_MODEL, RF_MODEL, SCALER, MODELS_LOADED, X_TEST, Y_TEST, MODEL_METRICS
    
    if MODELS_LOADED:
        return
    
    try:
        # Load dataset
        url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
        df = pd.read_csv(url)
        
        # Replace invalid zeros with NaN
        cols_to_replace = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
        df[cols_to_replace] = df[cols_to_replace].replace(0, np.nan)
        
        # Fill missing values with median
        df.fillna(df.median(), inplace=True)
        
        # Features and target
        X = df.drop('Outcome', axis=1)
        y = df['Outcome']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Store test data for metrics
        X_TEST = X_test
        Y_TEST = y_test
        
        # Scale data
        SCALER = StandardScaler()
        X_train_scaled = SCALER.fit_transform(X_train)
        X_test_scaled = SCALER.transform(X_test)
        
        # Train Logistic Regression
        LR_MODEL = LogisticRegression(max_iter=1000)
        LR_MODEL.fit(X_train_scaled, y_train)
        
        # Train Random Forest
        RF_MODEL = RandomForestClassifier(n_estimators=100, random_state=42)
        RF_MODEL.fit(X_train_scaled, y_train)
        
        # Calculate metrics
        lr_pred = LR_MODEL.predict(X_test_scaled)
        rf_pred = RF_MODEL.predict(X_test_scaled)
        
        lr_proba = LR_MODEL.predict_proba(X_test_scaled)[:, 1]
        rf_proba = RF_MODEL.predict_proba(X_test_scaled)[:, 1]
        
        MODEL_METRICS = {
            'logistic_regression': {
                'accuracy': round(accuracy_score(y_test, lr_pred), 4),
                'precision': round(precision_score(y_test, lr_pred), 4),
                'recall': round(recall_score(y_test, lr_pred), 4),
                'f1_score': round(f1_score(y_test, lr_pred), 4),
                'roc_auc': round(roc_auc_score(y_test, lr_proba), 4),
                'confusion_matrix': confusion_matrix(y_test, lr_pred).tolist()
            },
            'random_forest': {
                'accuracy': round(accuracy_score(y_test, rf_pred), 4),
                'precision': round(precision_score(y_test, rf_pred), 4),
                'recall': round(recall_score(y_test, rf_pred), 4),
                'f1_score': round(f1_score(y_test, rf_pred), 4),
                'roc_auc': round(roc_auc_score(y_test, rf_proba), 4),
                'confusion_matrix': confusion_matrix(y_test, rf_pred).tolist()
            },
            'dataset': {
                'total_samples': len(df),
                'train_samples': len(X_train),
                'test_samples': len(X_test),
                'features': list(X.columns),
                'positive_class': int(y.sum()),
                'negative_class': int((y == 0).sum())
            }
        }
        
        MODELS_LOADED = True
        print("✅ Models trained successfully!")
        
    except Exception as e:
        print(f"❌ Error training models: {str(e)}")
        MODELS_LOADED = False

def predict_diabetes(input_data):
    """
    Predict diabetes using both models
    input_data: list of 8 features [Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                     Insulin, BMI, DiabetesPedigreeFunction, Age]
    Returns: dict with predictions from both models
    """
    global LR_MODEL, RF_MODEL, SCALER
    
    if not MODELS_LOADED or LR_MODEL is None or RF_MODEL is None or SCALER is None:
        train_models()
    
    try:
        # Convert to numpy array and reshape
        input_array = np.array(input_data).reshape(1, -1)
        
        # Scale using the trained scaler
        input_scaled = SCALER.transform(input_array)
        
        # Predict using Logistic Regression
        lr_pred = LR_MODEL.predict(input_scaled)[0]
        lr_proba = LR_MODEL.predict_proba(input_scaled)[0]
        lr_confidence = max(lr_proba) * 100
        
        # Predict using Random Forest
        rf_pred = RF_MODEL.predict(input_scaled)[0]
        rf_proba = RF_MODEL.predict_proba(input_scaled)[0]
        rf_confidence = max(rf_proba) * 100
        
        return {
            'lr_prediction': 'Diabetic ⚠️' if lr_pred == 1 else 'Not Diabetic ✅',
            'rf_prediction': 'Diabetic ⚠️' if rf_pred == 1 else 'Not Diabetic ✅',
            'lr_confidence': round(lr_confidence, 2),
            'rf_confidence': round(rf_confidence, 2),
            'lr_raw': int(lr_pred),
            'rf_raw': int(rf_pred)
        }
        
    except Exception as e:
        return {
            'error': str(e)
        }

def get_model_metrics():
    """Get detailed metrics for both models"""
    global MODEL_METRICS, MODELS_LOADED
    
    if not MODELS_LOADED:
        train_models()
    
    return MODEL_METRICS
