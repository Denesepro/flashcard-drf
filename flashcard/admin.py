from django.contrib import admin
from .models import Flashcard
# Register your models here.

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer','created_at', 'updated_at',)

admin.site.register(Flashcard,FlashcardAdmin)