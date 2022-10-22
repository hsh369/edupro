from dataclasses import field
from rest_framework import serializers
from .models import User
from tutorials.models import Tutorial

class UserSerializer(serializers.ModelSerializer):
    tutorials = serializers.PrimaryKeyRelatedField(many=True, queryset = Tutorial.objects.all())
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='user-detail',
    #     lookup_field='pk'
    # )
    class Meta:
        model = User
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['tutorials'] = instance

    #     return representation
