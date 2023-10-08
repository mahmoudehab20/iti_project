from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic import ListView,UpdateView
from Admin.models import books
from students.models import borrowedbooks