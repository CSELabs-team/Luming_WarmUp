from django.shortcuts import render_to_response
from django.template.context import RequestContext
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.models import User
from todo.models import ToDoItem
# from todo.serializer import TodoSerializer

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})

   return render_to_response('home.html',
                             context_instance=context)