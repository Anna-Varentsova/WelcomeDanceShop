from rest_framework import serializers
from articles.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    # скрытое поле для автоматической подставки текущего пользователя
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Articles
        fields = '__all__'

