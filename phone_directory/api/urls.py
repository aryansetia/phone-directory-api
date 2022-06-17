from django.urls import path
from . views import *

urlpatterns=[
	path('contacts/',ContactList.as_view(),name='contacts'),
	path('spams/',Spam.as_view(),name='spams'),
	path('register/',Register.as_view(),name='register'),
	path('search_by_name/',SearchContact.as_view(),name='search_contact'),
	path('login/',Login.as_view(),name='login'),
]