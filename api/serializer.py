from rest_framework import serializers
from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Serializes a Question"""
    class Meta:
        model = Question
        fields = '__all__'