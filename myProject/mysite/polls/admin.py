from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['questionText']}),
        ('Date information', {'fields': ['pubDate'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# Register your models here.
