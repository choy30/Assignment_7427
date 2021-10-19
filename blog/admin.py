from django.contrib import admin

# Register your models here.
from blog.models import Dog, Activity

admin.site.register(Dog)
admin.site.register(Activity)