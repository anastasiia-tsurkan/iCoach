# Generated by Django 3.2.18 on 2023-03-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_academy', '0003_alter_coach_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='picture',
            field=models.ImageField(default='coaches/avatar.png', upload_to='coaches/'),
        ),
    ]
