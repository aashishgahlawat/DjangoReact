from rest_framework.views import APIView, Response
from rest_framework import status
from django.db import transaction
from django.db import IntegrityError
from rest_framework.permissions import AllowAny
from ..models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from ..models import MasterCustomer, MasterBusiness


# Don't catch any exceptions for atomicity
@transaction.atomic  # decorator
class RegisterCustomer(APIView):
    """
    This API is used to register a new customer
    """
    permission_classes = (AllowAny, )

    def post(self, request):
        username = request.POST.get('phone')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not password:
            return Response({'code': '400', 'message': 'Username and Password required'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not email:
            email = None

        try:
            user, created = User.objects.get_or_create(username=username, is_customer=True)
        except IntegrityError:
            return Response({'code': '400', 'message': 'Username shall contain less than 150 characters'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not created:
            return Response({'code': '400', 'message': 'Customer with given phone already exists.'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            # Same User's Business and Customer account emails may vary, default latest email will be used
            user.email = email
            user.set_password(password)
            user.save()

            customer = MasterCustomer(country_id=1, state_id=1, city_id=1, name=request.data.name, email=email)
            try:
                customer.save()
            except IntegrityError:
                return Response({'code': '400', 'message': 'Invalid data format.'},
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                token, created = Token.objects.get_or_create(user=user)
            except Exception as e:
                return Response({'code': '500', 'message': 'Internal server error', 'error': e},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'code': '200', 'message': 'Registered Successfully', 'token': token.key,
                         'customer_id': customer.id, 'user_id': user.id}, status=status.HTTP_200_OK)
