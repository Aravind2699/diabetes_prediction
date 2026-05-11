# 🏥 Diabetes Predictor

A professional Django web application for **early diabetes prediction** using advanced machine learning algorithms (Logistic Regression & Random Forest).

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](LICENSE)

---

## ✨ Features

### 🎯 Core Features
- **Dual ML Models**: Logistic Regression & Random Forest comparison
- **Real-time Predictions**: Instant diabetes risk assessment
- **Confidence Scores**: Probability-based confidence levels (0-100%)
- **Model Comparison**: Side-by-side performance metrics
- **Prediction History**: Track all previous predictions
- **Analytics Dashboard**: Comprehensive metrics and analysis

### 📊 Advanced Analytics
- Performance metrics (Accuracy, Precision, Recall, F1-Score, ROC-AUC)
- Confusion matrices for both models
- Dataset statistics and class distribution
- Feature importance explanations
- Model recommendations

### 🎨 User Interface
- Modern responsive design with Bootstrap 5
- Gradient backgrounds and smooth animations
- Color-coded predictions (Green ✅ / Red ⚠️)
- Mobile-friendly layout
- Professional dashboard

### 💾 Data Management
- SQLite database for prediction history
- Django ORM for data handling
- Admin panel for data management
- Automatic model training on startup

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation (5 minutes)

```bash
# 1. Navigate to project directory
cd diabetes_predictor

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
```

### Access the Application
Open your browser and visit: **http://localhost:8000/**

---

## 📖 Usage Guide

### 1. **Home Page** - Make Predictions
- Enter 8 health metrics:
  - Pregnancies
  - Glucose level (mg/dL)
  - Blood pressure (mmHg)
  - Skin thickness (mm)
  - Insulin level (mu U/ml)
  - BMI (Body Mass Index)
  - Diabetes pedigree function
  - Age (years)
- Click "🚀 Predict Diabetes Risk"
- View predictions from both ML models with confidence scores

### 2. **Analytics** - Model Comparison
- View dataset statistics (768 samples, 8 features)
- Compare model performance metrics
- See confusion matrices
- Understand feature explanations
- Read metrics interpretation guide
- Get model selection recommendations

### 3. **History** - Track Predictions
- View all previous predictions in a table
- Sort by date, age, glucose, BMI
- See predictions from both models
- Track confidence scores over time

### 4. **About** - Project Information
- Learn about the models
- Understand the dataset (Pima Indians Diabetes Dataset)
- Review technology stack
- Read important disclaimers

---

## 🤖 Machine Learning Models

### Logistic Regression
- **Type**: Linear classification algorithm
- **Speed**: Fast ⚡
- **Interpretability**: High 🔍
- **Accuracy**: ~67.5%
- **Best for**: Interpretable predictions, speed-critical applications

### Random Forest
- **Type**: Ensemble learning (100 decision trees)
- **Speed**: Moderate 🔄
- **Interpretability**: Medium 🔍
- **Accuracy**: ~70.1%
- **Best for**: Better accuracy, complex pattern detection

---

## 📊 Performance Metrics

| Metric | Logistic Regression | Random Forest |
|--------|-------------------|----------------|
| **Accuracy** | 0.6753 | 0.7013 |
| **Precision** | 0.6667 | 0.625 |
| **Recall** | 0.6182 | 0.6364 |
| **F1-Score** | 0.6415 | 0.6306 |
| **ROC-AUC** | 0.8228 | 0.8341 |

---

## 📁 Project Structure

```
diabetes_predictor/
├── diabetes_predictor/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── predictor/                   # Main app
│   ├── models.py               # PredictionHistory model
│   ├── views.py                # View logic
│   ├── forms.py                # Django forms
│   ├── ml_models.py            # ML training & prediction
│   ├── urls.py
│   ├── admin.py
│   ├── templates/              # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── analytics.html
│   │   ├── history.html
│   │   ├── result.html
│   │   └── about.html
│   └── migrations/             # Database migrations
├── manage.py
├── requirements.txt
├── db.sqlite3
├── INSTALL.md                  # Installation guide
└── README.md                   # This file
```

---

## 🔧 Technology Stack

### Backend
- **Django 4.2.13** - Web framework
- **Python 3.8+** - Programming language

### Machine Learning
- **Scikit-learn** - ML algorithms
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing

### Visualization
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical plots

### Frontend
- **Bootstrap 5** - Responsive framework
- **HTML5** - Markup
- **CSS3** - Styling
- **JavaScript** - Interactivity

### Database
- **SQLite** - Database (development)
- **PostgreSQL** - Recommended for production

---

## 📋 Requirements

