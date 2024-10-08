# Generated by Django 5.1.1 on 2024-09-08 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ITTeam',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=255)),
                ('expertise_areas', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestService',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('request_description', models.TextField()),
                ('request_status', models.CharField(max_length=100)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.requestservice')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.itteam')),
            ],
        ),
    ]
