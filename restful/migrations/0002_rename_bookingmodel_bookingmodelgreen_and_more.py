# Generated by Django 4.1.9 on 2023-06-06 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookingModel',
            new_name='BookingModelGreen',
        ),
        migrations.CreateModel(
            name='BookingModelRed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('06:00 - 07:00', '06:00 - 07:00'), ('07:00 - 08:00', '07:00 - 08:00'), ('08:00 - 09:00', '08:00 - 09:00'), ('09:00 - 10:00', '09:00 - 10:00'), ('10:00 - 11:00', '10:00 - 11:00'), ('11:00 - 12:00', '11:00 - 12:00'), ('12:00 - 13:00', '12:00 - 13:00'), ('13:00 - 14:00', '13:00 - 14:00'), ('14:00 - 15:00', '14:00 - 15:00'), ('15:00 - 16:00', '15:00 - 16:00'), ('16:00 - 17:00', '16:00 - 17:00'), ('17:00 - 18:00', '17:00 - 18:00'), ('18:00 - 19:00', '18:00 - 19:00'), ('19:00 - 20:00', '19:00 - 20:00'), ('20:00 - 21:00', '20:00 - 21:00'), ('21:00 - 22:00', '21:00 - 22:00')], default='06:00 - 07:00', max_length=16, verbose_name='Період бронювання')),
                ('cort', models.CharField(choices=[('1', 'Зелений'), ('2', 'Червоний')], default='2', max_length=3, verbose_name='Корт')),
                ('booking_date', models.DateField(verbose_name='Дата бронювання')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Персона, що бронює')),
            ],
            options={
                'verbose_name': 'Бронювання корту',
                'verbose_name_plural': 'Бронювання корту',
            },
        ),
    ]
