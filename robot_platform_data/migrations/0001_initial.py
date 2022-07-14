# Generated by Django 3.1.14 on 2022-05-03 17:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RobotPlatformData_CxtaTests_log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('log_content', models.TextField()),
            ],
            options={
                'verbose_name': 'CXTA_log',
                'verbose_name_plural': 'CXTA_logs',
                'ordering': ('date_added', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='RobotPlatformData_CxtaTests_output',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('log_content', models.JSONField()),
            ],
            options={
                'verbose_name': 'CXTA_output',
                'verbose_name_plural': 'CXTA_outputs',
                'ordering': ('date_added', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='RobotPlatformData_CxtaTests_report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('log_content', models.TextField()),
            ],
            options={
                'verbose_name': 'CXTA_report',
                'verbose_name_plural': 'CXTA_reports',
                'ordering': ('date_added', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='RobotPlatformData_MetaData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('current', models.BooleanField(default=True)),
                ('metadata', models.JSONField()),
            ],
            options={
                'verbose_name': 'Metadata',
                'ordering': ('date_added', 'pk'),
            },
        ),
    ]
