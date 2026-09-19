"""
Vistas para la landing page de Escuela Oaxaqueña del Café.
"""
from django.views.generic import TemplateView
from .models import Coordinador, Programa, Evento, Testimonio, GaleriaItem


class LandingView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coordinadores'] = Coordinador.objects.all()
        context['programas'] = Programa.objects.filter(publicado=True)
        context['eventos'] = Evento.objects.filter(publicado=True)
        context['testimonios'] = Testimonio.objects.filter(publicado=True)
        context['galeria'] = GaleriaItem.objects.filter(publicado=True)
        return context
