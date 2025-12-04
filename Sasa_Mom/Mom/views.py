from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .forms import MotherRegistrationForm
from .models import Mother, ChildVaccination, MessageLog
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_mother(request):
    if request.method == 'POST':
        form = MotherRegistrationForm(request.POST)
        if form.is_valid():
            mother = form.save()
            # Optionally queue a welcome message
            MessageLog.objects.create(mother=mother, phone=mother.phone, text=f"Welcome to {mother.hospital} — we will send reminders to this number.", status='queued')
            return redirect(('motherPage'))
    else:
        form = MotherRegistrationForm()
    return render(request, 'Mom/register.html', {'form': form})

@login_required
def motherPage(request,pk):
    # checks if mom exists
    mother = Mother.objects.get(id=pk)
    # this will bring up the upcoming child vaccinations only if mom exits
    vaccinations = ChildVaccination.objects.filter(child__mother=mother, completed=False).order_by('scheduled_date')[:1]
    context = {
        'mother': mother,
        'upcoming_vaccinations': vaccinations,
    }
    return render(request, 'Mom/mother.html', context)
