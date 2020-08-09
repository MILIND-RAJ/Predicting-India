from django.contrib import admin

# Register your models here.
from .models import signupform,loginform,railway1,tourismm,fertilizerm,educationm
admin.site.register(signupform)
admin.site.register(loginform)
admin.site.register(railway1)
admin.site.register(tourismm)
admin.site.register(educationm)
admin.site.register(fertilizerm)

