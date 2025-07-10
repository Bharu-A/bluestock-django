from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IPOViewSet, StatViewSet, NewsArticleViewSet, FAQViewSet,
    BrokerViewSet, BlogViewSet,
    all_brokers, blog_list_view, blogs_page,
    compare_brokers, candlestick_chart,
    careers_page, chart_patterns, contact_us,
    home, large_cap_funds, products_page,
    shark_investors_view, stock_school, 
    products_view, technical_indicators_view, technical_analysis_view,
    signup_view, login_view, logout_view, about_us, media_view,
    custom_404_view
)
from django.conf import settings
from django.conf.urls.static import static

# === API Router ===
router = DefaultRouter()
router.register(r'ipo', IPOViewSet)
router.register(r'stats', StatViewSet)
router.register(r'news', NewsArticleViewSet)
router.register(r'faqs', FAQViewSet)
router.register(r'brokers', BrokerViewSet)
router.register(r'blogs', BlogViewSet)

# === Combined urlpatterns ===
urlpatterns = [
    # API
    path('api/', include(router.urls)),

    # Auth
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Pages
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('brokers-page/', all_brokers, name='all-brokers'),
    path('blogs/', blog_list_view, name='blogs-list'),
    path('blogs-page/', blogs_page, name='blogs-page'),
    path('compare-brokers/', compare_brokers, name='compare-brokers'),
    path('candlestick/', candlestick_chart, name='candlestick'),
    path('careers/', careers_page, name='careers'),
    path('chart-patterns/', chart_patterns, name='chart-patterns'),
    path('contact-us/', contact_us, name='contact_us'),
    path('products/', products_page, name='products'),
    path('products-alt/', products_view, name='products_alt'),
    path('large-cap/', large_cap_funds, name='large_cap_funds'),
    path('shark-investors/', shark_investors_view, name='shark-investors'),
    path('stock-school/', stock_school, name='stock_school'),
    path('technical-indicators/', technical_indicators_view, name='technical_indicators'),
    path('technical-analysis/', technical_analysis_view, name='technical-analysis'),
    path('media/', media_view, name='media'),
    
]

# === Serve media files ===
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# === Custom 404 handler ===
handler404 = 'ipo_app.views.custom_404_view'
