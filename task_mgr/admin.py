from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Task_mgr_User, Task_mgr_Task


# Admin handler for user model
@admin.register(Task_mgr_User)
class Task_mgr_UserAdmin(UserAdmin):
    ''' Admin view for Users'''
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


@admin.register(Task_mgr_Task)
class Task_mgr_TaskAdmin(admin.ModelAdmin):
    ''' Admin view for Tasks'''
    list_display = ("title", "author", "status")
    # creates wrappers for the read-only fields, so they can be in fieldsets
    readonly_fields = (
        'created', 'updated')

    @admin.display(description="Created")
    def created(self, instance):
        return instance.created_on

    @admin.display(description="Modified")
    def updated(self, instance):
        return instance.updated_on

    @admin.display(description="starts")
    def starts(self, instance):
        return instance.starts_on

    @admin.display(description="ends")
    def ends(self, instance):
        return instance.ends_on

    # organize the list fields of Task
    list_display = ('created', 'title', 'author', 'starts', 'ends', 'priority', 'status')
    list_display_links = ('title',)
    search_fields = ('title', 'details',)
    list_filter = (
        ('status', 'created_on', 'author', 'status')
    )

    # Allows the user to togle Things between Draft and Published states
    actions = ['Pending', 'Completed', 'Cancelled']

    def Pending(self, request, queryset):
        queryset.update(status=0)

    def Completed(self, request, queryset):
        queryset.update(status=1)

    def Cancelled(self, request, queryset):
        queryset.update(status=2)

    # organize the admin form fields for editting details
    fieldsets = (
        ('Tasks', {
            'fields': (
                ('author', 'title'),
                ('status', 'priority'),
                ( 'starts_on', 'ends_on'),
                ('details',),
            ),
        }),
    )


# admin.site.register(Task_mgr_User, Task_mgr_UserAdmin)
