from app import app
import urllib.request,json
from .models import newss
Newss = newss.Newss 

api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]
  
def get_newss(sources):
  get_newss_url=base_url.format(sources,api_key)
  
  with urllib.request.urlopen(get_newss_url) as url:
    get_newss_data=url.read()
    get_newss_res=json.loads(get_newss_data)
    newss_results = None
    
    if get_newss_res['sources']:
      newss_results_list=get_newss_res['sources']
      newss_results=process_result(newss_results_list)

  return newss_results     

def process_result(newss_list):
  newss_results=[]

  for newss_item in newss_list:
    id=newss_item.get('id')
    name=newss_item.get('name')
    url=newss_item.get('url')
    

    if id:
      newss_object=Newss(id,name,url)
      newss_results.append(newss_object)

  return newss_results                           
