from rest_framework import serializers
from . import models


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('id', 'name', 'description')


class ClubRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClubRole
        fields = ('id', 'name', 'description', 'club')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id', 'name', 'description', 'started', 'closed', 'leader', 'members', 'clubs')


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Channel
        fields = ('id', 'name', 'description', 'club')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'content', 'created', 'channel')


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conversation
        fields = ('id', 'content', 'created', 'channel', 'author', 'parent')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ('id', 'content', 'created', 'club', 'author')


class FeedbackReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedbackReply
        fields = ('id', 'content', 'created', 'parent')
