from django.contrib import admin

from .models import User, Category, Joke

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Joke)


admin.site.site_header = "代码之间笑话工厂APP - 后台管理"
admin.site.site_title = "后台管理"


