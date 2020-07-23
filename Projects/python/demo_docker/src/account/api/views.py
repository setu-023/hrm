# from django.contrib.auth.decorators import permission_required

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import permissions
# from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.authtoken.models import Token

# # from account.permission import HRAdminGroupPermission
# from account.models import Account
# from account.api.serializers import RegistrationSerializer



# @api_view(['POST', ])
# @permission_classes([permissions.AllowAny],)
# def registration_view(request):

# 	if request.method == 'POST':
# 		serializer = RegistrationSerializer(data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			account = serializer.save()
# 			data['response'] = 'successfully registered new user.'
# 			data['email'] = account.email
# 			data['username'] = account.username
# 			token = Token.objects.get(user=account).key
# 			data['token'] = token
# 			return Response({"response_code": '200',"message:Succcessfully Regisy", "response": status.HTTP_200_OK,"data":data})
# 		else:
# 			data = serializer.errors
# 		return Response({"response_code": '500', "response": status.HTTP_500_INTERNAL_SERVER_ERROR,"data":data})



# # @api_view(['GET'])
# # @permission_required('is_check')
# # #@permission_classes([IsAuthenticated])
# # def sample(self):
# #
# # 	data={'msg':'hello'}
# #
# # 	group_required = 'HR Admin1'
# # 	return Response(data)

# @api_view(['GET'])
# def homePage(self):

# 	data={'msg':'Welcome to Homepage'}
# 	return Response(data)
