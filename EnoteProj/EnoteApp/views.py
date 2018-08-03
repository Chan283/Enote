from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login	#authenticate will chk for legitimate user in db, login attaches a seesion id for avoiding auth on every page
from EnoteApp.models import Notes
from EnoteApp.forms import NotesCreateForm,NotesUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

#display the about page	
class AboutView(TemplateView):
	template_name='about.html'

# Display the user signup page	
def signup(request):
	if request.method=="POST":	#if user clicks submit button
		form=UserCreationForm(request.POST)
		if form.is_valid():	#if form data is valid
			form.save()
			username=form.cleaned_data.get('username')	#get username from form data
			raw_password=form.cleaned_data.get('password1')	#get password from form data
			user=authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'signup.html',{'form':form})

# Display a form to user to create notes	
class NotesCreateView(LoginRequiredMixin,CreateView):
	model=Notes
	form_class=NotesCreateForm
	redirect_field_name='notes_detail.html'
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(NotesCreateView, self).form_valid(form)

# Display the List of notes created by a user		
class NotesListView(LoginRequiredMixin,ListView):
	model=Notes
	context_object_name = 'notes_list'
	template_name = 'notes_list'

	def get_queryset(self):
		return super(NotesListView, self).get_queryset().filter(user=self.request.user)	#get the list of notes specific to loggedin user 

#Display the details when user clicks on his particular note		
class NotesDetailView(LoginRequiredMixin,DetailView):
	model=Notes

#Editing of an existing note
class NotesUpdateView(LoginRequiredMixin,UpdateView):
	model=Notes
	form_class=NotesUpdateForm
	redirect_field_name='EnoteApp/notes_detail'

#Deleting of an existing note
class NotesDeleteView(LoginRequiredMixin,DeleteView):
	model=Notes
	success_url=reverse_lazy('notes_list')

# display homepage	
class HomeView(TemplateView):
	template_name='home.html'