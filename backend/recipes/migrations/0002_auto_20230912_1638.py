# Generated by Django 3.2.16 on 2023-09-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Имя'),
        ),
    ]
