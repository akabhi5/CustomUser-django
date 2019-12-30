from django.shortcuts import render
from .forms import SignUpForm

def index(request):
    return render(request, 'index.html')

def sign_up_view(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)

		user = form.save()
		user.set_password(user.password)
		user.save()
		return render(request, 'index.html')
	return render(request, 'signup.html', {'form': form})