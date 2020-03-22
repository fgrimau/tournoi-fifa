from django.urls import path
from django.conf.urls import include
import home.views

urlpatterns = [
    path('', home.views.home, name="home_view"),
    path('scores/', include('matching.urls')),
]
