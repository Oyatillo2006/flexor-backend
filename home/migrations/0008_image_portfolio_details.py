# Generated by Django 4.2.5 on 2023-09-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_portfolio_client_remove_portfolio_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_portfolio_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.FileField(upload_to='images/Portfolio_details')),
            ],
        ),
    ]