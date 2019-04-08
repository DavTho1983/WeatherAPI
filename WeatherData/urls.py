from django.urls import path
from .views import ResultAPIListView, ResultAPIID

urlpatterns = [
    path("", ResultAPIListView.as_view(), name="results_api_list"),
    path("<int:pk>", ResultAPIID.as_view(), name="results_api_detail"),
]
