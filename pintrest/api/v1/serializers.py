from rest_framework import serializers
from pintrest.models import Movie, Cast, Category, Seires



class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class SeiresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seires
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

