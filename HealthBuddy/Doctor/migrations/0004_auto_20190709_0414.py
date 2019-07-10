# Generated by Django 2.2.2 on 2019-07-08 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_auto_20190709_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='date',
        ),
        migrations.CreateModel(
            name='PresVisits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription')),
            ],
        ),
    ]
