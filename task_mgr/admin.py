from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Task_mgr_User


# Admin handler for user model
class Task_mgr_UserAdmin(UserAdmin):
    model = Task_mgr_User
    list_display = ("username", "email", "first_name", "last_name")

    fieldsets = (
        # Orgnize fields on admin page
        (None,
         {"fields": ("username",
                     "password",
                     )}),
        (_("Personal info"),
         {"fields": ("first_name",
                     "last_name",
                     "email",
                     "job_title",
                     )}),
        (_("Permissions"),
            {"fields": ("is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                        )}),
        # Presents user creation and last login dates
        (_("Important dates"),
         {"fields": ("last_login",
                     "date_joined",
                     )}),
    )

    # include extra fields in the admin user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,
         {"fields": ("job_title",
                     )}),
    )


admin.site.register(Task_mgr_User, Task_mgr_UserAdmin)
