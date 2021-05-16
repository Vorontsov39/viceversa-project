from django.shortcuts import render


def home(requste):
	return render(requste, 'home.html')