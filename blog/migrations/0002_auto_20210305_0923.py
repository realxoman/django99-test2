# Generated by Django 3.1.7 on 2021-03-05 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='author',
            new_name='user',
        ),
    ]