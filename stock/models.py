from django.db import models

# Create your models here.
class Category(models.Model):
	cat_name = models.TextField()
	cat_table_name = models.TextField()

	def __str__(self):
		return str(self.id) +" "+self.cat_name+" "+self.cat_table_name

