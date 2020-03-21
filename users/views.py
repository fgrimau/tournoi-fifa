from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/en/users")
def profile_view(request, lang=""):
    user_history = request.user.winner.all() | request.user.looser.all()
    total_points = request.user.winner.filter(null_match=False).count() * 3\
        + request.user.winner.filter(null_match=True).count()

    return render(request, "profil.html", locals())
