from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import AlgoForm
from rest_framework.permissions import AllowAny

@method_decorator(csrf_exempt, name="dispatch")
class AlgoFormView(APIView):
    permission_classes = [AllowAny,]
    def post(self,request):
        data = request.data
        print(data)
        try:
            name = data['name']
            email = data['email']
            phone = data['phoneNumber']
            city = data['city']
            state = data['state']

            AlgoForm.objects.create(name=name, email=email, phone=phone, city=city, state=state)
            print("Object created")
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": f"Error {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    