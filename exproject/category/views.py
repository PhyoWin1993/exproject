from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,"category/home.html",{"title":"Home Page"})

def create(request):
    return render(request,"category/home.html")

def edit(request):
    return render(request,"category/home.html")

def delete(request):
    return redirect('cat-home')