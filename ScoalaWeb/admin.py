from django.contrib import admin

# Register your models here.

from .models import Post, Documente, Activitati, Images
admin.site.register(Post)
admin.site.register(Images)
admin.site.register(Activitati)
admin.site.register(Documente)


