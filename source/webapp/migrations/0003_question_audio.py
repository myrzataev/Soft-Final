# Generated by Django 5.0.4 on 2024-05-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_question_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='audio',
            field=models.FileField(default='23/23', upload_to='questions/'),
            preserve_default=False,
        ),
    ]
