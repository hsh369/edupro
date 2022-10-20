import imp
from rest_framework import serializers
from . models import Tutorial,Blog,Task,Answer,Comment,TutorialType


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    # choices = ChoiceSerializer(many=True, read_only=True, required=False)
    blogs = BlogSerializer(many=True, read_only=True, required=False)
    tasks = TaskSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Tutorial
        fields = '__all__'



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TutorialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialType
        fields = '__all__'
        