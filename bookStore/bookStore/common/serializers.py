from rest_framework import serializers

from bookStore.common.models import BookReview


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = BookReview
        fields = ['id', 'user', 'title', 'content', 'created_at']
