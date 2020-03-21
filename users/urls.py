from django.urls import path
import connexion.views
import users.views

urlpatterns = [
    path('', connexion.views.register_view, name="register_view"),
    path('login/', connexion.views.login_view, name="login_view"),
    path('disconnect/', connexion.views.disconnect, name="disconnect_view"),
    path('me/', users.views.profile_view, name="profile_view"),
]
