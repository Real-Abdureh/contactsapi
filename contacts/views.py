from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import contacts
from .serializers import ContactSerializer
from rest_framework import permissions


class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)

    def get_queryset(self):
        return contacts.objects.filter(owner= self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'  


    def get_queryset(self):
        return contacts.objects.filter(owner= self.request.user)

# Create your views here.
