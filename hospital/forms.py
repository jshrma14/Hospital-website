from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ApForm(ModelForm):
	class Meta:
		model = Appointment
		fields = '__all__'

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']