from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'content', 'get_photo', 'photo', 'category', 'views', 'created_at', 'updated_at', 'is_published')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{ obj.photo.url }" width="85">')
        # else:
        #     return mark_safe(f'<img src="https://picsum.photos/id/1060/75/40/?blur=2">')
        return '-'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админка для крутых пацанов'
admin.site.site_header = 'Админка для крутых пацанов'

