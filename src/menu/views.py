from django.db.models import Q
import random
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
#This is standard HTML
from .models import MenuModel

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
	'''def get_object(self,*args,**kwargs):
		user_id =self.kwargs.get('user_id')
		#This is called a look up
		#This function will get the id from the database or return 404 error code
		obj = get_object_or_404(MenuModel, id=user_id)#pk = rest_id
		return obj
'''




'''class SearchFirstNameListView(ListView):
	template_name = 'menu/menu_list_.html'

	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = MenuModel.objects.filter(
				Q(name__iexact=slug) | #Will only search name
				Q(name__icontains=slug)

				) 
		else:
			queryset = MenuModel.objects.none()
		return queryset
'''
'''
class LastNameListView(ListView):
	queryset = MenuModel.objects.filter(name__iexact='last_name')
	template_name = 'menu/menu_list_.html'
'''
#Template based view
'''class HomeView(TemplateView):
	template_name='home.html'
	#Overrideing method: This method overridees
	#TemplateView becuase TemplateView is has nothing defined
	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args,**kwargs)
		num = None
		some_list = [
			random.randint(0, 10000000), 
			random.randint(0, 10000000),
			random.randint(0, 10000000)
		]
		condition_bool_item = True
		if condition_bool_item:
			num = random.randint(0, 10000000)
		context = {
			"num": num, 
			"some_list": some_list
		}
		return context
'''
#Class based views
'''class ContactView(TemplateView):
	template_name='contact.html'
class AboutView(TemplateView):
	template_name='about.html'
'''

#Function based view
'''
def about(request):
	context = {}
	return render(request, "about.html",context)# response
	
def contact(request):# Function based view
	context = {}
	return render(request, "contact.html",context)# response
'''
#class based view
'''class AboutView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "about.html",context)
		'''