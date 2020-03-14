import csv, io
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Post, Documente, Activitati, Images
from django.core.files.storage import FileSystemStorage
from .forms import DocForm, ActivitatiForm, ImageForm
from django.views.generic import (ListView,
								  DetailView,
								  CreateView,
								  UpdateView,
								  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.forms import modelformset_factory

# Create your views here.

class PostListView(ListView):
	model = Post
	context_object_name  = 'model'
	template_name = 'home.html'
	ordering = ['-data_publicarii']
	

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['titlu', 'text', 'descriere', 'data_publicarii']

	def form_valid(self,form):
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['titlu', 'text', 'descriere', 'data_publicarii']

	def form_valid(self,form):
		return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	success_url = '/'





def contact_view(request):
	return render(request, 'contact.html')





def doc_upload(request):
	if request.method == 'POST':
		form = DocForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect ('documente')
	else:
		form = DocForm()
		return render(request, 'doc_upload.html', {
			'form':form
			})

def doc_list(request):
	docs = Documente.objects.all()
	return render(request, 'doc_list.html', {'docs':docs})

class DocDeleteView(LoginRequiredMixin, DeleteView):
	model = Documente
	success_url = '/documente/list'




def activitati_upload(request):
	ImageFormset = modelformset_factory(Images, form = ImageForm, extra = 10)
	if request.method == 'POST':
		activitateform =ActivitatiForm(request.POST)
		formset = ImageFormset (request.POST or None, request.FILES or None, queryset = Images.objects.none())
		if activitateform.is_valid() and formset.is_valid():
			activitate_form = activitateform.save(commit=False)
			activitate_form.save()
			for form in formset.cleaned_data:
				if form: 
					image = form['image']
					photo = Images(activitati = activitate_form, image = image )
					photo.save()
			return redirect('activitati')
	else:
		activitateform = ActivitatiForm()
		formset = ImageFormset(queryset = Images.objects.none())
		return render(request, 'activitati_upload.html', {
			'form':activitateform,
			'formset':formset
			})

def activitati_list(request):
	activitati = Activitati.objects.all()
	post = Images.objects.all()
	ordering = ['-data_publicarii']
	return render(request, 'activitati_list.html', {'activitati':activitati,
													'post':post})


class ActivitatiDeleteView(LoginRequiredMixin, DeleteView):
	model = Activitati
	success_url = '/activitati/list'

