from django.contrib import admin
from quora_app import models

# Register your models here.
@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'visable', 'updated_at')

@admin.register(models.Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'visable', 'updated_at')

@admin.register(models.Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'author', 'updated_at')