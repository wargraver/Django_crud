from django.contrib import admin
from .models import account, user


# Register your models here.
admin.site.register(user)
admin.site.register(account)

