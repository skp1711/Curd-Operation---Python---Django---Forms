from django.shortcuts import render, redirect
from .models import Curd
from .forms import CurdForm

# Create your views here.


def home(request):
    blogs = Curd.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def add_data(request):
    if request.method == "POST":
        form = CurdForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/curds/')
            except:
                pass
    else:
        form = CurdForm()
    return render(request, 'add.html', {'form': form})


def update_data(request, pk):
    blogs = Curd.objects.get(id=pk)
    form = CurdForm(instance=blogs)

    if request.method == 'POST':
        form = CurdForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('/curds/')

    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request, 'update.html', context)


def delete_data(request, pk):
    blogs = Curd.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/curds/')

    context = {
        'blogs': blogs,
    }
    return render(request, 'delete.html', context)
