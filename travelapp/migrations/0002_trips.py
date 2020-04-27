# Generated by Django 2.2.4 on 2020-04-27 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=455)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attedning', models.ManyToManyField(related_name='going', to='travelapp.users')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_uploaded', to='travelapp.users')),
            ],
        ),
    ]
