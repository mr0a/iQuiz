from django.contrib import admin
from .models import Quiz, Question, QuizSettings
from django.contrib.admin.models import LogEntry
admin.site.register(LogEntry)

# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizSettings)
admin.site.register(Question)
