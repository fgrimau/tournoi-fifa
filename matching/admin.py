from django.contrib import admin
import matching.models
from matching.models import Finale_poule


class HistoryAdmin(admin.ModelAdmin):
    list_display = [
        "id", "player1", "player2", "player1_points",
        "player2_points", "date_played", "played"]
    list_filter = ["player1", "player2", "date_played"]
    ordering = ["date_played"]
    search_fields = ["player1", "player2"]


class PouleAdmin(admin.ModelAdmin):
    list_display = ["id", "platform", "is_finished"]
    list_filter = ["platform", "is_finished"]
    ordering = ["id"]
    search_fields = ["id", "platform"]


class FinalePouleAdmin(admin.ModelAdmin):
    list_display = ["level", "platform", "player1", "player2", "finished"]
    list_filter = ["platform", "finished"]
    ordering = ["id"]
    search_fields = ["id", "platform", "player1", "player2"]
    actions = ["generate_next"]

    def generate_next(modeladmin, request, queryset):
        if queryset.count() > 1:
            print("NO !")

        obj = queryset[0]
        obj.finished = True
        obj.save()

        if (int(obj.level[0])-1) % 2 == 0:  # AS FIRST PLAYER (TOP)
            other_level = ""
            nb_chiffres = obj.level.count("_") + 1
            for x in range(nb_chiffres):
                other_level += str(int(obj.level[(x*2)])+1) + "_"
            other_level = other_level[:-1]

            qs = Finale_poule.objects.filter(level=other_level)
            if qs.count() == 0:
                print("NO ACCOLYTE")
                return

            print("QS[0] :", qs[0].level)
            print("OBJ :", obj.level)

            qs_next = Finale_poule.objects.filter(
                player2=qs[0].winner_user).exclude(level=qs[0].level)

            if qs_next.count() == 0:
                newPoule = Finale_poule(
                    level="{}_{}".format(obj.level, qs[0].level),
                    player1=obj.winner_user, platform=obj.platform)
                newPoule.save()
            else:
                nextPoule = qs_next[0]
                nextPoule.player1 = obj.winner_user
                nextPoule.save()
        else:  # AS SECOND PLAYER (BOTTOM)
            other_level = ""
            nb_chiffres = obj.level.count("_") + 1
            for x in range(nb_chiffres):
                other_level += str(int(obj.level[(x*2)])-1) + "_"
            other_level = other_level[:-1]

            # The other pool that has to be mixed with this one
            qs = Finale_poule.objects.filter(level=other_level)
            if qs.count() == 0:
                print("NO ACCOLYTE")
                return

            qs_next = Finale_poule.objects.filter(
                player1=qs[0].winner_user).exclude(level=qs[0].level)

            if qs_next.count() == 0:
                newPoule = Finale_poule(
                    level="{}_{}".format(qs[0].level, obj.level),
                    player2=obj.winner_user, platform=obj.platform)
                newPoule.save()
            else:
                nextPoule = qs_next[0]
                nextPoule.player2 = obj.winner_user
                nextPoule.save()

    generate_next.short_description = "\
        Set as finished and generate the next pool"


admin.site.register(matching.models.Poule, PouleAdmin)
admin.site.register(matching.models.Finale_poule, FinalePouleAdmin)
admin.site.register(matching.models.History, HistoryAdmin)
