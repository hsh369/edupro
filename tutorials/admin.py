from django.contrib import admin
from . models import Tutorial,Blog,Task,TaskAnswer,Comment,TutorialType


class CommentInline(admin.TabularInline):
    model = Comment
    

# Register your models here with some advanced configurations
@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('name','user_id','rank', 'price', 'last_modified')
    list_filter = ('rank', 'price', 'last_modified')
    inlines = [CommentInline]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('tutorial_id','name', 'last_modified')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('tutorial_id','question')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =('tutorial_id','comment','rank','publish_date')

@admin.register(TaskAnswer)
class TaskAnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(TutorialType)
class TutorialTypeAdmin(admin.ModelAdmin):
    pass