from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
	email   = serializers.EmailField(max_length=128, required=True)
	content = serializers.CharField(max_length=256, required=True)

	class Meta:
		model = Comment
		fields = ['id', 'email', 'content', 'created']