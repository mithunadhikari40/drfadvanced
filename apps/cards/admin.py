from django.contrib import admin
from .models import Card, Buckets


class CardAdmin(admin.ModelAdmin):
    list_display = [
        "deck",
        "question",
        "answer",
        "bucket",
        "next_review_date",
        "last_reviewed_date",
        "created_at",
        "updated_at",
    ]


admin.site.register(Card, CardAdmin)
