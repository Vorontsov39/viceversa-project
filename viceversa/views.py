from django.shortcuts import render


def home(requste):
	return render(requste, 'home.html')

def reverse(requste):
	user_text = requste.GET['usertext']
	reverse_text = user_text[::-1]
	words = user_text.split()
	return render(requste, 'reverse.html', {'usertext':user_text, 'reversedtext': reverse_text, 'splittext': len(words)})