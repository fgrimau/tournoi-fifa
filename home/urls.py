from django.urls import path
from django.conf.urls import include
import home.views

urlpatterns = [
    path('', home.views.home, name="home_view"),
    path('forgotpass/', home.views.reset_password, name="forgotpass"),
    path(
        'reset/<slug:token>/',
        home.views.reset_password_form_view, name="resetpass"),
    path('scores/', include('matching.urls')),
]
