from django.shortcuts import render
import requests

# Create your views here.
def index(request):
  return render(request, 'top.html', {'keyword': ""})

def result(request):
  if request.method == 'POST':
    keyword = request.POST.get('keyword', '')
    api_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    app_id = ''
        
    params = {
      'format': 'json',
      'keyword': keyword,
      'applicationId': app_id,
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    items = data['Items']
  else:
    items = []
    keyword = ""
  return render(request, 'top.html', {'items': items, 'keyword': keyword})