from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from .views import AppLoginView


urlpatterns = [
    path('login/', AppLoginView.as_view(), name='login'),
    path('', RedirectView.as_view(url=reverse_lazy('login')))
]