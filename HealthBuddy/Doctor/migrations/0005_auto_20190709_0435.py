# Generated by Django 2.2.2 on 2019-07-08 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0004_auto_20190709_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresConsultDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Doctor')),
                ('pres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription')),
            ],
        ),
        migrations.DeleteModel(
            name='PresVisits',
        ),
    ]