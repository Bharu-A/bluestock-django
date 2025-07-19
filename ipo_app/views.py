from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .models import (
    Stat, NewsArticle, FAQ, IPO, Broker, Blog,
    CandlestickPattern, ChartPattern, ContactOption,
    JobOpening, MutualFund, Product, SharkInvestor,
    TechnicalIndicator, TechnicalLesson
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
    return render(request, 'Home.html')

def about_us(request):
    return render(request, 'About_us.html')

def all_brokers(request):
    return render(request, 'AllBroker.html')


def blogs_page(request):
    return render(request, 'Blog.html')

def compare_brokers(request):
    return render(request, 'BrokerComparison.html')

def community_view(request):
    return render(request, 'Community.html')

def careers_page(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        print("Received contact info:", contact)
    return render(request, "Careers.html")

def careers_view(request):
    jobs = JobOpening.objects.all()
    return render(request, 'Careers.html', {'jobs': jobs})

def chart_patterns(request):
    patterns = ChartPattern.objects.all().order_by('order')
    return render(request, 'ChartPatterns.html', {'patterns': patterns})

def candlestick_chart(request):
    patterns = CandlestickPattern.objects.all()
    return render(request, 'candlestick.html', {'patterns': patterns})

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

def products_view(request):
    return render(request, 'Products.html', {
        "platforms": [
            {"title": "Bluestock IPO", "description": "Apply for IPOs and FPOs listed on NSE and BSE."},
            {"title": "Trading Terminal", "description": "A modern desktop trading app for fast execution."},
            {"title": "Mobile App", "description": "Trade from anywhere with our user-friendly app."},
        ],
        "network": [
            {"description": "Join our expert-led webinars and community chats."},
            {"description": "Share strategies and grow together as a trader."},
            {"description": "Get real-time tips and market insights."},
        ],
        "powerful": [
            {"title": "Open APIs", "description": "Use our APIs to build your own tools."},
            {"title": "Custom Dashboards", "description": "Personalize your trading experience."},
            {"title": "Algo Trading", "description": "Integrate your own trading bots."},
        ]
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

from .models import LoginLog  # ✅ Must be at the top

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            # ✅ Add this line to save login time
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
from django.shortcuts import render


from django.shortcuts import render

def home_view(request):
    return render(request, 'Home.html') 
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Already import these if not present
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            return render(request, 'Signup.html', {'error': 'Email already exists'})
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        login(request, user)
        return redirect('home')
    return render(request, 'Signup.html')
from django.shortcuts import render


from django.shortcuts import render
from .models import MediaItem

def media_view(request):
    media_items = MediaItem.objects.all().order_by('-created_at')
    return render(request, 'Media.html', {'media_items': media_items})
from django.shortcuts import render
from .models import CommunityPost

def community(request):
    posts = CommunityPost.objects.order_by('-created_at')
    return render(request, 'Community.html', {'posts': posts})
def community(request):
    return render(request, 'Community.html')

from django.shortcuts import render
import requests

def home(request):
    API_KEY = 'YOUR_API_KEY'
    symbol_list = ['RELIANCE.BSE', 'TCS.BSE', 'INFY.BSE']  # add more if needed

    high_data = []
    low_data = []

    for symbol in symbol_list:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
        res = requests.get(url).json()

        try:
            latest_day = list(res['Time Series (Daily)'].keys())[0]
            data = res['Time Series (Daily)'][latest_day]

            high = float(data['2. high'])
            low = float(data['3. low'])
            close = float(data['4. close'])

            high_data.append({'symbol': symbol, 'price': close, 'high': high})
            low_data.append({'symbol': symbol, 'price': close, 'low': low})
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")

    return render(request, 'home.html', {
        'high_data': high_data,
        'low_data': low_data
    })
from django.templatetags.static import static

def home(request):
    brokers = Broker.objects.all()
    brokers_data = {broker.name: broker.logo_url or "" for broker in brokers}
    return render(request, "home.html", {
        "brokers": brokers,
        "brokers_data": brokers_data,
    })


from django.shortcuts import render
from .models import IPOModel
from datetime import date

def ipo_home(request):
    today = date.today()
    upcoming_ipos = IPOModel.objects.filter(open_date__gt=today)
    ongoing_ipos = IPOModel.objects.filter(open_date__lte=today, close_date__gte=today)
    return render(request, "IPOHome.html", {
        "upcoming_ipos": upcoming_ipos,
        "ongoing_ipos": ongoing_ipos
    })
from .models import MutualFund

def large_cap_funds_view(request):
    funds = MutualFund.objects.filter(category='Large Cap')
    return render(request, 'MutualFunds.html', {'funds': funds})


def products_view(request):
    funds = MutualFund.objects.all()
    return render(request, 'Products.html', {'funds': funds})
from django.shortcuts import render

def ipo_home_view(request):
    return render(request, 'IPOHome.html')  # create a template if needed
