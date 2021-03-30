# Generated by Django 3.1.6 on 2021-03-30 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0003_auto_20210330_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_inspection_action',
            name='id',
        ),
        migrations.AlterField(
            model_name='activity_inspection_action',
            name='act_desp_action_descp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inspection.activity_description'),
        ),
    ]
