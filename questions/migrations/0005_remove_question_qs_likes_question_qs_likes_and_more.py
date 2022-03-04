# Generated by Django 4.0.2 on 2022-03-02 05:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0004_question_qs_dislikes_question_qs_likes_preference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='qs_likes',
        ),
        migrations.AddField(
            model_name='question',
            name='qs_likes',
            field=models.ManyToManyField(related_name='questions_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]