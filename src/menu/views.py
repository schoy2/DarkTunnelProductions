#Samuel Choy
from django.db.models import Q
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# Create your views here.
#This is standard HTML
from .forms import EmailCreateForm, MenuModelCreateForm
from .models import MenuModel

def email_createview(request):
	form = MenuModelCreateForm(request.POST or None)
	errors = None
	if form.is_valid():# To validate form
	# customize
	#Like a pre_save
		form.save()
	#like a post_save
		return HttpResponseRedirect("/menu/")# Routes back to menu
	if form.errors: # to handle errors
		errors = form.errors

	template_name ='menu/form.html'
	context ={"form": form,"errors": errors}

	return render(request,template_name,context)


class MenuListView(ListView):
	#queryset = MenuModel.objects.all()
#	template_name = 'menu/menu_list_.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = MenuModel.objects.filter(
				Q(name__iexact=slug) | #Will only search name
				Q(name__icontains=slug)
				)
		else:
			queryset = MenuModel.objects.all()
		return queryset

class MenuDetailView(DetailView):
	queryset = MenuModel.objects.all()

class MenuCreateView(CreateView):
	form_class = MenuModelCreateForm# created from MenuModelCreateForm in forms.py
	template_name = 'menu/form.html'
	success_url = "/menu/"
