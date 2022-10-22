import imp
from rest_framework import serializers
from . models import Tutorial,Blog,Task,TaskAnswer,Comment,TutorialType


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TutorialSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # choices = ChoiceSerializer(many=True, read_only=True, required=False)
    blogs = BlogSerializer(many=True, read_only=True, required=False)
    tasks = TaskSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Tutorial
        fields = '__all__' 



class TaskAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAnswer
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    
    def validate_rank(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError('Rating has to be between 1 and 10.')
        return value

class TutorialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialType
        fields = '__all__'
        