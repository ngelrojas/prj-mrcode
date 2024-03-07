from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["user", "location", "birth_date"]
    list_filter = []
    fieldsets = (
        (None, {"fields": (
            "user",
            "bio",
            "location",
            "birth_date",
            "photo",
            "sn_facebook",
            "sn_twitter",
            "sn_linkedin",
            "sn_instagram",
            "sn_github",
            "sn_youtube",
            "sn_website",
        )}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("user", "bio", "location", "birth_date", "photo")}),
    )