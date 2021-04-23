from django.shortcuts import render
from .forms import NewDeafForm

# Create your views here.
def create(request):
    deaf = None
    if(request.method == 'POST'):
        form = NewDeafForm(request.POST)
        if form.is_valid():
            deaf = form.save()
        else:
            return render(request, 'auth/register.html', {'form': form, 'deaf': 'error'})
    
    form = NewDeafForm()
    return render(request, 'auth/register.html', {'form': form, 'deaf': deaf})
