from django.shortcuts import render,reverse,redirect
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView,ListView
from Admin.models import books
from Admin.forms import booksModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your views here.

class booksListGenericView(ListView):
    model = books
    template_name = 'Admin/books.html'
    context_object_name = 'book'

class booksDetailGenericView(DetailView):
    model = books
    template_name = 'Admin/show.html'   

class DeletebookGenericView(DeleteView):
    model = books
    template_name = 'Admin/delete.html'
    success_url = '/home'

class addbookGenericView(CreateView):
    form_class =  booksModelForm
    template_name =  'Admin/create.html'
    success_url = '/home' 

class UpdatebookGenericView(UpdateView):
    model = books
    form_class = booksModelForm
    template_name = 'Admin/edit.html'
    success_url = '/home/show'




class registration(CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url='/acc/login'


class usersListGenericView(ListView):
    model = User
    template_name = 'Admin/users.html'
    context_object_name = 'user'


def search(request):
    if 'search' in request.POST:
        query=request.POST['search']
        name=User.objects.get(username=query)
        return render(request,'Admin/specuser.html',context={'name':name})
def bowbooks(request,id):
    bo=books.get_spec_book(id)
    bo.borrow=request.user.id
    bo.save()
    return redirect('books')


def showborrow(request):
    borrow=books.objects.filter(borrow=request.user.id)
    return render(request,'Admin/bowbooks.html',context={'borrow':borrow})

class returnbookGenericView(DeleteView):
    model = books
    template_name = 'Admin/delete.html'
    success_url = '/home'
