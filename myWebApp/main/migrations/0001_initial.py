# Generated by Django 4.2 on 2023-05-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО')),
                ('title', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
