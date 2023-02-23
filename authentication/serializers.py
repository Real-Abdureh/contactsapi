from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length= 200, min_length=8,write_only=True)
    email = serializers.EmailField(max_length=200, min=3)
    first_name = serializers.CharField(max_length=200, min_length=3)
    last_name = serializers.CharField(max_length=200, min_length=3)