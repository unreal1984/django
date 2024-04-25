#!/usr/bin/python
# -*- coding: utf8 -*-
from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    all_workers = Worker.objects.all()
    print(all_workers)
    
    workers_filtered = Worker.objects.filter(salary=30000)
    print(workers_filtered)
    
    for i in all_workers:
        print(f"Surname: {i.second_name}, Name: {i.name}, Salary: {i.salary}, ID: {i.id}")
                
    return render(request, 'index.html')
#def about_page(request):
#   return render(request, 'about.html')
