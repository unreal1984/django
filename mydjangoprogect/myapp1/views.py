#!/usr/bin/python
# -*- coding: utf8 -*-
from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    #new_worker = Worker.objects.create(name="Ivan", second_name="Ivanov", salary=35000)
    
    worker_to_change = Worker.objects.get(id=5)
    worker_to_change.second_name = "Livanov"
    worker_to_change.save()
    print(worker_to_change)
    
    all_workers = Worker.objects.all()
    print(all_workers)
    
    workers_filtered = Worker.objects.filter(salary=30000)
    print(workers_filtered)
    
    for i in all_workers:
        print(f"Surname: {i.second_name}, Name: {i.name}, Salary: {i.salary}, ID: {i.id}")
                
    return render(request, 'index.html', context={'data':all_workers})
#def about_page(request):
#   return render(request, 'about.html')
