from django.urls import path
from .views import ResultAPIView

urlpatterns = [
    path('', ResultAPIView.as_view(), name='results_api'),
]