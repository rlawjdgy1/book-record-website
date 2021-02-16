from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    allBooks = Book.objects.all()

    context = {
        "books": allBooks,
    }

    return render(request, 'main/index.html', context)

def detail(request, id):
    book = Book.objects.get(id=id)

    context = {
        "book": book
    }
    return render(request, 'main/details.html', context)

def add_books(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = BookForm(request.POST or None)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:home")
            else:
                form = BookForm()
            return render(request, 'main/addbooks.html', {"form": form, "controller": "책 추가하기"})
        else:
            return redirect("main:home")

    return redirect("accounts:login")

#edit the movie
def edit_books(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
    
            book = Book.objects.get(id=id)

            if request.method == "POST":
                form = BookForm(request.POST or None, instance=book)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = BookForm(instance=book)
            return render(request, 'main/addbooks.html', {"form":form, "controller": "책 정보 수정하기"})
        else:
            return redirect("main:home")
    
    return redirect("accounts:login")

def delete_books(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            book = Book.objects.get(id=id)

            book.delete()
            return redirect("main:home")
        else:
            return redirect("main:home")
    
    return redirect("accounts:login")
        