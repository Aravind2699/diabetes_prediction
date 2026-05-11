from django.db import models

# Create your models here.
class PredictionHistory(models.Model):
    pregnancies = models.FloatField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.FloatField()
    prediction_lr = models.CharField(max_length=20)
    prediction_rf = models.CharField(max_length=20)
    confidence_lr = models.FloatField(default=0.0)
    confidence_rf = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Prediction {self.id} - {self.created_at}"
