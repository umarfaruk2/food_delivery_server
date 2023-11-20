from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, UserPasswordResetEmailSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate, login
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create access and refresh token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializer = RegisterSerializer(data = request.data) 

        if serializer.is_valid(raise_exception=True):
            user = serializer.save() 
            token = get_tokens_for_user(user)
            return Response({'msg': 'Registration successful', 'token': token}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format = None):
        serializer = LoginSerializer(data = request.data) 

        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email = email, password = password)
            
            print(user, email, password)
            if user is not None:
                token = get_tokens_for_user(user)

                return Response({'token': token, 'msg': 'Login success'}, status = status.HTTP_200_OK) 
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not valid']}}, status = status.HTTP_404_NOT_FOUND) 
            
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Only authenticate user can get this data with access token
class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


# user change password view
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format = None):
        serializer = UserChangePasswordSerializer(data = request.data, context = {'user': request.user}) 

        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password change success'}, status = status.HTTP_200_OK) 
    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# Password reset with email
class UserSendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format = None):
        serializer = UserPasswordResetEmailSerializer(data = request.data)  

        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password reset link send, check you email'}, status = status.HTTP_200_OK) 
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]            

    def post(self, request, uid, token, format = None):
        serializer = UserPasswordResetSerializer(data = request.data, context = {'uid': uid, 'token': token}) 

        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password reset successful'}, status = status.HTTP_200_OK) 
            
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            