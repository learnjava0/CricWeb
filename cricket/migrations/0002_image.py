# Generated by Django 5.0.4 on 2024-04-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/images/dcTeam')),
            ],
        ),
    ]
