from django.contrib import admin
from .models import Card, Buckets


class CardAdmin(admin.ModelAdmin):
    list_display = [
        "deck",
        "question",
        "answer",
        "bucket",
        "next_review_date",
        "last_reviewed_date"
    ]


admin.site.register(Card, CardAdmin)
