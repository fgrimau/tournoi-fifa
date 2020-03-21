from django.urls import path
import connexion.views

urlpatterns = [
    path('', connexion.views.register_view, name="register_view"),
    path('login/', connexion.views.login_view, name="login_view"),
]
