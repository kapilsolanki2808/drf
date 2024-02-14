from .models import Comment

from rest_framework.response import Response
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


class BlogPostSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def validate_content(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        else:
            return Response("django is exist")


    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
            







########################################### MODEL SERIALIZER ###################################
# from django.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'profile']

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         user = User.objects.create(**validated_data)
#         Profile.objects.create(user=user, **profile_data)
#         return user










# {
# "email":"kapil@gmail.com",
# "content":"hello",
# "created":"2024-10-10"
# }
    

