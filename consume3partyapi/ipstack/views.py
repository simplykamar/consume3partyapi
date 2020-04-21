from django.shortcuts import render
import requests
# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
	if request.method =='POST':
		target_ip=request.POST['target_ip']
		url="http://api.ipstack.com/"+str(target_ip)+"?access_key=78a577413a35d789781f4c013ff762b2"
		response=requests.get(url)
		status_code=response.status_code
		py_data=response.json()
		return render(request,"ipstack/index.html",{"status_code":status_code,"data":py_data})
	return render(request,"ipstack/index.html")
	