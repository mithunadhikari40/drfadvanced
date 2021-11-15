from django.contrib import admin
from .models import Deck


class DeckAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "last_reviewed_date",
        "created_at",
        "updated_at",
    ]
    # Can do this way too,
    # list_display = "__all__"


admin.site.register(Deck, DeckAdmin)
