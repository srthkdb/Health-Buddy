# Generated by Django 2.2.2 on 2019-07-05 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0008_auto_20190704_0028'),
        ('Doctor', '0014_auto_20190703_0342'),
        ('Reception', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateNtime', models.DateTimeField(auto_now_add=True)),
                ('brief', models.TextField(blank=True)),
                ('reqApproval', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('refer_remarks', models.TextField(blank=True)),
                ('is_referred', models.BooleanField(default=False)),
                ('doc_ref', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_ref', to='Doctor.Doctor')),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='Doctor.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Patient')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Prescription')),
            ],
        ),
    ]
