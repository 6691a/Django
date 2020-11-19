from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.


@csrf_exempt
def login(request):

    if(request.method == 'POST'):
        data = json.loads(request)
        email = request.get("email", '')
        print('request_body'+str(email))

        # return render(request, 'login.html')


# def user_list(request):
