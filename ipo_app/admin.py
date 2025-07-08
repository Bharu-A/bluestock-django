from django.contrib import admin
from .models import (
    IPO, Stat, NewsArticle, FAQ,
    Broker, Blog, CandlestickPattern,
    ChartPattern, JobOpening,
    ContactOption, MutualFund,
    Product, SharkInvestor,
    TechnicalIndicator, TechnicalLesson
)

# Custom Admin for IPO
@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'status', 'ipo_price', 'listing_price', 'current_market_price')
    list_filter = ('status',)
    search_fields = ('company_name',)

# Custom Admin for ChartPattern
@admin.register(ChartPattern)
class ChartPatternAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

# Custom Admin for ContactOption
@admin.register(ContactOption)
class ContactOptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

# Register all other models with default admin
admin.site.register(Stat)
admin.site.register(NewsArticle)
admin.site.register(FAQ)
admin.site.register(Broker)
admin.site.register(Blog)
admin.site.register(CandlestickPattern)
admin.site.register(JobOpening)
admin.site.register(MutualFund)
admin.site.register(Product)
admin.site.register(SharkInvestor)
admin.site.register(TechnicalIndicator)
admin.site.register(TechnicalLesson)
