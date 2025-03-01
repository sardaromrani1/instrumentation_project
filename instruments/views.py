from django.shortcuts import render, redirect
from .models import Instrument
from .forms import InstrumentForm

# Create your views here.
def add_instrument(request):
    if request.method == "POST":
        form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()     # Save to database
            return redirect('instrument_list')      # Redirect to list view
    else:
        form = InstrumentForm()

    return render(request, 'instruments/add_instrument.html', {'form': form})

def instrument_list(request):
    instruments = Instrument.objects.all()      # Return all instruments
    return render(request, 'instruments/instrument_list.html', {'instruments': instruments})
