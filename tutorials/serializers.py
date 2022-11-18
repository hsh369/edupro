from rest_framework import serializers
from . models import Tutorial, Blog, Task, TaskAnswer, Comment, TutorialType
from rest_framework.serializers import HyperlinkedModelSerializer


class BlogSerializer(serializers.ModelSerializer, serializers.RelatedField):
    class Meta:
        model = Blog
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# Tutorial based serializers
class TutorialListSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='tutorial-detail-view', read_only=True, required=False)
    tasks_count = serializers.SerializerMethodField()
    blogs_count = serializers.SerializerMethodField()

    class Meta:
        model = Tutorial
        fields = ['pk','name', 'description', 'tasks_count',
                  'blogs_count', 'rank', 'price', 'last_modified', 'url']

    def get_tasks_count(self, obj):
        return Task.objects.filter(id=obj.id).count()

    def get_blogs_count(self, obj):
        return Blog.objects.filter(id=obj.id).count()

class TutorialDetailCreateSerializer(serializers.ModelSerializer):
    # choices = ChoiceSerializer(many=True, read_only=True, required=False)
    blogs = BlogSerializer(many=True, read_only=True, required=False)
    tasks = TaskSerializer(many=True, read_only=True,required=False)

    class Meta:
        model = Tutorial
        fields = ['pk','name','description','price','last_modified','blogs','tasks',]

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
            raise serializers.ValidationError(
                'Rating has to be between 1 and 10.')
        return value

class TutorialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorialType
        fields = '__all__'


