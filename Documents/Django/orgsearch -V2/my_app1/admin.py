from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export import resources



@admin.register(parentchild)
class ParentchildAdmin(ImportExportModelAdmin):
	pass
#




# class parentchildAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#
# 	class Meta:
# 		model= parentchild
#
# admin.site.register(parentchildAdmin, parentchild)
# Register your models here.
