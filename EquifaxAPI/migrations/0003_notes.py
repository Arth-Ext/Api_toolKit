# Generated by Django 3.1.2 on 2023-06-16 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EquifaxAPI', '0002_auto_20230616_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_column='created_on', default=django.utils.timezone.localtime)),
                ('updated_on', models.DateTimeField(db_column='updated_on', default=django.utils.timezone.localtime)),
                ('is_deleted', models.BooleanField(default=False)),
                ('note_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video'), ('text', 'Text')], max_length=10)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='notes/audio/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='notes/video/')),
                ('text_content', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated_on', '-created_on'),
                'get_latest_by': 'updated_on',
                'abstract': False,
                'default_permissions': (),
            },
        ),
    ]
