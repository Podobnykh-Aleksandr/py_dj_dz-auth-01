from django.contrib import admin

# Register your models here.
from advertisements.models import Advertisement


# Register your models here.
class AdvertisementInline(admin.TabularInline):
    model = Advertisement  # промежуточная таблица


class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [AdvertisementInline]
    list_display = ['id', 'brand', 'model', 'color']  # отображение в админке в виде таблицы
    list_filter = ['brand', 'model']  # фильтрация в админке по выбранным полям