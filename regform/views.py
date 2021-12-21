from django.shortcuts import render
from .models import student

def form(request,content = None):
	if request.method == 'POST':
		stid = request.POST.get('stid')
		password = request.POST.get('password')


		content = {'done':'Thank You For Your Registration.'}
		student.objects.create(stid=stid,password=password)




	return render(request,'index.html',content)


def showdata(request,content=None):

	data = student.objects.all()
	content = {'data':data,'number' : len(data)}

	return render(request,'data.html',content)