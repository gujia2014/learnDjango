from django.shortcuts import render
from books.models import Publisher
from django.http import (HttpResponse, HttpResponseNotFound,
    HttpResponseNotAllowed, HttpResponseForbidden)

# Create your views here.
def add_publisher(request):
	response = HttpResponse("add_publisher success")

	if request.method == 'GET':
		pName = request.REQUEST.get('name', '')
		pOrg = request.REQUEST.get('org','')
		tag = process_parameters(pName, pOrg)
		if tag < 0:
			return HttpResponse("name is null")
		else:
			publisher, created = Publisher.objects.get_or_create(name=pName, org=pOrg, defaults={'address':'tempAddress', 'city':'tempCity'})
		if created:
			print publisher.name
		else:
			print publisher.name
		return response

		#name = models.CharField(max_length=30)
		#address = models.CharField(max_length=50)
		#city = models.CharField(max_length=60)
		#state_province = models.CharField(max_length=30)
		#org = models.CharField(max_length=50, blank=True, null=True)
		#country = models.CharField(max_length=50)
		#website = models.URLField()

def process_parameters(name, org):
	if name == '':
		return -1
	else:
		return 0

 
def update_publisher(request):
	response = HttpResponse("update_publisher success")

	if request.method == 'GET':
		pName = request.REQUEST.get('name', '')
		if pName == '':
			return HttpResponse("The Publisher doesn't exist.")
		
		pOrg = request.REQUEST.get('org', '')
		if pOrg == '':
			return HttpResponse("URL doesn't have org field.")
		else:
			publisher = Publisher.objects.filter(name=pName).update(org=pOrg)
			#print publisher.address
			print publisher
			return response