from django.shortcuts import render,redirect
from django.views.generic.edit import DeleteView
from Admin.models import books



class returnbookGenericView(DeleteView):
    model = books
    template_name = 'students/return.html'
    success_url = '/home'


def showborrow(request):
    borrow=books.objects.filter(borrow=request.user.id)
    return render(request,'students/bowbooks.html',context={'borrow':borrow})

def bowbooks(request,id):
    bo=books.get_spec_book(id)
    bo.borrow=request.user.id
    bo.save()
    return redirect('books')
