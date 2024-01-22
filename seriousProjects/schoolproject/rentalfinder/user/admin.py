from django.contrib import admin
from user.models import UserModel


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'dob',
        'gender',
    )


admin.site.register(UserModel, UserAdmin)
