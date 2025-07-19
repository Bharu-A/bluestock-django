from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home, community, about_us, all_brokers, blog_list_view, blogs_page,
    compare_brokers, candlestick_chart, careers_page, chart_patterns,
    contact_us, products_page, products_view, large_cap_funds,
    shark_investors_view, stock_school, technical_indicators_view,
    technical_analysis_view, media_view, signup_view, login_view,
    logout_view, BrokerViewSet, large_cap_funds_view,products_view
)
from . import views
router = DefaultRouter()
router.register(r'brokers', BrokerViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('community/', community, name='community'),
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
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('ipo-home/', views.ipo_home, name='ipo_home'),
    path('large-cap/', large_cap_funds_view, name='large_cap_funds'),
    path('api/', include(router.urls)),
]

