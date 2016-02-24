from django.shortcuts import render, get_object_or_404
from .models import Comanda, Subcomanda
from .forms import PersoanaForm

def pending_comanda(request):
	comenzi = Comanda.objects.all().filter(status__text='Deschis').order_by('data')
	return render(request,'orderhelper/pending_comanda.html', {'comenzi':comenzi})

def comanda_subcomenzi(request, pk):
	comanda = get_object_or_404(Comanda, pk=pk)
	# subcomenzi = Subcomanda.objects.all().filter(comanda_ref__numar_unic=476)
	subcomenzi = Subcomanda.objects.all().filter(comanda_ref__pk=pk)
	comanda = Comanda.objects.get(pk=pk)
	return render(request,'orderhelper/comanda_subcomenzi.html', {'subcomenzi':subcomenzi, 'comanda':comanda})


def persoana_new(request):
	form = PersoanaForm()
	return render(request,'orderhelper/persoana_new.html', {'form': form})

def add_home(request):
	return render(request,'orderhelper/add_home.html', {})
