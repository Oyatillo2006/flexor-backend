# Generated by Django 4.2.5 on 2023-09-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_professions_support_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='image',
            field=models.ImageField(default=2, upload_to='images/sepports'),
            preserve_default=False,
        ),
    ]