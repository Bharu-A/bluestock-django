from django.db import models
from django.contrib.auth.models import User

class IPO(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('listed', 'Listed'),
    ]
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    price_band = models.CharField(max_length=100)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    listing_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ipo_price = models.FloatField(null=True, blank=True)
    listing_price = models.FloatField(null=True, blank=True)
    current_market_price = models.FloatField(null=True, blank=True)
    rhp_pdf = models.FileField(upload_to='docs/', null=True, blank=True)
    drhp_pdf = models.FileField(upload_to='docs/', null=True, blank=True)

    @property
    def listing_gain(self):
        if self.ipo_price and self.listing_price:
            return round(((self.listing_price - self.ipo_price) / self.ipo_price) * 100, 2)
        return None

    @property
    def current_return(self):
        if self.ipo_price and self.current_market_price:
            return round(((self.current_market_price - self.ipo_price) / self.ipo_price) * 100, 2)
        return None

    def __str__(self):
        return self.company_name

class Stat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class NewsArticle(models.Model):
    source = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.source

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Broker(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    account_opening_charge = models.CharField(max_length=50, blank=True, null=True)
    amc = models.CharField(max_length=50)
    delivery_charge = models.CharField(max_length=50, blank=True, null=True)
    intraday_charge = models.CharField(max_length=50, blank=True, null=True)
    ease_of_use = models.IntegerField(default=0)
    customer_support = models.IntegerField(default=0)
    pros = models.TextField(blank=True, null=True)
    cons = models.TextField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    features = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(blank=True)
    published_date = models.DateField(auto_now_add=True)
    read_time = models.CharField(max_length=20, default="5 min read")

    def __str__(self):
        return self.title

class CandlestickPattern(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='candlestick_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class ChartPattern(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='patterns/', null=True, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class JobOpening(models.Model):
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_on = models.DateField(auto_now_add=True)
    apply_link = models.URLField()

    def __str__(self):
        return self.role

class ContactOption(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class MutualFund(models.Model):
    CATEGORY_CHOICES = [
        ('Large Cap', 'Large Cap'),
        ('Mid Cap', 'Mid Cap'),
        ('Debt', 'Debt'),
        ('Hybrid', 'Hybrid'),
    ]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    aum = models.CharField(max_length=100)
    expense_ratio = models.CharField(max_length=50)
    cagr_5y = models.CharField(max_length=50)
    performance = models.TextField()
    risk = models.TextField()
    composition = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=20, default='#ffffff')
    section = models.CharField(max_length=100, choices=[
        ('platforms', 'Platforms'),
        ('network', 'Network'),
        ('powerful', 'Powerful Platform'),
    ])

class SharkInvestor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='investors/')
    description = models.TextField()

    def __str__(self):
        return self.name

class TechnicalIndicator(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='technical_indicators/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class TechnicalLesson(models.Model):
    title = models.CharField(max_length=255)
    views = models.PositiveIntegerField(default=0)
    image = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"

class MediaItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    media_type = models.CharField(max_length=50, choices=[('video', 'Video'), ('article', 'Article')])
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
