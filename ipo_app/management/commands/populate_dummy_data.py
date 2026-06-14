import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ipo_app.models import (
    Stat, NewsArticle, FAQ, IPO, Broker, Blog,
    CandlestickPattern, ChartPattern, ContactOption,
    JobOpening, MutualFund, Product, SharkInvestor,
    TechnicalIndicator, TechnicalLesson, MediaItem, CommunityPost
)

class Command(BaseCommand):
    help = "Populate the database with realistic dummy data for testing the application."

    def handle(self, *args, **options):
        self.stdout.write("Populating dummy data...")

        # 1. Create a superuser / dummy user if not exists
        user, created = User.objects.get_or_create(
            username="admin@bluestock.in",
            defaults={
                "email": "admin@bluestock.in",
                "first_name": "Bluestock Admin",
                "is_staff": True,
                "is_superuser": True
            }
        )
        if created:
            user.set_password("admin123")
            user.save()
            self.stdout.write("Created superuser: admin@bluestock.in (password: admin123)")

        # 2. Populate Brokers
        brokers_data = [
            {
                "name": "Zerodha",
                "rating": 4.8,
                "account_opening_charge": "₹200",
                "amc": "₹300/year",
                "delivery_charge": "₹0 (Free)",
                "intraday_charge": "Flat ₹20 or 0.03%",
                "ease_of_use": 5,
                "customer_support": 4,
                "pros": "Kite platform is extremely clean. No delivery charges. Direct mutual funds.",
                "cons": "No trading tips. Call and trade costs extra. Charting can sometimes lag.",
                "logo_url": "/static/images/zerodha.png",
                "features": ["Kite App", "Console Reports", "Sentinel Alerts", "Coin Mutual Funds"]
            },
            {
                "name": "Groww",
                "rating": 4.6,
                "account_opening_charge": "₹0 (Free)",
                "amc": "₹0 (Free)",
                "delivery_charge": "Flat ₹20 or 0.05%",
                "intraday_charge": "Flat ₹20 or 0.05%",
                "ease_of_use": 5,
                "customer_support": 4,
                "pros": "Zero account opening and AMC. Very simple interface for beginners.",
                "cons": "Customer support can be slow. Advanced charting features are limited.",
                "logo_url": "/static/images/groww.webp",
                "features": ["Simple UI", "Direct Mutual Funds", "US Stocks", "Gold Investment"]
            },
            {
                "name": "Angel One",
                "rating": 4.5,
                "account_opening_charge": "₹0 (Free)",
                "amc": "₹240/year",
                "delivery_charge": "₹0 (Free)",
                "intraday_charge": "Flat ₹20 or 0.25%",
                "ease_of_use": 4,
                "customer_support": 5,
                "pros": "Provides daily research reports and recommendations. Wide network of branches.",
                "cons": "AMC is charged from the first year. UI can be complex for beginners.",
                "logo_url": "/static/images/AngelOne.png",
                "features": ["ARQ Advisory", "SmartAPI", "Margin Funding", "Portfolio Analyzer"]
            },
            {
                "name": "Upstox",
                "rating": 4.4,
                "account_opening_charge": "₹0 (Free)",
                "amc": "₹150/year",
                "delivery_charge": "Flat ₹20 or 0.1%",
                "intraday_charge": "Flat ₹20 or 0.05%",
                "ease_of_use": 4,
                "customer_support": 4,
                "pros": "Backed by Ratan Tata. Powerful Pro platform. High leverage available.",
                "cons": "Delivery is not completely free. Call and trade charges apply.",
                "logo_url": "/static/images/upstox.png",
                "features": ["Pro Web & Mobile", "TradingView integration", "Option Chain Analysis"]
            }
        ]

        for b in brokers_data:
            Broker.objects.update_or_create(name=b["name"], defaults=b)
        self.stdout.write(f"Populated {len(brokers_data)} brokers.")

        # 3. Populate IPOs
        today = datetime.date.today()
        ipos_data = [
            {
                "company_name": "Ola Electric Mobility Ltd",
                "logo": "logos/ola.png",
                "price_band": "₹72 - ₹76",
                "open_date": today - datetime.timedelta(days=2),
                "close_date": today + datetime.timedelta(days=2),
                "issue_size": "₹6,145 Cr",
                "issue_type": "Book Built",
                "status": "ongoing",
                "ipo_price": 76.0,
                "current_market_price": 78.5
            },
            {
                "company_name": "FirstCry (Brainbees Solutions Ltd)",
                "logo": "logos/firstcry.png",
                "price_band": "₹440 - ₹465",
                "open_date": today + datetime.timedelta(days=5),
                "close_date": today + datetime.timedelta(days=8),
                "issue_size": "₹4,193 Cr",
                "issue_type": "Book Built",
                "status": "upcoming"
            },
            {
                "company_name": "Tata Technologies Ltd",
                "logo": "logos/tatatech.png",
                "price_band": "₹475 - ₹500",
                "open_date": today - datetime.timedelta(days=200),
                "close_date": today - datetime.timedelta(days=197),
                "issue_size": "₹3,042 Cr",
                "issue_type": "Book Built",
                "listing_date": today - datetime.timedelta(days=190),
                "status": "listed",
                "ipo_price": 500.0,
                "listing_price": 1200.0,
                "current_market_price": 1050.0
            },
            {
                "company_name": "IdeaForge Technology Ltd",
                "logo": "logos/ideaforge.png",
                "price_band": "₹638 - ₹672",
                "open_date": today - datetime.timedelta(days=300),
                "close_date": today - datetime.timedelta(days=297),
                "issue_size": "₹567 Cr",
                "issue_type": "Book Built",
                "listing_date": today - datetime.timedelta(days=290),
                "status": "listed",
                "ipo_price": 672.0,
                "listing_price": 1300.0,
                "current_market_price": 810.0
            }
        ]

        for ipo in ipos_data:
            IPO.objects.get_or_create(company_name=ipo["company_name"], defaults=ipo)
        self.stdout.write(f"Populated {len(ipos_data)} IPOs.")

        # 4. Populate Products
        products_data = [
            {"title": "Bluestock Web", "description": "Trade and analyze directly from your desktop browser.", "color": "#4a00e0", "section": "platforms"},
            {"title": "Bluestock Mobile App", "description": "Powerful charting and instant execution on the go.", "color": "#00f2fe", "section": "platforms"},
            {"title": "Bluestock API", "description": "Integrate real-time stock feeds into your custom apps.", "color": "#f107a3", "section": "platforms"},
            {"title": "Trader Network", "description": "Share portfolios, copy-trade experts, and chat in real-time.", "color": "#00f2fe", "section": "network"},
            {"title": "Market Screener", "description": "Scan 5000+ stocks using 100+ technical indicators.", "color": "#4a00e0", "section": "powerful"},
        ]
        for prod in products_data:
            Product.objects.get_or_create(title=prod["title"], defaults=prod)

        # 5. Populate Shark Investors
        sharks_data = [
            {"name": "Aman Gupta", "description": "Co-founder and CMO of boAt. Passionate about consumer tech brands and marketing strategies."},
            {"name": "Peyush Bansal", "description": "Founder and CEO of Lenskart. Focused on tech-driven solutions and scaling operations."},
            {"name": "Namita Thapar", "description": "Executive Director of Emcure Pharmaceuticals. Investor in healthcare and wellness startups."}
        ]
        for shark in sharks_data:
            SharkInvestor.objects.get_or_create(name=shark["name"], defaults=shark)

        # 6. Populate Mutual Funds
        funds_data = [
            {
                "name": "SBI Bluechip Fund",
                "category": "Large Cap",
                "aum": "₹43,500 Cr",
                "expense_ratio": "0.9%",
                "cagr_5y": "15.4%",
                "performance": "Consistently outperformed its benchmark index (Nifty 50 TRI) over 3, 5, and 7-year horizons.",
                "risk": "Moderate-high risk profile, typical of equity funds focused on bluechip corporations.",
                "composition": "Financial Services (28%), IT (15%), Energy (12%), Consumer Goods (10%)"
            },
            {
                "name": "HDFC Top 100 Fund",
                "category": "Large Cap",
                "aum": "₹32,100 Cr",
                "expense_ratio": "1.1%",
                "cagr_5y": "14.8%",
                "performance": "Strong performance history, particularly during market recovery phases.",
                "risk": "Moderate risk, holds highly liquid shares of India's top 100 companies.",
                "composition": "Banking (31%), Technology (14%), Oil & Gas (11%), Automobile (9%)"
            }
        ]
        for fund in funds_data:
            MutualFund.objects.get_or_create(name=fund["name"], defaults=fund)

        # 7. Populate Technical Indicators
        indicators_data = [
            {"title": "Relative Strength Index (RSI)", "content": "RSI is a momentum oscillator that measures the speed and change of price movements between 0 and 100. Traditionally, values over 70 indicate overbought conditions, and values below 30 indicate oversold conditions.", "order": 1},
            {"title": "MACD (Moving Average Convergence Divergence)", "content": "MACD is a trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. Crossovers are used to signal buy and sell opportunities.", "order": 2},
            {"title": "Bollinger Bands", "content": "Bollinger Bands consist of a middle band (SMA) and two outer bands (standard deviations). They help identify high and low volatility and potential price breakouts.", "order": 3}
        ]
        for ind in indicators_data:
            TechnicalIndicator.objects.get_or_create(title=ind["title"], defaults=ind)

        # 8. Populate Chart Patterns
        patterns_data = [
            {"title": "Head and Shoulders", "description": "A reversal pattern that indicates a transition from a bullish trend to a bearish trend, characterized by three peaks.", "order": 1},
            {"title": "Double Bottom", "description": "A bullish reversal pattern that describes the rise of a stock, a drop, another rise to the same level, and a final breakthrough.", "order": 2}
        ]
        for pat in patterns_data:
            ChartPattern.objects.get_or_create(title=pat["title"], defaults=pat)

        # 9. Populate Candlestick Patterns
        candles_data = [
            {"title": "Hammer", "description": "A bullish reversal pattern that forms during a downtrend. It has a small body at the top and a long lower shadow."},
            {"title": "Doji", "description": "Indicates indecision between buyers and sellers where the opening and closing prices are virtually equal."}
        ]
        for candle in candles_data:
            CandlestickPattern.objects.get_or_create(title=candle["title"], defaults=candle)

        # 10. Populate Blogs
        blogs_data = [
            {"title": "How to Analyze an IPO: A Beginner's Guide", "content": "Analyzing an IPO requires reading the DRHP, looking at financial health, evaluating promoters, and checking the valuation...", "image_url": "https://picsum.photos/400/250", "read_time": "6 min read"},
            {"title": "Understanding Support and Resistance in Charts", "content": "Support and resistance are key concepts in technical analysis. Support acts as a floor, while resistance acts as a ceiling...", "image_url": "https://picsum.photos/400/251", "read_time": "4 min read"}
        ]
        for blog in blogs_data:
            Blog.objects.get_or_create(title=blog["title"], defaults=blog)

        # 11. Populate Job Openings
        jobs_data = [
            {"role": "Backend Django Developer", "location": "Bangalore / Remote", "apply_link": "https://bluestock.in/careers/django"},
            {"role": "Frontend React Developer", "location": "Mumbai / Hybrid", "apply_link": "https://bluestock.in/careers/react"}
        ]
        for job in jobs_data:
            JobOpening.objects.get_or_create(role=job["role"], defaults=job)

        # 12. Populate Contact Options
        contacts_data = [
            {"title": "Support Desk", "description": "Get help with your account or general inquiries.", "icon": "bi-chat-dots", "link": "mailto:support@bluestock.in"},
            {"title": "Business Relations", "description": "Collaborate with our broker network team.", "icon": "bi-briefcase", "link": "mailto:partners@bluestock.in"}
        ]
        for contact in contacts_data:
            ContactOption.objects.get_or_create(title=contact["title"], defaults=contact)

        # 13. Populate Community Posts
        posts_data = [
            {"author": user, "title": "Which broker has the best API platform?", "content": "I am looking to automate my trades using Python. Zerodha's Kite Connect seems good but is paid. Angel One is free. Any recommendations?"},
            {"author": user, "title": "Tata Technologies IPO Listing Gain discussion", "content": "Tata Tech listed at 140% gain! Anyone still holding or did you book profit on day one?"}
        ]
        for post in posts_data:
            CommunityPost.objects.get_or_create(title=post["title"], defaults=post)

        self.stdout.write(self.style.SUCCESS("Successfully populated all dummy data!"))
