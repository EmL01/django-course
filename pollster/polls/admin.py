from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin'
admin.site.index_title = 'Welcome to Pollster Admin'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['text'] })
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)