import datetime

from django.contrib import admin
from django.contrib.auth.models import Group
from restful.models import *
from restful.forms import *
# Register your models here.

admin.site.site_header = "Панель адміністратора"
admin.site.site_title = "Панель адміністратора"
admin.site.index_title = "Ласкаво просимо."

admin.site.register(News)
# admin.site.register(models.BookingModel)
admin.site.unregister(Group)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = (
        "first_name",
        "last_name",
        "username",
        "gender",
        "city",
        "phone",
        "photo",
        "password",
        "birth_date",
        "is_booking_period",
        "cort",
        "period"
    )


@admin.register(BookingModelGreen)
class BookingModelGreenAdmin(admin.ModelAdmin):
    list_display = ("period", "booking_date", "user", "cort")
    search_fields = ("booking_date", )
    date_hierarchy = "booking_date"
    actions = ['delete_last_month_bookings']

    def delete_last_month_bookings(self, request, queryset):
        current_month = datetime.datetime.now().month
        queryset.filter(booking_date__month__lt=current_month).delete()

    delete_last_month_bookings.short_description = "Видалити неактуальні дані"


@admin.register(BookingModelRed)
class BookingModelRedAdmin(admin.ModelAdmin):
    list_display = ("period", "booking_date", "user", "cort")
    search_fields = ("booking_date", )
    date_hierarchy = "booking_date"
    actions = ['delete_last_month_bookings']

    def delete_last_month_bookings(self, request, queryset):
        current_month = datetime.datetime.now().month
        queryset.filter(booking_date__month__lt=current_month).delete()

    delete_last_month_bookings.short_description = "Видалити неактуальні дані"

