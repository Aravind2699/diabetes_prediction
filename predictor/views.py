from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import DiabetesPredictionForm
from .models import PredictionHistory
from .ml_models import predict_diabetes, train_models, get_model_metrics

# Train models on startup
train_models()

class HomeView(View):
    """Home page with prediction form"""
    def get(self, request):
        form = DiabetesPredictionForm()
        recent_predictions = PredictionHistory.objects.all()[:10]
        return render(request, 'home.html', {
            'form': form,
            'recent_predictions': recent_predictions
        })
    
    def post(self, request):
        form = DiabetesPredictionForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            input_data = [
                form.cleaned_data['pregnancies'],
                form.cleaned_data['glucose'],
                form.cleaned_data['blood_pressure'],
                form.cleaned_data['skin_thickness'],
                form.cleaned_data['insulin'],
                form.cleaned_data['bmi'],
                form.cleaned_data['diabetes_pedigree_function'],
                form.cleaned_data['age'],
            ]
            
            # Get predictions
            result = predict_diabetes(input_data)
            
            if 'error' not in result:
                # Save to history
                prediction = PredictionHistory.objects.create(
                    pregnancies=form.cleaned_data['pregnancies'],
                    glucose=form.cleaned_data['glucose'],
                    blood_pressure=form.cleaned_data['blood_pressure'],
                    skin_thickness=form.cleaned_data['skin_thickness'],
                    insulin=form.cleaned_data['insulin'],
                    bmi=form.cleaned_data['bmi'],
                    diabetes_pedigree_function=form.cleaned_data['diabetes_pedigree_function'],
                    age=form.cleaned_data['age'],
                    prediction_lr=result['lr_prediction'],
                    prediction_rf=result['rf_prediction'],
                    confidence_lr=result['lr_confidence'],
                    confidence_rf=result['rf_confidence']
                )
                
                return render(request, 'result.html', {
                    'result': result,
                    'input_data': form.cleaned_data,
                    'prediction': prediction
                })
            else:
                messages.error(request, f"Error: {result['error']}")
                return redirect('home')
        
        recent_predictions = PredictionHistory.objects.all()[:10]
        return render(request, 'home.html', {
            'form': form,
            'recent_predictions': recent_predictions
        })

def result_view(request):
    """View for prediction result"""
    return render(request, 'result.html')

def history_view(request):
    """View prediction history"""
    predictions = PredictionHistory.objects.all()
    return render(request, 'history.html', {
        'predictions': predictions
    })

def about_view(request):
    """About page"""
    return render(request, 'about.html')

def analytics_view(request):
    """Analytics and model comparison dashboard"""
    metrics = get_model_metrics()
    
    # Calculate percentages
    total_samples = metrics['dataset']['total_samples']
    negative_percentage = round((metrics['dataset']['negative_class'] / total_samples) * 100, 1)
    positive_percentage = round((metrics['dataset']['positive_class'] / total_samples) * 100, 1)
    
    # Prepare comparison data
    comparison_data = {
        'models': ['Logistic Regression', 'Random Forest'],
        'accuracy': [metrics['logistic_regression']['accuracy'], metrics['random_forest']['accuracy']],
        'precision': [metrics['logistic_regression']['precision'], metrics['random_forest']['precision']],
        'recall': [metrics['logistic_regression']['recall'], metrics['random_forest']['recall']],
        'f1_score': [metrics['logistic_regression']['f1_score'], metrics['random_forest']['f1_score']],
        'roc_auc': [metrics['logistic_regression']['roc_auc'], metrics['random_forest']['roc_auc']],
    }
    
    context = {
        'metrics': metrics,
        'comparison': comparison_data,
        'negative_percentage': negative_percentage,
        'positive_percentage': positive_percentage,
        'feature_explanations': {
            'Pregnancies': 'Number of times pregnant',
            'Glucose': 'Plasma glucose concentration (fasting)',
            'BloodPressure': 'Diastolic blood pressure (mmHg)',
            'SkinThickness': 'Triceps skin fold thickness (mm)',
            'Insulin': '2-Hour serum insulin (mu U/ml)',
            'BMI': 'Body mass index (weight in kg/(height in m)^2)',
            'DiabetesPedigreeFunction': 'Diabetes pedigree function (family history)',
            'Age': 'Age in years'
        },
        'metric_explanations': {
            'accuracy': 'Proportion of correct predictions among all predictions',
            'precision': 'Proportion of diabetic predictions that were correct',
            'recall': 'Proportion of actual diabetic cases that were correctly identified',
            'f1_score': 'Harmonic mean of precision and recall',
            'roc_auc': 'Area under the ROC curve (0.5 = random, 1.0 = perfect)'
        }
    }
    
    return render(request, 'analytics.html', context)
