# Generated by Django 4.0.4 on 2022-10-30 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=250)),
                ('buy_date', models.DateField(auto_now_add=True, verbose_name='fecha de compra')),
                ('marca', models.CharField(max_length=250)),
            ],
        ),
    ]
