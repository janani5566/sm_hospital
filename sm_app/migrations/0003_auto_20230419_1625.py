# Generated by Django 3.0.10 on 2023-04-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm_app', '0002_ipmodel_admitdate_ipmodel_dischargedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
