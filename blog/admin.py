from django.contrib import admin
from .models import Post, Tag, Category


class PostAdmin(admin.ModelAdmin):
    # 控制 Post 后台列表页展示的字段
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 控制后台表单展现的字段
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    # 自动填充作者信息
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