See `requirements.txt` for all dependencies:

```
Django==4.2.13
pandas
numpy
scikit-learn
matplotlib
seaborn
requests
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🔐 Security & Best Practices

### Development
- ✅ SQLite database
- ✅ DEBUG mode ON
- ✅ Local development only

### Production Deployment
- 🔒 Change SECRET_KEY
- 🔒 Set DEBUG=False
- 🔒 Use PostgreSQL
- 🔒 Enable HTTPS
- 🔒 Use gunicorn/uWSGI
- 🔒 Configure allowed hosts
- 🔒 Use environment variables

---

## 📚 Detailed Documentation

- **[Installation Guide](INSTALL.md)** - Complete setup instructions
- **[Django Docs](https://docs.djangoproject.com/)** - Framework documentation
- **[Scikit-learn Docs](https://scikit-learn.org/)** - ML library documentation

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: "ModuleNotFoundError: No module named 'django'"
```bash
# Solution: Ensure venv is activated and pip install is run
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

**Issue**: "Address already in use" on port 8000
```bash
# Solution: Use different port
python manage.py runserver 8001
```

**Issue**: Static files not loading
```bash
# Solution: Collect static files
python manage.py collectstatic
```

See [INSTALL.md](INSTALL.md) for more troubleshooting steps.

---

## 🎓 Educational Dataset

**Pima Indians Diabetes Dataset**
- **Samples**: 768 instances
- **Features**: 8 medical attributes
- **Classes**: Binary (Diabetic/Non-Diabetic)
- **Positive Class**: 268 samples (34.9%)
- **Negative Class**: 500 samples (65.1%)

**Features:**
1. Pregnancies - Number of pregnancies
2. Glucose - Plasma glucose concentration
3. BloodPressure - Diastolic blood pressure
4. SkinThickness - Triceps skin fold thickness
5. Insulin - 2-Hour serum insulin
6. BMI - Body mass index
7. DiabetesPedigreeFunction - Family history
8. Age - Age in years

---

## 📊 Model Training

Models are automatically trained on server startup using:
1. Data loading from online source
2. Missing value imputation
3. Feature scaling (StandardScaler)
4. Train-test split (80-20)
5. Model fitting on training data
6. Metrics calculation on test data

---

## 🎯 Use Cases

- 🏥 Hospital diabetes screening systems
- 💊 Healthcare provider applications
- 📱 Medical mobile apps
- 🎓 Educational ML demonstrations
- 📊 Data science projects
- 🔬 Healthcare analytics

---

## ⚠️ Important Disclaimer

**This application is for educational and informational purposes only.**

This tool should **NOT** be used as a substitute for:
- Professional medical advice
- Clinical diagnosis
- Medical treatment decisions
- Healthcare provider consultations

**Always consult with a qualified healthcare professional for medical concerns.**

---

## 📈 Performance Notes

- **Model Training Time**: ~2-3 seconds (first load)
- **Prediction Time**: <100ms
- **Database**: SQLite (development only)
- **Memory Usage**: ~200MB for ML models
- **Max Concurrent Users**: Depends on deployment

---

## 🔄 Future Enhancements

- [ ] User authentication system
- [ ] Export predictions to PDF/CSV
- [ ] REST API endpoints
- [ ] Advanced visualizations
- [ ] Cross-validation metrics
- [ ] Hyperparameter tuning UI
- [ ] Multiple datasets support
- [ ] Real-time model retraining
- [ ] Mobile app version
- [ ] Cloud deployment ready

---

## 📞 Support

For issues or questions:
1. Check [INSTALL.md](INSTALL.md) troubleshooting section
2. Review error messages in terminal
3. Check Django logs
4. Visit [Django documentation](https://docs.djangoproject.com/)

---

## 📄 License

This project is provided for educational purposes.

---

## 👨‍💻 Development

### Made with ❤️ using
- Python & Django
- Machine Learning (Scikit-learn)
- Modern Web Technologies

---

## 🎉 Credits

- **Dataset**: Pima Indians Diabetes Database
- **Framework**: Django
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Frontend**: Bootstrap 5

---

**Status**: ✅ Production Ready (with proper configuration)  
**Last Updated**: May 11, 2026  
**Version**: 1.0.0

---

### 📱 Access Points

| Page | URL | Purpose |
|------|-----|---------|
| Home | `/` | Make predictions |
| Analytics | `/analytics/` | View model comparison |
| History | `/history/` | View prediction history |
| About | `/about/` | Project information |
| Admin | `/admin/` | Database management |

---

**Start predicting diabetes risk today! 🚀**

For detailed installation instructions, see [INSTALL.md](INSTALL.md)
