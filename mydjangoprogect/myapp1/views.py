from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    all_workers = Worker.objects.all()
    print(all_workers)
    return render(request, 'index.html')
#def about_page(request):
#   return render(request, 'about.html')
