from django.shortcuts import render
from .models import *
from .forms import *
from django.http import  *
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
import numbers

def home(request):
	obj =  parentchild.objects.all()
	return  render(request,'index.html',{'obj': obj})

def parentchildhier(request):
	if request.method == 'POST':
		form = pc_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/parentChild/')
	else:
		form = pc_form()
	return  render(request,'parentchild.html',{'form':form})

# def parentchildhier(request):
#     if(request.method == 'POST'):
#         # parent_name = request.POST['parent_name']
#         # parent_id = request.POST.get('parent_domain')
#         #person = Person(name=name, parent_id=parent_id)
#         form = pc_form(request.POST)
#         person = parentchild.objects.get(id = parent )
#         person.children.all()
#         person.save()
#
#         return HttpResponseRedirect('/parentChild/')
#     else:
#         return render(request, 'parentChild.html',{'form':form})


def search(request):
	if request.method == "GET":
		srch = request.GET.get('srh')
		match = parentchild.objects.filter(child_name__icontains=srch )
		return render(request, 'search.html', {'sr': match})
	else:
		return render(request, 'search.html')

