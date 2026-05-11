from django.contrib import admin
from .models import PredictionHistory

@admin.register(PredictionHistory)
class PredictionHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', 'glucose', 'bmi', 'prediction_rf', 'confidence_rf', 'created_at')
    list_filter = ('created_at', 'prediction_rf')
    search_fields = ('glucose', 'bmi')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Health Metrics', {
            'fields': ('pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree_function', 'age')
        }),
        ('Predictions', {
            'fields': ('prediction_lr', 'prediction_rf', 'confidence_lr', 'confidence_rf')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )
