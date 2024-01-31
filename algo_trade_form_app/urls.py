from django.urls import path
from .views import AlgoFormView

urlpatterns = [
    path('form', AlgoFormView.as_view() ),
]