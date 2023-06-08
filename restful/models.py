import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    img_field = models.ImageField(blank=True, upload_to="photos/")

    class Meta:
        verbose_name = "Новини"
        verbose_name_plural = "Новини"

    def __str__(self):
        return self.title


PERIOD_CHOICES = [
    ("06:00 - 07:00", _("06:00 - 07:00")),
    ("07:00 - 08:00", _("07:00 - 08:00")),
    ("08:00 - 09:00", _("08:00 - 09:00")),
    ("09:00 - 10:00", _("09:00 - 10:00")),
    ("10:00 - 11:00", _("10:00 - 11:00")),
    ("11:00 - 12:00", _("11:00 - 12:00")),
    ("12:00 - 13:00", _("12:00 - 13:00")),
    ("13:00 - 14:00", _("13:00 - 14:00")),
    ("14:00 - 15:00", _("14:00 - 15:00")),
    ("15:00 - 16:00", _("15:00 - 16:00")),
    ("16:00 - 17:00", _("16:00 - 17:00")),
    ("17:00 - 18:00", _("17:00 - 18:00")),
    ("18:00 - 19:00", _("18:00 - 19:00")),
    ("19:00 - 20:00", _("19:00 - 20:00")),
    ("20:00 - 21:00", _("20:00 - 21:00")),
    ("21:00 - 22:00", _("21:00 - 22:00")),
]


class Profile(AbstractUser):
    GENDER_CHOICES = [
        ("Mr", _("Чоловік")),
        ("Ms", _("Жінка")),
    ]
    gender = models.CharField(
        max_length=30,
        choices=GENDER_CHOICES,
        default="Mr",
        blank=True,
        null=True,
        verbose_name="Стать"
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name="День народження")
    phone = models.CharField(null=True, blank=True, max_length=30, verbose_name="Телефон")
    photo = models.ImageField(blank=True, upload_to="photos/")
    city = models.CharField(max_length=30, blank=True)
    is_booking_period = models.BooleanField(default=False, verbose_name="Чи є бронювання періоду?")

    CORT_CHOICES = [
        ("1", _("Зелений")),
        ("2", _("Червоний")),
    ]
    cort = models.CharField(
        max_length=3,
        choices=CORT_CHOICES,
        default="1",
        verbose_name="Корт",
    )
    period = models.CharField(
        max_length=16,
        choices=PERIOD_CHOICES,
        default="06:00 - 07:00",
        blank=True,
        null=True,
        verbose_name="Період бронювання"
    )

    class Meta:
        verbose_name = "Профіль користувача"
        verbose_name_plural = "Профіль користувача"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class BookingModelGreen(models.Model):
    period = models.CharField(
        max_length=16,
        choices=PERIOD_CHOICES,
        default="06:00 - 07:00",
        blank=False,
        null=False,
        verbose_name="Період бронювання"
    )
    CORT_CHOICES = [
        ("1", _("Зелений")),
        ("2", _("Червоний")),
    ]
    cort = models.CharField(
        max_length=3,
        choices=CORT_CHOICES,
        default="1",
        blank=False,
        null=False,
        verbose_name="Корт",
    )
    booking_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата бронювання",
    )
    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        verbose_name="Персона, що бронює"
    )

    class Meta:
        verbose_name = "Бронювання корту"
        verbose_name_plural = "Бронювання корту"

    def __str__(self):
        return self.period + " " + self.booking_date.strftime("%d-%m-%Y") + " " + self.user.__str__()


class BookingModelRed(models.Model):
    period = models.CharField(
        max_length=16,
        choices=PERIOD_CHOICES,
        default="06:00 - 07:00",
        blank=False,
        null=False,
        verbose_name="Період бронювання"
    )
    CORT_CHOICES = [
        ("1", _("Зелений")),
        ("2", _("Червоний")),
    ]
    cort = models.CharField(
        max_length=3,
        choices=CORT_CHOICES,
        default="2",
        blank=False,
        null=False,
        verbose_name="Корт",
    )
    booking_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата бронювання",
    )
    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        verbose_name="Персона, що бронює"
    )

    class Meta:
        verbose_name = "Бронювання корту"
        verbose_name_plural = "Бронювання корту"

    def __str__(self):
        return self.period + " " + self.booking_date.strftime("%d-%m-%Y") + " " + self.user.__str__()