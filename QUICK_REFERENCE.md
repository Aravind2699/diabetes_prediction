# 🚀 Quick Reference Guide

## ⚡ Common Commands

### Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

### Installation & Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Upgrade pip
pip install --upgrade pip

# Check installed packages
pip list

# Freeze current environment
pip freeze > requirements.txt
```

### Database Management

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser

# Reset database (caution: deletes all data)
python manage.py migrate zero predictor
python manage.py migrate
```

### Running the Server

```bash
# Start development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8001

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000

# Run in production mode (with gunicorn)
gunicorn diabetes_predictor.wsgi
```

### Django Shell

```bash
# Open Django interactive shell
python manage.py shell

# Example commands inside shell:
# >>> from predictor.models import PredictionHistory
# >>> PredictionHistory.objects.all()
# >>> PredictionHistory.objects.count()
# >>> exit()
```

### Static Files

```bash
# Collect static files (production)
python manage.py collectstatic

# Collect with no input
python manage.py collectstatic --noinput

# Clear static files
python manage.py collectstatic --clear
```

### Testing & Debugging

```bash
# Run tests
python manage.py test

# Run specific test app
python manage.py test predictor

# Check project for issues
python manage.py check

# Show SQL queries
python manage.py sqlall predictor
```

### User Management

```bash
# Change superuser password
python manage.py changepassword admin

# Delete user
python manage.py shell
# >>> from django.contrib.auth.models import User
# >>> User.objects.get(username='username').delete()

# Create user
python manage.py createsuperuser
```

### Performance & Optimization

```bash
# Run development server with threading
python manage.py runserver --threaded

# Profile Django application
python manage.py runprofileserver

# Show slow queries
python manage.py debugsqlshell
```

---

## 🌐 Application URLs

| Feature | URL | Method |
|---------|-----|--------|
| **Home** | http://localhost:8000/ | GET, POST |
| **Analytics** | http://localhost:8000/analytics/ | GET |
| **History** | http://localhost:8000/history/ | GET |
| **About** | http://localhost:8000/about/ | GET |
| **Admin** | http://localhost:8000/admin/ | GET, POST |
| **Admin Login** | http://localhost:8000/admin/login/ | GET, POST |

---

## 📝 Environment Variables

Create `.env` file for sensitive settings:

```bash
# .env file
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

Load in `settings.py`:

```python
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG', True)
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
```

---

## 🔍 Debugging Tips

### Enable Detailed Logging

Add to `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
```

### SQL Query Logging

```python
# In Django shell or views
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as context:
    # Your code here
    pass

for query in context:
    print(query)
```

### View Request/Response

```python
# In views.py
import logging
logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug(f"Request: {request.method} {request.path}")
    logger.debug(f"POST data: {request.POST}")
    return response
```

---

## 📊 Database Queries

### Django ORM Examples

```python
from predictor.models import PredictionHistory

# Get all predictions
all_predictions = PredictionHistory.objects.all()

# Filter predictions
diabetic_predictions = PredictionHistory.objects.filter(prediction_rf="Diabetic ⚠️")

# Count predictions
total = PredictionHistory.objects.count()

# Order by date
recent = PredictionHistory.objects.all().order_by('-created_at')[:10]

# Get specific prediction
prediction = PredictionHistory.objects.get(id=1)

# Update prediction
prediction.prediction_rf = "Not Diabetic ✅"
prediction.save()

# Delete prediction
prediction.delete()

# Aggregate data
from django.db.models import Count, Avg
stats = PredictionHistory.objects.aggregate(
    total=Count('id'),
    avg_glucose=Avg('glucose')
)
```

---

## 🐍 Python Virtual Environment Management

### Create Project-specific Environment

```bash
# Create venv in project directory
python -m venv env_name

# List all packages
pip list

# Install specific version
pip install Django==4.2.13

# Install from requirements with specific Python version
python3.9 -m venv venv
```

### Troubleshooting venv

```bash
# Remove old venv (if needed)
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# Recreate venv
python -m venv venv

# Verify venv is using correct Python
which python  # macOS/Linux
where python  # Windows
```

---

## 🔐 Security Commands

### Change Secret Key

```bash
# Generate new secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Update in settings.py
SECRET_KEY = 'your-new-key-here'
```

### CSRF Token in Templates

```html
<!-- Add to all POST forms -->
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

### Secure Cookie Settings

```python
# In settings.py for production
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
```

---

## 📦 Package Management

### Create requirements.txt

```bash
# Generate from current environment
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Verify installation
pip check
```

### Update Packages

```bash
# Update single package
pip install --upgrade Django

# Update all packages
pip install -U -r requirements.txt
```

---

## 🚀 Deployment Commands

### Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Run with Gunicorn

```bash
# Install gunicorn
pip install gunicorn

# Run application
gunicorn diabetes_predictor.wsgi:application --bind 0.0.0.0:8000

# Run with workers
gunicorn diabetes_predictor.wsgi:application --workers 4 --bind 0.0.0.0:8000
```

### Run with uWSGI

```bash
# Install uWSGI
pip install uwsgi

# Run application
uwsgi --http :8000 --wsgi-file diabetes_predictor/wsgi.py --master --processes 4 --threads 2
```

---

## 🧪 Testing Commands

```bash
# Run all tests
python manage.py test

# Run specific test
python manage.py test predictor.tests.PredictionTestCase

# Run with verbosity
python manage.py test --verbosity=2

# Run specific test method
python manage.py test predictor.tests.PredictionTestCase.test_prediction
```

---

## 📋 Project Structure Commands

### List all Django apps

```bash
python manage.py list
```

### Show installed apps

```bash
# In Django shell
from django.conf import settings
print(settings.INSTALLED_APPS)
```

### Check project structure

```bash
# Find all Python files
find . -name "*.py" -type f

# Count lines of code
find . -name "*.py" -exec wc -l {} +
```

---

## 🎯 Common Workflows

### Development Workflow

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Make code changes
# ... edit files ...

# 3. Create migrations (if models changed)
python manage.py makemigrations

# 4. Apply migrations
python manage.py migrate

# 5. Run development server
python manage.py runserver

# 6. Test in browser
# Visit http://localhost:8000
```

### Deployment Workflow

```bash
# 1. Update requirements
pip freeze > requirements.txt

# 2. Run tests
python manage.py test

# 3. Collect static files
python manage.py collectstatic --noinput

# 4. Check for errors
python manage.py check

# 5. Run production server
gunicorn diabetes_predictor.wsgi
```

---

## 📚 Useful Resources

### Django
- Official Docs: https://docs.djangoproject.com/
- Django Girls Tutorial: https://tutorial.djangogirls.org/

### Scikit-learn
- Official Docs: https://scikit-learn.org/
- User Guide: https://scikit-learn.org/stable/user_guide.html

### Python
- Official Docs: https://docs.python.org/
- Virtual Environments: https://docs.python.org/3/tutorial/venv.html

---

## ❓ Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Activate venv and run `pip install -r requirements.txt` |
| Port 8000 in use | Use `python manage.py runserver 8001` |
| Database locked | Delete `db.sqlite3` and re-run migrations |
| Static files missing | Run `python manage.py collectstatic` |
| Import errors | Ensure venv is activated |
| CSS/JS not loading | Clear browser cache (Ctrl+F5) |

---

**Happy Coding! 🎉**

For more details, see [README.md](README.md) and [INSTALL.md](INSTALL.md)
