from django import template

register = template.Library()


@register.filter(name='lookup')
def lookup(value, arg):
    try:
        return value[arg]
    except Exception:
        return None


@register.filter(name='get_player')
def get_player(value, arg):
    if value is None:
        return "-"
    if arg == 1:
        return value[0].player1.profile.identifiant
    return value[0].player2.profile.identifiant
