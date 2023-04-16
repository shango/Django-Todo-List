from django.shortcuts import redirect, render
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('A new tem has been added to the List.'))
			return render(request, 'home.html', {'all_items' : all_items})
	else:
		all_items = List.objects.all
		return render(request, 'home.html', {'all_items' : all_items})

def about(request):
	return render(request, 'about.html', {})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been deleted.'))
	return redirect('home')

