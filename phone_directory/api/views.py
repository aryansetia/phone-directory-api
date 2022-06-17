from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import ContactSerializer
from . models import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.

class ContactList(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if request.data["name"] is None or request.data["phone"] is None:
            return Response({"Error":"name and contact number are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if request.data["email"]:
                email = request.data["email"]
        except:
            email = None

        contact = Contact.objects.create(
            name=request.data["name"],
            contact_number=request.data["contact_number"],
            email=email
        )

        mapping=MapUserContact.objects.create(
            user=request.user,
            contact=contact
        )

        return Response({
            "Message":"Contact successfully added to the directory"
        },
        status=status.HTTP_201_CREATED
        )



@permission_classes([AllowAny])
class Register(APIView):
    def post(self, request):
        if request.data["name"] is None or request.data["contact_number"] is None:
            return Response({
                "Error":"Both name and contact number are required"
            })
        
        try:
            if request.data["email"]:
                email = request.data["email"]
        except:
            email = None

        user=User(
            username = request.data["name"],
            password = request.data["password"],
            email = email
        )

        if user:
            user.set_password(request.data["password"])
            user.save()

            profile = Profile.objects.create(
                user=user,
                contact_number = request.data["contact_number"],
                email = email
            )
            return Response(
                {"Message":"Profile created successfully"},
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"Message": "Error during the registration!"},
                status = status.HTTP_400_BAD_REQUEST
            )


@permission_classes([AllowAny])
class Login(APIView):
    def post(self, request):
        if not request.data:
            return Response(
                {"Error":"Username/Password is neccessary"},
                status = status.HTTP_400_BAD_REQUEST
            )
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response(
                {"Error":"Please enter valid credentials"},
                status=status.HTTP_404_NOT_FOUND
            )
        user = authenticate(username = username, password = password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "Token":token.key
            },
            status=status.HTTP_200_OK
        )

class Spam(APIView):
    def post(self, request):
        contact_number = request.data.get("contact_number")
        if request.data["contact_number"] is None:
            return Response(
                {"Error":"Phone number needed!"},
                status = status.HTTP_400_BAD_REQUEST
            )
        contact = Contact.objects.filter(contact_number = contact_number).update(spam=True)
        profile = Profile.objects.filter(contact_number = contact_number).update(spam=True)
        if(contact+profile):
            return Response(
                {"Message":"Contact marked as spam!"},
                status=status.HTTP_200_OK
            )
        else:
		        return Response(
				{
					"Error":"Phone number not found in database!"
				},
				status = status.HTTP_404_NOT_FOUND
			)


class SearchContact(APIView):
	def get(self,request):
		name=request.data.get("name")
		if request.data["name"] is None:
			return Response(
				{
					"Error":"Name is required!!"
				},
				status = status.HTTP_400_BAD_REQUEST
			)
		profile_start=Profile.objects.filter(user__username__startswith=name)
		profile_contain=Profile.objects.filter(user__username__contains=name).exclude(user__username__startswith=name)
		contact_start=Contact.objects.filter(name__startswith=name)
		contact_contain=Contact.objects.filter(name__contains=name).exclude(name__startswith=name)
		response=[]
		for contact in profile_start:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		for contact in contact_start:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		for contact in profile_contain:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		for contact in contact_contain:
			response.append(
					{
						"name":contact.name,
						"phone_number":contact.phone_number,
						"spam":contact.spam,
					}
				)
		return Response(
				response,
				status=status.HTTP_200_OK
			)
