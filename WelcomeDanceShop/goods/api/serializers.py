from rest_framework import serializers
from goods.models import Goods, Rubric


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'title', 'price', 'rubric']



