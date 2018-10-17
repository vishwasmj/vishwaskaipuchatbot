from django import forms
from .models import *

class pc_form(forms.ModelForm):
	parent_name = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
	parent_domain = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
	child_name = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
	child_EA_Number = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
	child_domain = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)

	class Meta():
		model = parentchild
		fields = ['parent_name','parent_domain','child_name','child_EA_Number','child_domain']