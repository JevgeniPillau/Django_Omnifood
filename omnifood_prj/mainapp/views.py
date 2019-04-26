from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def base(request):
    return render(request, 'mainapp/base.html')


def products(request):
    context = {'products': ['apple', 'banana', 'kiwi']}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')
