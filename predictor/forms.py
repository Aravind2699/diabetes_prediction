from django import forms

class DiabetesPredictionForm(forms.Form):
    pregnancies = forms.FloatField(
        label='Pregnancies',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of pregnancies',
            'min': '0',
            'step': '1'
        })
    )
    glucose = forms.FloatField(
        label='Glucose (mg/dL)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Glucose level',
            'min': '0'
        })
    )
    blood_pressure = forms.FloatField(
        label='Blood Pressure (mmHg)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Blood pressure',
            'min': '0'
        })
    )
    skin_thickness = forms.FloatField(
        label='Skin Thickness (mm)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Skin thickness',
            'min': '0'
        })
    )
    insulin = forms.FloatField(
        label='Insulin (mu U/ml)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Insulin level',
            'min': '0'
        })
    )
    bmi = forms.FloatField(
        label='BMI (Body Mass Index)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'BMI',
            'min': '0'
        })
    )
    diabetes_pedigree_function = forms.FloatField(
        label='Diabetes Pedigree Function',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Diabetes pedigree',
            'min': '0'
        })
    )
    age = forms.FloatField(
        label='Age (years)',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Age',
            'min': '0'
        })
    )
