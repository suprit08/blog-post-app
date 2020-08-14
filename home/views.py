from django.shortcuts import render

from django.views.generic import ListView
from users.models import Post

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from project import helpers

# Create your views here.
def home(request):

    post = Post.objects.order_by('-id').all()
    Context1 = helpers.pg_records(request, post, 5)

    return render(request, 'home_page.html', {'post':post})




class PostListView(ListView):
    model = Post
    template_name = 'home_page.html'
    context_object_name = 'post'
    ordering = ['-date_published']



