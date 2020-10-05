from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bug_trackerapp.models import Ticket, My_User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'company',
                ),
            },
        ),
    )

admin.site.register(My_User)

admin.site.register(Ticket)

