# Generated by Django 3.1.7 on 2021-04-07 07:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='activity_description',
            fields=[
                ('act_descp', models.CharField(blank=True, max_length=200, primary_key=True, serialize=False)),
                ('act_descp_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('project_number', models.IntegerField(primary_key=True, serialize=False)),
                ('report_number', models.IntegerField(unique=True)),
                ('data_perform', models.DateTimeField(default=datetime.datetime(2021, 4, 7, 12, 50, 56, 924592))),
                ('project_user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='drawing',
            fields=[
                ('drawing_number', models.CharField(max_length=200)),
                ('drawing_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inspection.project')),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('photo', models.ImageField(default='weld.png', upload_to='photo_pics')),
                ('photo_report_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inspection.project')),
            ],
        ),
        migrations.CreateModel(
            name='heat_calc',
            fields=[
                ('current_A', models.IntegerField(blank=True, default=0)),
                ('voltage_V', models.IntegerField(blank=True, default=0)),
                ('time_SS', models.IntegerField(blank=True, default=0)),
                ('length_MM', models.IntegerField(blank=True, default=0)),
                ('heat_input', models.IntegerField(blank=True, default=0)),
                ('heat_calc_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inspection.project')),
            ],
        ),
        migrations.CreateModel(
            name='location_discipline',
            fields=[
                ('location_name', models.CharField(max_length=200)),
                ('discipline_name', models.CharField(max_length=200)),
                ('location_discipline_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inspection.project')),
            ],
        ),
        migrations.CreateModel(
            name='weld_action',
            fields=[
                ('during_welding', models.BooleanField(default=False)),
                ('before_welding', models.BooleanField(default=False)),
                ('after_welding', models.BooleanField(default=False)),
                ('weld_action_project_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inspection.project')),
            ],
        ),
        migrations.CreateModel(
            name='activity_inspection_action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('according', models.BooleanField(default=False)),
                ('not_according', models.BooleanField(default=False)),
                ('correction_action', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=100)),
                ('act_desp_action_descp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.activity_description')),
                ('inspection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.project')),
            ],
        ),
        migrations.CreateModel(
            name='weld',
            fields=[
                ('weld_number', models.IntegerField(primary_key=True, serialize=False)),
                ('weld_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.drawing')),
            ],
        ),
    ]
