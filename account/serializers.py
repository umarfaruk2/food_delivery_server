from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'address', 'restaurant', 'customer', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # validated password and confirm password while registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")
        return attrs 
    
    # while use custom user auth model then we have to create the user
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
        

class LoginSerializer(serializers.ModelSerializer):
        email = serializers.EmailField(max_length = 255)
        class Meta:
            model = User
            fields = ['email', 'password']


# user profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'name']


# user change password
class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 244, style={'input_type': 'password'}, write_only= True)
    password2 = serializers.CharField(max_length = 244, style={'input_type': 'password'}, write_only= True)

    class Meta:
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")
        
        user = self.context.get('user')
        user.set_password(password)
        user.save()
        return attrs


# Reset password serializer
class UserPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')

        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            link = 'http://localhost:300/api/user/reset/'+uid+'/'+token
            # Email send
            body = 'Click following link to reset your password' + " " + link
            data = {
                'subject': "Rest your password",
                'body': body,
                'to_email': user.email
            }
            Util.send_email(data)
            print('password reset link: ', link)
            return attrs
        else:
            raise serializers.ValidationError('You are not a valid user')
            
        
class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 244, style={'input_type': 'password'}, write_only= True)
    password2 = serializers.CharField(max_length = 244, style={'input_type': 'password'}, write_only= True)

    class Meta:
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        uid = self.context.get('uid')
        token = self.context.get('token')

        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match")
        id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk = id) 
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError('You are not a valid user')
            
        user.set_password(password)
        user.save()
        return attrs

          
