from django.db import models
from django.contrib.auth.models import User


class ToDoItem(models.Model):
	"""
	Just a simple CharField to fill the do to items
	"""
	owner = models.ForeignKey(User)
	to_do_item = models.CharField(max_length=200)

	class Meta:
		db_table = "todo_items"