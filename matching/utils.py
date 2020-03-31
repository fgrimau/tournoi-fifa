from users.models import Profile
from random import randrange


def create_pools(nb_pools, platform):
    users = [prof.user.username for prof in Profile.objects.filter(platform=platform, user__is_staff=False)]
    final = {}
    users_per_pool = len(users) // nb_pools
    leftover = len(users) % nb_pools

    for pool in range(nb_pools):
        final[str(pool)] = []
        for user_index in range(users_per_pool):
            randomIndex = randrange(0, len(users))
            final[str(pool)].append(users[randomIndex])
            del users[randomIndex]

    for pool in range(leftover):
        randomIndex = randrange(0, len(users))
        final[str(pool)].append(users[randomIndex])
        del users[randomIndex]

    return final
