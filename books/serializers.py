from rest_framework import serializers
from .models import Book, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class NestedUserSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class CommentSerializer(serializers.ModelSerializer):
    ''' Serializer for Comments'''
    
    class Meta:
        model = Comment
        fields = '__all__'

class NestedCommentSerializer(serializers.ModelSerializer):
    ''' Serializer for Nested Comments'''
    owner = NestedUserSerilaizer()

    class Meta:
        model = Comment
        fields = '__all__'        

class BookSerializer(serializers.ModelSerializer):
    ''' Serializer for Book '''
    comments = NestedCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        