from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from todo.models import ToDoItem
from django.contrib.auth import authenticate


def to_do_list(request):

	# authentication:
	if not hasattr(request.user, 'email'):
		return redirect('http://127.0.0.1:8000')

	user_email = request.user.email
	user = User.objects.filter(username=request.user.username, email=user_email)
	
	template = loader.get_template('todo/todolist_page.html')

	todo_items_of_user = ToDoItem.objects.filter(owner=user).values_list('to_do_item', flat=True)
	context = RequestContext(request, {
        'init_todo_items' : todo_items_of_user,
        'username': request.user.username,
        'user_email': request.user.email,
    })

	return HttpResponse(template.render(context))


def add_to_do(request):
	if request.method == 'POST':
		new_item = request.POST['new_item']

		user=request.user
		new_list_item = ToDoItem.objects.create(owner=user, to_do_item=new_item)
		item_id = new_list_item.id

	return render_to_response("todo/items_list.html",
	                              { 'new_item' : new_item,
    	                          	'item_id' :  item_id
    	                          	}
                              )


def delete_item(request):
	if request.method == 'POST':
		item_id_delete = request.POST['item_id']
		user = request.user
		
		ToDoItem.objects.filter(id=item_id_delete).delete()
		
		return HttpResponse(status=200)


def edit_item(request):
	if request.method == 'POST':
		item_id_edit = request.POST['item_id']
		update_info = request.POST['update_info']
		item = ToDoItem.objects.get(id=item_id_edit)
		item.to_do_item = update_info
		item.save()
		
		return HttpResponse(status=200)