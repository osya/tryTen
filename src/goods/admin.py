from django.contrib import admin

from goods.models import Good


class GoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category', 'name')}
    # TODO: Make prepopulated_fields somehow fill `slug` field based on (category.name, name)


admin.site.register(Good, GoodAdmin)
