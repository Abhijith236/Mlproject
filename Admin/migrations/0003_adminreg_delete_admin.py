# Generated by Django 4.2.5 on 2023-09-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.IntegerField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
