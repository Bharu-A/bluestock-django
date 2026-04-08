from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import date

from .models import (
    Stat, NewsArticle, FAQ, IPO, Broker, Blog,
    CandlestickPattern, ChartPattern, ContactOption,
    JobOpening, MutualFund, Product, SharkInvestor,
    TechnicalIndicator, TechnicalLesson, LoginLog,
    MediaItem, CommunityPost
)
from .serializers import (
    StatSerializer, NewsArticleSerializer, FAQSerializer,
    IPOSerializer, BrokerSerializer, BlogSerializer
)

# === API ViewSets ===

class StatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class NewsArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

class BrokerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by('-published_date')
    serializer_class = BlogSerializer

# === Template Views ===

def home(request):
    brokers = Broker.objects.all()
    brokers_data = {broker.name: broker.logo_url or "" for broker in brokers}
    return render(request, "Home.html", {
        "brokers": brokers,
        "brokers_data": brokers_data,
    })

def about_us(request):
    return render(request, 'About_us.html')

def all_brokers(request):
    return render(request, 'AllBroker.html')

def blogs_page(request):
    return render(request, 'Blog.html')

def compare_brokers(request):
    return render(request, 'BrokerComparison.html')

def community(request):
    posts = CommunityPost.objects.order_by('-created_at')
    return render(request, 'Community.html', {'posts': posts})

def careers_page(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        print("Received contact info:", contact)
    jobs = JobOpening.objects.all()
    return render(request, "Careers.html", {'jobs': jobs})

def chart_patterns(request):
    patterns = ChartPattern.objects.all().order_by('order')
    return render(request, 'ChartPatterns.html', {'patterns': patterns})

def candlestick_chart(request):
    patterns = CandlestickPattern.objects.all()
    return render(request, 'CandleStick.html', {'patterns': patterns})

def contact_us(request):
    options = ContactOption.objects.all()
    return render(request, 'Contact.html', {'options': options})

def large_cap_funds(request):
    funds = MutualFund.objects.filter(category='Large Cap')
    return render(request, 'MutualFunds.html', {'funds': funds})

def products_page(request):
    products = Product.objects.all()
    return render(request, 'Products.html', {
        'platforms': products.filter(section='platforms'),
        'network': products.filter(section='network'),
        'powerful': products.filter(section='powerful')
    })



def shark_investors_view(request):
    investors = SharkInvestor.objects.all()
    return render(request, 'SharkInvestors.html', {'investors': investors})

def stock_school(request):
    return render(request, 'StockSchool.html')

def technical_indicators_view(request):
    indicators = TechnicalIndicator.objects.all().order_by('order')
    return render(request, 'TechnicalIndicators.html', {'indicators': indicators})

def technical_analysis_view(request):
    lessons = TechnicalLesson.objects.all()
    return render(request, 'TechnicalAnalysis.html', {'lessons': lessons})

def media_view(request):
    media_items = MediaItem.objects.all().order_by('-created_at')
    return render(request, 'Media.html', {'media_items': media_items})

def ipo_home(request):
    today = date.today()
    upcoming_ipos = IPO.objects.filter(open_date__gt=today)
    ongoing_ipos = IPO.objects.filter(open_date__lte=today, close_date__gte=today)
    listed_ipos = IPO.objects.filter(status='listed')
    return render(request, "IPOHome.html", {
        "upcoming_ipos": upcoming_ipos,
        "ongoing_ipos": ongoing_ipos,
        "listed_ipos": listed_ipos
    })

# === Blog API ===

def blog_list_view(request):
    blogs = Blog.objects.all().values("id", "title", "image_url", "published_date", "read_time")
    return JsonResponse(list(blogs), safe=False)

# === Auth Views ===

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            return render(request, 'Signup.html', {'error': 'Email already registered'})
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        login(request, user)
        return redirect('home')
    return render(request, 'Signup.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            LoginLog.objects.create(user=user)

            return redirect('home')
        else:
            return render(request, 'Login.html', {'error': 'Invalid credentials'})
    return render(request, 'Login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# === Custom 404 ===

def custom_404_view(request, exception):
    return render(request, "Error404.html", status=404)
