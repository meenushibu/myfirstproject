from django.shortcuts import render
from .models import Post
# Create your views here.


def post_list(request):
	from django.utils import timezone
	mass=Post.objects.all()
	return render(request, 'blog/post_list.html', {'s': mass})