# Generated by Django 4.0.5 on 2023-05-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_facematching_match_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='facematching',
            name='message',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
