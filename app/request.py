from app import app
import urllib.request,json
from .models import newss
Newss = newss.Newss 

api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]
  
def get_newss(source):
  get_newss_url=base_url.format(source,api_key)
  
  with urllib.request.urlopen(get_newss_url) as url:
    get_newss_data=url.read()
    get_newss_res=json.loads(get_newss_data)
    newss_results = None
    
    if get_newss_res['articles']:
      newss_results_list=get_newss_res['articles']
      newss_results=process_results(newss_results_list)

  return newss_results     


def process_results(newss_list):

  newss_results=[]
  for newss_item in newss_list:
    urlToImage=newss_item.get('urlToImage')
    title=newss_item.get('title')
    description=newss_item.get('description')
    url=newss_item.get('url')
    time=newss_item.get('publishedAt')
    content=newss_item.get('content')


    if urlToImage:
      newss_object=Newss(urlToImage,title,description,url,time,content)
      newss_results.append(newss_object)

  return newss_results



