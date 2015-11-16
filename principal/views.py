from django.shortcuts import render

# Create your views here.

def inicio(request):
	return render(request,'index.html',{})

def servicios(request):
	return render(request,'servicios.html',{})

def sobre(request):
	return render(request,'about.html',{})

def contacto(request):
	return render(request,'contacto.html',{})