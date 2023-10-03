from django.urls import path
from .views import PredictionView

urlpatterns = [
    path('', PredictionView.as_view(), name='root'),
    path('predict/', PredictionView.as_view(), name='predict'),
]
