# Generated by Django 5.0.2 on 2024-02-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, upload_to='course_previews/'),
        ),
    ]
