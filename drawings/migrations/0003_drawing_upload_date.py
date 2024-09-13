# Generated by Django 5.1.1 on 2024-09-13 07:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawings', '0002_category_remove_drawing_upload_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawing',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
