from rest_framework import serializers
from .models import (
    Stat, NewsArticle, FAQ, IPO, Broker, Blog,
    CandlestickPattern, ChartPattern, ContactOption,
    JobOpening, MutualFund, Product, SharkInvestor,
    TechnicalIndicator, TechnicalLesson, MediaItem, CommunityPost
)

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class IPOSerializer(serializers.ModelSerializer):
    listing_gain = serializers.ReadOnlyField()
    current_return = serializers.ReadOnlyField()

    class Meta:
        model = IPO
        fields = '__all__'

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CandlestickPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandlestickPattern
        fields = '__all__'

class ChartPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartPattern
        fields = '__all__'

class ContactOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactOption
        fields = '__all__'

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'

class MutualFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualFund
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SharkInvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharkInvestor
        fields = '__all__'

class TechnicalIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalIndicator
        fields = '__all__'

class TechnicalLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalLesson
        fields = '__all__'

class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = '__all__'

class CommunityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityPost
        fields = '__all__'