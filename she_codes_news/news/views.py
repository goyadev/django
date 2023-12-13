
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Comment
from .forms import StoryForm, CommentForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404




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

# use getcontextdata. see line 20, change line 22
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    

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
    form_class = CommentForm
    template_name = 'news/story.html'
    context_object_name = 'commentform'

    # a function to allow the URL to go to the right page
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get("pk")}) 
    
    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.instance.post = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)