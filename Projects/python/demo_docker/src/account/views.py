from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError

from account.api.serializers import AccountSerializer
from account.models import Account
from account.permission import UserPermission, CustomUpdatePermission


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.filter()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        elif self.request.method == 'GET':
            return (UserPermission('can_get_users'),)
        raise MethodNotAllowed(method=self.request.method)

    # def create(self, request, *args, **kwargs):
    #     try:
    #         #return Response ("hi")
    #         account = Account.objects.create(

    #             first_name=self.request.data['first_name'],
    #             last_name=self.request.data['last_name'],
    #             gender=self.request.data.get('gender', 'male'),
    #             email=self.request.data['email'],
    #             # set_password=self.request.data['password'],
    #             username=self.request.data['username']
    #         )
    #         account.set_password(request.data.get('new_password'))

    #         serializer = self.get_serializer(account)
 
    #         return Response({'msg':'okay'} , data=serializer.data, status=status.HTTP_201_CREATED)
    #     except Exception as e:
    #         print(e)
    #         return Response(data={'message': e}, status=status.HTTP_409_CONFLICT)


class UserLogin(CreateAPIView):
 
    serializer_class = AccountSerializer
    queryset = Account.objects.filter()
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = Account.objects.get(email__exact=email)
            
            verify_password = check_password(password=password, encoded=user.password)
            if not user.is_active:
                return Response({'message': 'user is not an active user'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            if not verify_password:
                return Response({'message': 'incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
            token = jwt.encode(payload=self.get_serializer(user).data, key=settings.SECRET_KEY, algorithm='HS256')
           # return Response({'token': token}, status=status.HTTP_200_OK)
            return Response(data={
                 'data': request.data, 'token': token,},
                  status=status.HTTP_201_CREATED)
        except Account.DoesNotExist:
            return Response({'message': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)


class PasswordSet(CreateAPIView):

    serializer_class = AccountSerializer
    queryset = Account.objects.filter()
    permission_classes = (permissions.AllowAny, ) 

    def create(self, request, *args, **kwargs):

        data                        = request.headers['token']
        password                    = request.data.get('password')
        data                        = jwt.decode(jwt=data, key=settings.SECRET_KEY, algorithm='HS256')

        user                        = Account.objects.get(pk=data['id'])
        verify_password             = check_password(password=password, encoded=user.password)

        if  verify_password:

            new_password            = request.data.get('new_password')
            # new_password            = jwt.encode({'data':new_password},key=settings.SECRET_KEY, algorithm='HS256')
            # user.set_password           = new_password
            # user.save()
            # serializer = self.get_serializer(user)
            user.set_password(request.data.get('new_password'))
            user.save()

            #return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response({'message': data}, status=status.HTTP_200_OK)
        return Response({'message': "not okay"}, status=status.HTTP_401_UNAUTHORIZED)

class ChangePassword(CreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.filter()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (UserPermission('can_change_password'), )
        raise MethodNotAllowed(method=self.request.method)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        verify_password = check_password(password=request.data.get('old_password'), encoded=str(user.password))
        if not verify_password:
            return Response({'message': 'old password does not match'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('old_password') == request.data.get('new_password'):
            return Response({'message': 'new password cannot be the old password'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('new_password') != request.data.get('confirm_password'):
            return Response(
                {'message': 'new password and confirm password does not match'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.set_password(request.data.get('new_password'))
        user.save()
        serializer = self.get_serializer(user)
        resp = {
            'data': serializer.data,
            'info': f'{user.email} has changed the password'
        }
        return Response(data=resp, status=status.HTTP_201_CREATED)

class AccountListAPIView(ListAPIView):
    
    serializer_class = AccountSerializer
    queryset = Account.objects.filter()
    permission_classes = (permissions.AllowAny, )


    def list(self, request):
        user = Account.objects.get(id = request.user.id)
        serializer = AccountSerializer(user)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 
        
