from django.contrib import admin
from NewsPaper.NewsPaper.models import *


admin.site.reqister(Post)
admin.site.register(Author)
admin.site.reqister(Category)
admin.site.reqister(Comment)