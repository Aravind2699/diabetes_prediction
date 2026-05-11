# 🏥 Diabetes Predictor - Installation Guide

A comprehensive Django web application for early diabetes prediction using Machine Learning (Logistic Regression & Random Forest).

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Configuration](#configuration)
4. [Running the Server](#running-the-server)
5. [Accessing the Application](#accessing-the-application)
6. [Project Structure](#project-structure)
7. [Troubleshooting](#troubleshooting)

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package manager) - Usually comes with Python
- **Git** (optional, for version control) - [Download Git](https://git-scm.com/)
- **Virtual Environment** - Built into Python 3.3+

### Check Installation

```bash
python --version
pip --version
```

---

## 🚀 Installation Steps

### Step 1: Clone or Download the Project

**Option A: Using Git**
```bash
git clone https://github.com/Aravind2699/diabetes_prediction.git
cd diabetes_predictor
```

**Option B: Download ZIP**
- Download the project as ZIP
- Extract to your desired location
- Navigate to the project directory

```bash
cd diabetes_predictor
```

### Step 2: Create a Virtual Environment

Creating a virtual environment isolates project dependencies:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt when activated.

### Step 3: Upgrade pip (Optional but Recommended)

```bash
pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected Output:**
```
Successfully installed Django-4.2.13 pandas numpy scikit-learn matplotlib seaborn requests
```

### Step 5: Apply Database Migrations

Initialize the SQLite database:

```bash
python manage.py migrate
```

**Expected Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, predictor
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
  Applying predictor.0001_initial... OK
```

### Step 6: Create a Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account:
```
Username: admin
Email: admin@example.com
Password: ••••••••
Password (again): ••••••••
```

---

## ⚙️ Configuration

### Django Settings

The main settings are located in `diabetes_predictor/settings.py`:

- **DEBUG**: Set to `True` for development, `False` for production
- **ALLOWED_HOSTS**: Add your domain/IP addresses
- **SECRET_KEY**: Change for production
- **DATABASES**: Configure database settings

### Environment Variables (Optional)

Create a `.env` file for sensitive settings:

```bash
# .env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## ▶️ Running the Server

### Start the Development Server

```bash
python manage.py runserver
```

**Custom Host/Port:**
```bash
python manage.py runserver 0.0.0.0:8000
```

**Expected Output:**
```
✅ Models trained successfully!
System check identified no issues (0 silenced).
May 11, 2026 - 21:47:02
Django version 4.2.13, using settings 'diabetes_predictor.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Stop the Server

Press `CTRL+C` (or `CTRL+BREAK` on Windows) in the terminal.

---

## 🌐 Accessing the Application

Once the server is running, access the application at:

### Main URLs

| Page | URL | Description |
|------|-----|-------------|
| **Home** | http://localhost:8000/ | Prediction form & recent predictions |
| **Analytics** | http://localhost:8000/analytics/ | Model comparison & metrics dashboard |
| **History** | http://localhost:8000/history/ | View all previous predictions |
| **About** | http://localhost:8000/about/ | Project information |
| **Admin Panel** | http://localhost:8000/admin/ | Django admin (if superuser created) |

### Default Credentials for Admin Panel
```
Username: admin (or your chosen username)
Password: Your superuser password
```

---

## 📁 Project Structure

```
diabetes_predictor/
│
├── diabetes_predictor/          # Main Django project settings
│   ├── settings.py              # Django configuration
│   ├── urls.py                  # URL routing
│   ├── wsgi.py                  # WSGI application
│   └── asgi.py                  # ASGI application
│
├── predictor/                   # Main Django app
│   ├── models.py                # Database models
│   ├── views.py                 # View logic
│   ├── urls.py                  # App URL patterns
│   ├── forms.py                 # Django forms
│   ├── admin.py                 # Admin configuration
│   ├── ml_models.py             # ML model functions
│   ├── apps.py                  # App configuration
│   │
│   ├── templates/               # HTML templates
│   │   ├── base.html            # Base template
│   │   ├── home.html            # Home page
│   │   ├── analytics.html       # Analytics dashboard
│   │   ├── history.html         # Prediction history
│   │   ├── result.html          # Prediction result
│   │   └── about.html           # About page
│   │
│   ├── static/                  # Static files (CSS, JS)
│   │
│   └── migrations/              # Database migrations
│       └── 0001_initial.py
│
├── manage.py                    # Django management script
├── requirements.txt             # Project dependencies
├── db.sqlite3                   # SQLite database
└── README.md                    # Project documentation
```

---

## 📦 Dependencies

### Core Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| Django | 4.2.13 | Web framework |
| pandas | Latest | Data manipulation |
| numpy | Latest | Numerical computing |
| scikit-learn | Latest | Machine learning |
| matplotlib | Latest | Data visualization |
| seaborn | Latest | Statistical visualization |
| requests | Latest | HTTP requests |

### Installation
All dependencies are listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
# Activate virtual environment
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Issue: "Address already in use" on port 8000

**Solution:** Use a different port:
```bash
python manage.py runserver 8001
```

### Issue: Database errors or migration issues

**Solution:** Reset the database:
```bash
# Delete db.sqlite3 file (all data will be lost)
rm db.sqlite3  # macOS/Linux
del db.sqlite3  # Windows

# Reapply migrations
python manage.py migrate
```

### Issue: Models not training / ML errors

**Solution:** Check internet connection (downloads data from online source):
```bash
python manage.py runserver
# Check terminal for errors
```

### Issue: Static files not loading (CSS/images not showing)

**Solution:** Collect static files:
```bash
python manage.py collectstatic
```

### Issue: Permission denied on macOS/Linux

**Solution:** Make manage.py executable:
```bash
chmod +x manage.py
```

---

## 🔐 Security Considerations

### For Production Deployment:

1. **Change Secret Key:**
   ```python
   # In settings.py
   SECRET_KEY = 'your-new-secure-random-key'
   ```

2. **Set DEBUG to False:**
   ```python
   DEBUG = False
   ```

3. **Update ALLOWED_HOSTS:**
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Use Environment Variables:**
   ```python
   import os
   SECRET_KEY = os.getenv('SECRET_KEY')
   DEBUG = os.getenv('DEBUG', False)
   ```

5. **Install gunicorn for production:**
   ```bash
   pip install gunicorn
   gunicorn diabetes_predictor.wsgi
   ```

---

## 📊 Using the Application

### 1. Make a Prediction

1. Navigate to http://localhost:8000/
2. Fill in health metrics:
   - Pregnancies
   - Glucose level
   - Blood pressure
   - Skin thickness
   - Insulin level
   - BMI
   - Diabetes pedigree function
   - Age
3. Click "🚀 Predict Diabetes Risk"
4. View results from both models

### 2. View Analytics

1. Go to http://localhost:8000/analytics/
2. See detailed metrics comparison
3. Understand model performance
4. Review data statistics

### 3. Check History

1. Visit http://localhost:8000/history/
2. View all previous predictions in a table
3. Track prediction trends

### 4. Admin Panel

1. Visit http://localhost:8000/admin/
2. Login with superuser credentials
3. Manage prediction history records
4. View database statistics

---

## 🚀 Next Steps

- **Customize the Application:**
  - Modify templates in `predictor/templates/`
  - Update styling in `predictor/static/`
  - Adjust form fields in `predictor/forms.py`

- **Add New Features:**
  - Custom data visualization
  - Export predictions to CSV
  - User authentication system
  - REST API endpoints

- **Deploy to Production:**
  - Use Heroku, AWS, or DigitalOcean
  - Configure PostgreSQL database
  - Set up SSL certificates
  - Enable caching

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [pandas Documentation](https://pandas.pydata.org/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

## 📞 Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review Django error messages in terminal
3. Check project logs in `django.log` (if enabled)

---

## 📄 License

This project is provided as-is for educational purposes.

---

## ⚠️ Medical Disclaimer

This application is for educational and informational purposes only. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare professional for medical concerns.

---

**Last Updated:** May 11, 2026  
**Version:** 1.0
