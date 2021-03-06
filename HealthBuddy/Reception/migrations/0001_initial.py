
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patient', '0001_initial'),
        ('Doctor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_roll', models.PositiveIntegerField()),
                ('dateNtime', models.DateTimeField(auto_now_add=True)),
                ('brief', models.TextField(blank=True)),
                ('reqApproval', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('w', 'Waiting'), ('e', 'Examining'), ('t', 'Terminated')], default='w', max_length=2)),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Doctor.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Patient')),
            ],
        ),
    ]
