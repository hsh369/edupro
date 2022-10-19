from django.contrib import admin
from . models import Tutorial,Blog,Task,Answer,Comment,TutorialType

# Register your models here.
admin.site.register(Tutorial)
admin.site.register(Blog)
admin.site.register(Task)
# admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(TutorialType)
