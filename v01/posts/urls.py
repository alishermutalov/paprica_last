from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),  # pk is the primary key of the news article
    path('contacts/', views.contacts_view, name='contacts'),
    path('success/', views.success_view, name='success'),
    path('contact/thanks/', TemplateView.as_view(template_name='contact_thanks.html'), name='contact_thanks'),
]
