#Samuel Choy
from django.db import models
from django.db.models.signals import pre_save, post_save
# Create your models here.

from .utils import unique_slug_generator
class MenuModel(models.Model):
	name  = models.CharField(max_length=120)
	email  = models.EmailField()#(max_length=254, **options)#CharField(max_length=120, null=True, blank=True)
	about_you = models.CharField(max_length=120, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=True)
	updated =  models.DateTimeField(auto_now=True)
	slug = models.SlugField(null=True, blank=True)
	#slug = models.SlugField(unique=True, blank=True)
	#my_date_field = models.DateTimeField(auto_now=False, auto_now= False)
	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name #obj.title
def menu_pre_save_reciver(sender, instance, *args,**kwargs):
	#print('saving..')
	#print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
'''
def menu_post_save_reciver(sender, instance, created, *args,**kwargs):
	print('saved!')
	print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.save()
'''
pre_save.connect(menu_pre_save_reciver, sender=MenuModel)

#post_save.connect(menu_post_save_reciver, sender=MenuModel)
