
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Comment
from .forms import StoryForm
from django.shortcuts import redirect


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by("-pub_date",)[4:]
# the slice of stories needs to exclude the first 4 stories because they are showing up in the latest stories section without repeating the stories from the latest section. 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date",)[:4]
        return context
    # Here the  [:4] slice and negative pub_date allow for a snapshot of the latest four stories to show up in reverse chronological order (newest to oldest)


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    template_name = 'news/createStory.html'
    context_object_name = 'storyform'
    success_url = reverse_lazy('news:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redirect to create account or login page
            return redirect('login') 
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Adding a view for comments form on the page, rather than opening a new page 12 Dec
class AddCommentView(generic.CreateView):
    form_class = Comment
    template_name = 'news/story.html'
    context_object_name = 'commentform'
    success_url = reverse_lazy('news:index') #will need to update this to be the article page. May need reference to article number URL. Think on this