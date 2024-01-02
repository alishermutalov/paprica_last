from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from .models import News
# Create your views here.



def news_list(request):
    news = News.objects.all()  # Retrieve all news objects from the database
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, pk):
    news_article = get_object_or_404(News, pk=pk)  # Retrieve news article by primary key or return 404
    return render(request, 'news_detail.html', {'news_article': news_article})

def success_view(request):
    return render(request, 'success.html')

def contacts_view(request):
    return render(request, 'contact.html')


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'index.html', {'form': form})

