from django.urls import path, reverse_lazy
from .views import HomeView, OfferDetailView, SearchView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('offer/<int:pk>/', OfferDetailView.as_view(), name='offer_detail'),
    path('search/', SearchView.as_view(), name='search_results'),
]