from django.shortcuts import render

def book(request):
    return render(request,'book.html')
def writer_info(request):
    return render(request,'writer_info.html')
def writer_manage(request):
    return render(request,'writer_manage.html')
def writer_book(request):
    return render(request,'writer_book.html')
def book_manage(request):
    return render(request,'book_manage.html')
def main(request):
    return render(request,'main.html')