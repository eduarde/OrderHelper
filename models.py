from django.db import models
from django.utils import timezone

class Status(models.Model):
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text

class Persoana(models.Model):
	nume = models.CharField('Nume', max_length=100)
	prenume = models.CharField('Prenume', max_length=100)
	telefon = models.CharField('Telefon', max_length=10)

	def __str__(self):
		return self.nume + ' ' + self.prenume;

class Proiect(models.Model):
	titlu = models.CharField('Denumire', max_length=255)
	descriere = models.TextField('Descriere', blank=True, null=True)
	telefon = models.CharField('Telefon', max_length=10, blank=True, null=True)

	def __str__(self):
		return self.titlu

class Producator(models.Model):
	nume = models.CharField('Nume', max_length=255)
	descriere = models.TextField('Descriere', blank=True, null=True)
	telefon = models.CharField('Telefon', max_length=10, blank=True, null=True)

	def __str__(self):
		return self.nume

class Furnizor(models.Model):
	nume = models.CharField('Nume', max_length=255)
	descriere = models.TextField('Descriere', blank=True, null=True)
	telefon = models.CharField('Telefon', max_length=10, blank=True, null=True)

	def __str__(self):
		return self.nume

class TermenPlata(models.Model):
	tip = models.CharField('Tip termen', max_length=50)

	def __str__(self):
		return self.tip

class ModPlata(models.Model):
	tip = models.CharField('Mod plata', max_length=50)

	def __str__(self):
		return self.tip

class Reper(models.Model):
	cod_reper = models.CharField('Cod reper', max_length=100, null=True)
	reper = models.TextField('Reper',null=True)

	def __str__(self):
		return self.cod_reper

class Subcomanda(models.Model):
	numar_curent = models.IntegerField()
	status = models.ForeignKey('Status',null=True)
	producator = models.ForeignKey('Producator', null=True)
	reper = models.ForeignKey('Reper', null=True)
	furnizor = models.ForeignKey('Furnizor', null=True)
	cantitate = models.DecimalField('Cantitate', default=0, max_digits=9, decimal_places=0, null=True)
	data_livrare = models.DateField('Data livrare',null=True)
	data_primire = models.DateField('Data primire',blank=True, null=True)
	pret = models.DecimalField('Pret', default=0, max_digits=9, decimal_places=6, null=True)
	link = models.URLField('Link',blank=True,null=True)
	facturat = models.DecimalField('Facturat', default=0, max_digits=9, decimal_places=6, null=True, blank=True)
	de_facturat = models.DecimalField('De facturat', default=0, max_digits=9, decimal_places=6, null=True, blank=True)
	tva_facturat = models.DecimalField('TVA Facturat', default=0, max_digits=9, decimal_places=6, null=True, blank=True)
	tva_de_facturat = models.DecimalField('TVA de Facturat', default=0, max_digits=9, decimal_places=6, null=True, blank=True)
	data_de_facturare = models.DateField('Data de facturare', null=True, blank=True)
	termen_plata = models.ForeignKey('TermenPlata', null=True)
	mod_plata = models.ForeignKey('ModPlata', null=True)

	def pret_total(self):
		self.pret * self.cantitate

	def calculate_late(self):
		self.data_primire - self.data_livrare 	

	def __str__(self):
		return 'Subcomanda #' + str(self.numar_curent)

