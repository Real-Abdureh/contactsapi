from rest_framework.serializers import ModelSerializer
from .models import contacts


class ContactSerializer(ModelSerializer):

    class Meta:
        model=contacts

    fields = ['country_code', 'first_name', 'last_name', 'phone_number', 'contact_picture', 'is_favourite',]
