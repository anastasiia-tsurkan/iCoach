from django.contrib.auth.models import AbstractUser
from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=67, unique=True)
    country = models.CharField(max_length=67)
    city = models.CharField(max_length=67)
    main_stadium = models.CharField(max_length=67)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.city}"


class Team(models.Model):
    name = models.CharField(max_length=67, unique=True)
    status = models.CharField(max_length=67)
    league = models.CharField(max_length=67)
    season = models.CharField(max_length=67)
    club = models.ForeignKey(
        Club,
        related_name="teams",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.club.name} {self.name} team"


class Coach(AbstractUser):
    team = models.ManyToManyField(
        Team,
        related_name="teams",
    )

    class Meta:
        verbose_name = "coach"
        verbose_name_plural = "coaches"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Position(models.Model):
    position_name = models.CharField(max_length=67)

    def __str__(self):
        return self.position_name


class Player(models.Model):
    first_name = models.CharField(max_length=67)
    last_name = models.CharField(max_length=67)
    birth_date = models.DateField(max_length=67)
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="players"
    )
    nationality = models.CharField(max_length=67)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position.position_name})"
