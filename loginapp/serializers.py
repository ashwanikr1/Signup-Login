from django.contrib.auth.models import User
from rest_framework import serializers,validators

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only':True},
            'email':{
                'required':True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(),"A user with this email already exists"
                    )
                ]
            }
        }
        
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        
        user =User.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        return user
                  