from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Coach, Team, Player, Position, Club


@admin.register(Coach)
class CoachAdmin(UserAdmin):
    pass
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("team", "position")}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "team",
                        "position"
                    )
                }
            )
        )
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "league", "season", "club")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date", "position", "nationality", "team")
    search_fields = ("first_name", "last_name")


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city", "main_stadium",)


admin.site.register(Position)
