from django.shortcuts import render
def dangky(request):
    context= {}
    return render(request, 'dangky.html', context)
def dangnhap(request):
    context= {}
    return render(request, 'dangnhap.html', context)

# Create your views here.
