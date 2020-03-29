from django.urls import path
import connexion.views
import users.views

urlpatterns = [
    path('', connexion.views.register_view, name="register_view"),
    path(
        'complete/', connexion.views.complete_profile_view,
        name="complete_registration"),
    path(
        'final/', connexion.views.payment_view,
        name="final_registration"),
    path('login/', connexion.views.login_view, name="login_view"),
    path('disconnect/', connexion.views.disconnect, name="disconnect_view"),
    path('me/', users.views.profile_view, name="profile_view"),
    path('all/', users.views.user_list_view, name="list_user_view"),
    path(
        '<str:username>/', users.views.other_profile_view,
        name="other_profile_view"),
]
