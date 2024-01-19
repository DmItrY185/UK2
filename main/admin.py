from django.contrib import admin

from main.models import Code


class CodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'date_create')
    list_display_links = ('id', 'code')
    search_fields = ('code',)
    list_filter = ('date_create',)


admin.site.register(Code, CodeAdmin)
