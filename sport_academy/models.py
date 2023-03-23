from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
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
    name = models.CharField(max_length=67)
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

    @property
    def num_of_players(self):
        return self.players.count()


def validate_birth_date(value):
    if value.birth_date > date(1950, 1, 1):
        return value
    raise ValidationError("Birth date error")


class Coach(AbstractUser):
    MIN_BIRTH_DATE = date(1950, 1, 1)

    team = models.ManyToManyField(
        Team,
        blank=True,
        related_name="coaches"
    )
    position = models.CharField(max_length=67, null=True)
    picture_url = models.CharField(
        max_length=255,
        default="/images/coaches/avatar.png"
    )
    birth_date = models.DateField(
        MinValueValidator(
            MIN_BIRTH_DATE,
            message="Birth date shouldn't be earlier than 1 Jan, 1950"
        ),
        default=date(1980, 1, 1)
    )

    class Meta:
        verbose_name = "coach"
        verbose_name_plural = "coaches"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
                (today.month, today.day) <
                (self.birth_date.month, self.birth_date.day)
        )
        return age


class Position(models.Model):
    position_name = models.CharField(max_length=67)

    class Meta:
        ordering = ["position_name"]

    def __str__(self):
        return self.position_name


class Player(models.Model):
    first_name = models.CharField(max_length=67)
    last_name = models.CharField(max_length=67)
    birth_date = models.DateField()
    number = models.IntegerField()
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
    picture_url = models.CharField(
        max_length=255,
        default="/images/players/avatar.png"
    )

    class Meta:
        ordering = ["position", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} " \
               f"({self.position.position_name})"

    @property
    def age(self):
        today = date.today()
        age = (today.year - self.birth_date.year -
               ((today.month, today.day) <
                (self.birth_date.month, self.birth_date.day)))
        return age
