# Generated by Django 3.1.7 on 2021-03-17 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectReport', '0008_activity_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity_inspection_action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('according', models.BooleanField(default=False)),
                ('not_according', models.BooleanField(default=False)),
                ('correction_action', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=100)),
                ('act_desp_action_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='projectReport.activity_description')),
                ('inspection_id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='projectReport.project')),
            ],
        ),
    ]
