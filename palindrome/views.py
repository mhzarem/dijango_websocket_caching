from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'palin/user.html')


def user(request, user_name):
    return render(request, 'palin/palin_test.html', {'user_name': user_name})