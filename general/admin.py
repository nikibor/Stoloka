from django.contrib import admin

# Register your models here.
from .models import Report, Place, Rate


class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'latitude',
        'longitude',
        'title',
        'rating',
        'address',
        'views'
    ]
    list_filter = [
        'feature'
    ]


class ReportAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'date',
        'mark'
    ]
    list_filter = [
        'mark'
    ]


class RateAdmin(admin.ModelAdmin):
    list_display = [
        'place',
        'mark'
    ]
    list_filter = [
        'mark'
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Rate, RateAdmin)
