"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ScoalaWeb.views import (
	contact_view,

    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,

    doc_upload,
    doc_list,
    DocDeleteView,
    
    activitati_upload,
    activitati_list,
    ActivitatiDeleteView,
) 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', PostListView.as_view(), name = 'acasa'),
    path('acasa/',PostListView.as_view(), name = 'acasa'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/nou/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),

    path('contact/', contact_view, name = 'contact'),

    path('documente/upload', doc_upload, name = 'upload'),
    path('documente/list', doc_list, name = 'documente'),
    path('documente/<int:pk>/delete', DocDeleteView.as_view(), name = 'doc-delete'),

    path('activitati/upload', activitati_upload, name = 'activitati-upload'),
    path('activitati/list', activitati_list, name = 'activitati'),
    path('activitati/<int:pk>/delete', ActivitatiDeleteView.as_view(), name = 'activitati-delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)