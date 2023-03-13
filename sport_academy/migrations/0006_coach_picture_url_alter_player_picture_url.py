# Generated by Django 4.1.7 on 2023-03-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_academy', '0005_player_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='picture_url',
            field=models.CharField(default='/images/coaches/avatar.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='picture_url',
            field=models.CharField(default='/images/players/avatar.png', max_length=255),
        ),
    ]
