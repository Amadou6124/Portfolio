from django.urls import path
from .views import portfolio_onepage


urlpatterns = [
    path('', portfolio_onepage, name="accueil"),
]