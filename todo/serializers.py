# 전체 조회용 시리얼라이저. Todo 설명을 제외한 제목, 완료여부, 중요여부가 필요.
from rest_framework import serializers
from .models import Todo

class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created', 'complete', 'important')