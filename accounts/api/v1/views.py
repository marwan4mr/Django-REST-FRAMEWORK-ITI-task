from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.authtoken.models import Token



# Create your views here.
# Available RESTAPI Permission
# 1- AllowAny
# 2- IsAuthenticated
# 3- IsAdminUser
# 4- IsAuthenticatedReadOnly
# 5-DjangoModelPermissionsOrAnonReadOnly
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format="json"):
    content = { 'user': str(request.user), 'auth': str(request.auth), }
    return Response(content)

from .serializers import UserSerializer

@permission_classes([])
@api_view(['POST'])
def sign_up(request):
    data = {'data': '',  'status': ''}
    user_serialized = UserSerializer(data=request.data)

    if user_serialized.is_valid():
        user_serialized.save()
        data['data'] = {
            'user': {
                "username": user_serialized.data.get('username'),
                "email": user_serialized.data.get('email')
            },
            "token" : Token.objects.get(user__username=user_serialized.data.get('username')).key,
            'message': 'Created'
            }
        data['status'] = status.HTTP_200_OK
    else:
        data['data'] = user_serialized.errors
        data['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication]) 
def logout(request):
    # pass
    data = {'data': 'logged out',  'status': status.HTTP_200_OK}
    tv = str(request.auth)
    print(f"request.auth 👏{str(request.auth)}")
    t = Token.objects.get(key=tv)
    # print(dir(t))
    t.delete()
    return Response(**data)
# @api_view(['POST'])
# def login(request):
#     pass