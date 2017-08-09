from django.db.models import Q
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
#This is standard HTML
from .forms import EmailCreateForm
from .models import MenuModel

def email_createview(request):
	form = EmailCreateForm(request.POST or None)
	errors = None
	if form.is_valid():# To validate form
		obj = MenuModel.objects.create(
				name = form.cleaned_data.get('name'),
				email = form.cleaned_data.get('email'),
				about_you = form.cleaned_data.get('about_you')
			)
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
'''
	def get_object(self,*args,**kwargs):
		user_id =self.kwargs.get('user_id')
		#context = super(MenuDetailView, self).get_context_data(*args,**kwargs)
		#This is called a look up
		#This function will get the id from the database or return 404 error code
		obj = get_object_or_404(MenuModel, id=user_id)#pk = rest_id
		return obj
'''
