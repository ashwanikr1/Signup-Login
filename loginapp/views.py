from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer  # to validate user credentials
from knox.auth import AuthToken
from loginapp.models import User

from .serializers import RegisterSerializer
# Create your views here.

@api_view(['POST'])
def userLogin(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user=user)
        
    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email,

        },
        'token': token
    })
    
@api_view(['POST'])
def userRegister(request):
    serializer =RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    
    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email,

        },
        'token': token
    })

    
        
    
