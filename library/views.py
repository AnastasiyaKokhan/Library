from django.shortcuts import render, get_object_or_404, redirect

from library.models import Library, Book


# Create your views here.

def get_library_page(request):
    library_queryset = Library.objects.all()
    book_queryset = Book.objects.all()
    context = {
        'library_queryset': library_queryset,
        'book_queryset': book_queryset,
    }

    return render(request, 'library.html', context)

def get_book_library(request, id):
    library_queryset = Library.objects.all()
    book_queryset = Book.objects.filter(library_id=id)
    context = {
        'library_queryset': library_queryset,
        'book_queryset': book_queryset,
    }
    return render(request, 'library.html', context)

def add_book(request):
    libraries = Library.objects.all()
    context = {
        'libraries': libraries,
    }
    if request.method == 'POST':
        if request.POST.get('add_library'):
            new_library = Library(name=request.POST.get('add_library'))
            new_library.save()
            new_book = Book(name=request.POST.get('name'), author=request.POST.get('author'), library=new_library)
            new_book.save()
            return redirect("libraries")
        elif request.POST.get('library'):
            new_book = Book(name=request.POST.get('name'), author=request.POST.get('author'),
                            library=libraries.get(name=request.POST.get('library')))
            new_book.save()
            return redirect("libraries")

    return render(request, 'add_book.html', context)

