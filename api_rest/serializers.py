from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *
#from django.contrib.auth.models import User


class UserSerializers(serializers.Serializer):
	id = serializers.ReadOnlyField()
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	username = serializers.CharField()
	email = serializers.EmailField()
	password = serializers.CharField()

	def create(self, validate_data):
		instance = User()
		instance.first_name = validate_data.get('first_name')
		instance.last_name = validate_data.get('last_name')
		instance.username = validate_data.get('username')
		instance.email = validate_data.get('email')
		instance.password = make_password(validate_data.get('password'))
		instance.save()
		return instance

	def validate_username(self, data):
		users = User.objects.filter(username = data)
		email = User.objects.filter(email = data)
		if (len(users) + len(email))==0:
			return data
		else:
			raise serializers.ValidationError("USUARIO YA REGISTRADO, INTENTELO DE NUEVO")
