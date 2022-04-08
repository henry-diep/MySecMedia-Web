from django.http import HttpResponse
from django.http  import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
import feedparser

from .models import NewsItem
from .models import Feedmodel

from django.views.generic.list import ListView

from datetime import datetime, timezone



class NewsItemListView(ListView):
    model = NewsItem
    template_name = "newsitem_list.html"

class RSSList(ListView):

    model = Feedmodel   
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        qs = super(RSSList, self).get_queryset(*args, **kwargs)
        #qs = qs.order_by("-publish_date") #old code
        qs = qs.order_by("-Date_Received")
        return qs

class news_content(ListView):

    # model = Feedmodel   
    # paginate_by = 20

    def get_content():
        news = Feedmodel.objects.all()
        return news
    

feed_urls = {
    'acsm':'https://australiancybersecuritymagazine.com.au/feed/',
    'asm':'https://australiansecuritymagazine.com.au/feed/',
    'apsm':'https://www.asiapacificsecuritymagazine.com/feed/',
    'cctv':'https://cctvbuyersguide.com/feed/',
    'space':'https://spaceanddefense.io/feed/',
    'crl':'https://cyberriskleaders.com/feed/',
    'chiefit':'https://chiefit.me/feed/',
    'smartcities':'https://smartcitiestech.io/feed/',
    'drastic':'https://drasticnews.com/feed/',
    'asean':'https://aseantechsec.com/feed/',
}

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    text = text.replace('&amp;','&')
    text = text.replace('&#8217;',"'")
    text = text.replace('?&nbsp', ' ')
    return re.sub(clean, '', text)

def load(request):
    #Feedmodel.objects.all().delete() #old code
    list_rssfeed_entry = []
    #d = datetime.date(1997, 10, 19)

    for url in feed_urls.keys():
        feed = feedparser.parse(feed_urls[url])
        for entry in feed['entries']:
            data = Feedmodel()
            data.title_name = entry['title']
            data.url_link = entry['link']
            data.feed_site_url = 'https://www.'+entry['link'].split('/')[2]
            
            data.feed_site = feed.feed.title 
            dt_string = entry['published']
            d = datetime.strptime(dt_string, "%a, %d %b %Y %H:%M:%S +%f")
            now = datetime.today().strftime("%d %b %Y %H:%M:%S +%f")
            data.load_datetime = datetime.strptime(now, "%d %b %Y %H:%M:%S +%f")
            data.publish_date = d
            data.description = remove_html_tags(entry['description'])
            data.save()
            
            
        
        all_data = Feedmodel.objects.order_by('-publish_date')         
            
        list_rssfeed_entry.append(feed)

        # feeds are saved to the database
        # now need to load feeds from the database
        # allow caching
        # view sort by publish date 

    #return render(request, 'load.html')
    return HttpResponseRedirect('/')


def msmall(request):
    
    #Feedmodel.objects.all().delete()
    list_rssfeed_entry = []
    #d = datetime.date(1997, 10, 19)

    for url in feed_urls.keys():
        feed = feedparser.parse(feed_urls[url])
        for entry in feed['entries']:
            data = Feedmodel()
            data.title_name = entry['title']
            data.url_link = entry['link']
            
            data.feed_site = feed.feed.title 
            dt_string = entry['published']
            d = datetime.strptime(dt_string, "%a, %d %b %Y %H:%M:%S +%f")
            now = datetime.today().strftime("%d %b %Y %H:%M:%S +%f")
            data.load_datetime = datetime.strptime(now, "%d %b %Y %H:%M:%S +%f")
            data.publish_date = d
            data.description = remove_html_tags(entry['description'])
            data.save()                            
        all_data = Feedmodel.objects.order_by('-publish_date')                    
        list_rssfeed_entry.append(feed)

        # feeds are saved to the database
        # now need to load feeds from the database
        # allow caching
        # view sort by publish date 
    return render(request, 'test.html', {'list_rssfeed_entry' : list_rssfeed_entry,})

def newsletter(request):
    news = Feedmodel.objects.all() #not working
    return render(request, 'hello/newsletter.html', {'newsletter': news})

def hello(request):
    return HttpResponse("Hello, Azure!")

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def rss(request):
    """ if request.GET.get("url"):
        url = request.GET["url"] #Getting URL
        feed = feedparser.parse(url) #Parsing XML data
    else:
        feed = None """
    
    bbc = 'http://feeds.bbci.co.uk/news/rss.xml'
    feed = feedparser.parse(bbc)
    return render(request, 'rss.html', {'feed' : feed,})

def acsm(request):    
    feed = feedparser.parse(feed_urls['acsm'])
    return render(request, 'rss.html', {'feed' : feed,})


def asm(request):
    feed = feedparser.parse(feed_urls['asm'])
    return render(request, 'rss.html', {'feed' : feed,})

def apsm(request):    
    feed = feedparser.parse(feed_urls['apsm'])
    return render(request, 'rss.html', {'feed' : feed,})

#cctv
def cctv_view(request):
    feed = feedparser.parse(feed_urls['cctv'])
    return render(request, 'rss.html', {'feed' : feed,})

#space&defence
def space_view(request):    
    feed = feedparser.parse(feed_urls['space'])
    return render(request, 'rss.html', {'feed' : feed,})

#crl
def crl_view(request):    
    feed = feedparser.parse(feed_urls['crl'])
    return render(request, 'rss.html', {'feed' : feed,})

#chiefit
def chiefit_view(request):    
    feed = feedparser.parse(feed_urls['chiefit'])
    return render(request, 'rss.html', {'feed' : feed,})

#smartcities
def smartcities_view(request):    
    feed = feedparser.parse(feed_urls['smartcities'])
    return render(request, 'rss.html', {'feed' : feed,})

#drastic
def drastic_view(request):
    feed = feedparser.parse(feed_urls['drastic'])
    return render(request, 'rss.html', {'feed' : feed,})

#asean
def asean_view(request):    
    feed = feedparser.parse(feed_urls['asean'])
    return render(request, 'rss.html', {'feed' : feed,})

def test_view(request):    
    feed = feedparser.parse(feed_urls['asean'])

    return render(request, 'rss.html', {'feed' : feed,})

from django.shortcuts   import redirect

def optout(request):
    
    return HttpResponse('http://google.com')

    # Define function to handle request and response
def year_archive(request):
    path = request.path
    method = request.method
    userAgent = request.META['HTTP_USER_AGENT']
    full_path = request.get_full_path()
    full_uri = request.build_absolute_uri()
    val = request.GET.get('channel_url')
    # request is handled using HttpResponse object
    return redirect(val)
'''
    return HttpResponse("<center><h1>Testing Django Request Response Cycle</h1><br/>"
                        "<p>Request path : " + val +
                        "</p>Request Method : " + method +
                        "<p>full paths Agent : " + full_path + "</p></center>")
'''