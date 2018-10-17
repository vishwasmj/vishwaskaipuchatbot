from django.db import models

class parentchild(models.Model):
	parent_name = models.CharField(max_length= 50)
	parent_domain = models.CharField(max_length= 50)
	child_name = models.CharField(max_length= 50)
	child_EA_Number = models.CharField(max_length= 50)
	child_domain = models.CharField(max_length= 50)
	is_highlight = models.BooleanField(default=False)
	#parent = models.ForeignKey('self',on_delete=models.CASCADE,)
	#parent_id = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE,)

	def __str__(self):
		return self.parent_name

# Create your models here.
