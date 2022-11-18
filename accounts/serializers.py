from rest_framework import serializers
from .models import User
from tutorials.models import Tutorial

class UserSerializer(serializers.ModelSerializer):
    tutorials = serializers.PrimaryKeyRelatedField(many=True, queryset = Tutorial.objects.all())

    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email','username','password','image','first_name','last_name','phone_number','bio','bithdate')
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True},
        'password': {'write_only': True}
        }

class UserListSerializer(serializers.ModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail', read_only=True, required=False)
    tutorials_count = serializers.SerializerMethodField()
    rank = serializers.ReadOnlyField()
    class Meta: 
        model = User
        fields= ('id','url','image','username','first_name','last_name','rank','tutorials_count')
    
    def get_tutorials_count(self,obj):
        return Tutorial.objects.filter(id = obj.id).count()