from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home/index.html')

def full(request):
	return render(request, 'home/pages/full.html')

def about(request):
	return render(request, 'home/pages/about.html')

def menu(request):
	return render(request, 'home/pages/menu.html')

def specials(request):
	return render(request, 'home/pages/specials.html')

def events(request):
	return render(request, 'home/pages/events.html')

def chefs(request):
	return render(request, 'home/pages/chefs.html')

def gallery(request):
	return render(request, 'home/pages/gallery.html')

def contact(request):
	return render(request, 'home/pages/contact.html')

def book(request):
	return render(request, 'home/pages/book.html')


