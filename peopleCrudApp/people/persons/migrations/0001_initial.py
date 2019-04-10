# Generated by Django 2.2 on 2019-04-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
    ]
