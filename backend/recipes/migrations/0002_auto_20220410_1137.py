# Generated by Django 2.2.19 on 2022-04-10 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='recipe',
            new_name='recipes',
        ),
    ]
