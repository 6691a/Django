from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .models import Address
from .serializers import AddressSerializers
# Create your views here.


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Address.objects.all()
        serializer = AddressSerializers(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # 웹에서 json 파일을 보내줌
        # 그걸 열어서 data에 저장
        data = JSONParser().parse(request)

        # serializers의 포맷과 웹에서 준 정보를 일치 시켜 저장
        serializer = AddressSerializers(data=data)
        # 올라온 값이 models 포맷과의 유효성을 검사
        if serializer.is_valid():
            # DB에 값을 저장
            serializer.save()
            # 저장 후 웹에 잘 저장됬다고 표시 해줌
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
