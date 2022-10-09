from django.shortcuts import render


def store_main_page(request):
    return render(request, 'store/store-main-page.html')


def details_book(request, pk):
    return render(request, 'store/book-details-page.html')
