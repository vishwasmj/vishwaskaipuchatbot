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
	if request.method == "POST":
		srch = request.POST['srh']
		print ("SERCH", srch)
		if srch:
			match = parentchild.objects.filter(Q(child_name__icontains = srch) |
			                                   Q(child_domain__icontains =srch) |
			                                   Q(parent_name__icontains=srch) |
			                                   Q(parent_domain__icontains=srch )|
			                                   Q(child_EA_Number__icontains =srch)
			                                   )
			if match:
				parent_domain = match[0].parent_domain
				print ("PARENT DOMAIN", parent_domain)
				child_info = parentchild.objects.filter(parent_domain=parent_domain).order_by('is_highlight')
				print(len(child_info))

				child_info.update(is_highlight = False)
				for child in child_info:
					if isinstance(srch, str):
						if child.child_EA_Number == srch:
							child.is_highlight = True
					elif isinstance(srch, str):
						if child.child_name == srch:
							child.is_highlight = True
					elif isinstance(srch,str):
						if child.domain == srch:
							child.is_highlight = True
					else:
						child.is_highlight = False
					child.save()

				child = child_info.order_by('-is_highlight').values()[0:7]
				print("childs",child)
				Paginator = Paginator(child, 10)
				page = request.GET.get('page')
				contacts = paginator.get_page(page)
				return render(request,'search.html',{'sr':child})
			else:
				messages.error(request,'no result found,try again!')
		else:
			return HttpResponseRedirect('/search/')
	return render(request,'search.html')

# for item in parentchild.objects.filter():
#     print( parentchild.parent_name)
#     for child in item.children.all():
#         print (child.child_name)

# def tree_view(request):
#     people =  parentchild.objects.prefetch('children')
#     return render(request, 'template.html', {'people': people})

# Create your views here.
