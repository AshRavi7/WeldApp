# Generated by Django 3.1.6 on 2021-03-30 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0005_auto_20210330_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heat_calc',
            name='id',
        ),
        migrations.AlterField(
            model_name='heat_calc',
            name='heat_calc_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inspection.project'),
        ),
    ]