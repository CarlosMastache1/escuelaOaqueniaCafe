"""
Comando de gestión para cargar datos semilla de la Escuela Oaxaqueña del Café.
Ejecutar: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from datetime import date
from landing.models import Coordinador, Programa, Evento, Testimonio, GaleriaItem


class Command(BaseCommand):
    help = 'Carga datos semilla iniciales para la Escuela Oaxaqueña del Café'

    def handle(self, *args, **kwargs):
        self.cargar_coordinadores()
        self.cargar_programas()
        self.cargar_eventos()
        self.cargar_testimonios()
        self.cargar_galeria()
        self.stdout.write(self.style.SUCCESS('Datos semilla cargados exitosamente.'))

    def cargar_coordinadores(self):
        Coordinador.objects.all().delete()
        Coordinador.objects.create(
            nombre='Efraín Aragón Ibáñez',
            cargo='Coordinador Escuela Oaxaqueña del Café',
            bio=(
                'Efraín Aragón Ibáñez es el coordinador de la Escuela Oaxaqueña del Café, '
                'que forma parte del equipo técnico de la Secretaría de Fomento Agroalimentario '
                'y Desarrollo Rural (Sefader). Su propósito es formar capital humano que participe '
                'en la cadena productiva del café para elevar la calidad de los servicios desde '
                'el cultivo hasta el consumo.'
            ),
            orden=1,
        )
        self.stdout.write(self.style.SUCCESS('  - Coordinadores creados'))

    def cargar_programas(self):
        Programa.objects.all().delete()
        programas = [
            {
                'titulo': 'Cata Sensorial',
                'slug': 'cata-sensorial',
                'descripcion_corta': 'Desarrolla el sentido del gusto y olfato para identificar aroma, sabor y defectos del café de especialidad.',
                'descripcion_completa': 'Aprende a identificar los perfiles sensoriales del café, analizando aroma, sabor, acidos, cuerpos y defectos. La cata es un proceso mediante el cual se analiza el aroma, sabor y demás atributos del café.',
                'orden': 1,
            },
            {
                'titulo': 'Barismo y Preparación',
                'slug': 'barismo-preparacion',
                'descripcion_corta': 'Domina las técnicas de extracción y preparación del café para ofrecer la mejor experiencia sensorial.',
                'descripcion_completa': 'Aprende desde los fundamentos del barismo hasta técnicas avanzadas de preparación: espresso, pour-over, French press, prensa de inmersión y más.',
                'orden': 2,
            },
            {
                'titulo': 'Cafeticultura Sostenible',
                'slug': 'cafeticultura-sostenible',
                'descripcion_corta': 'Prácticas agroecológicas que preservan el medio ambiente y mejoran la calidad del grano.',
                'descripcion_completa': 'Más del 90% del café en Oaxaca se cultiva bajo sombra, preservando bosques y selvas. Aprende técnicas sostenibles de cultivo, manejo de sombra y conservación de suelos.',
                'orden': 3,
            },
            {
                'titulo': 'Comercio Directo',
                'slug': 'comercio-directo',
                'descripcion_corta': 'Conectamos productores con consumidores especializados para un comercio justo y transparente.',
                'descripcion_completa': 'Fortalecemos el vínculo entre productores y compradores, eliminando intermediarios y garantizando precios justos para las y los cafeticultores.',
                'orden': 4,
            },
        ]
        for prog in programas:
            Programa.objects.create(**prog)
        self.stdout.write(self.style.SUCCESS('  - Programas creados'))

    def cargar_eventos(self):
        Evento.objects.all().delete()
        Evento.objects.create(
            titulo='Convención del Café Oaxaqueño 2026',
            fecha=date(2026, 8, 14),
            ubicacion='Plaza de la Danza, Oaxaca de Juárez',
            descripcion=(
                'Encuentro que impulsa la comercialización directa, el consumo y el posicionamiento '
                'nacional e internacional del café de especialidad. Incluye catas y degustaciones, '
                'subasta de microlotes y talleres de divulgación científica. Participan productores, '
                'compradores especializados, tostadores, baristas e investigadores.'
            ),
            enlace='https://www.gob.mx/agricultura',
            publicado=True,
            orden=1,
        )
        self.stdout.write(self.style.SUCCESS('  - Eventos creados'))

    def cargar_testimonios(self):
        Testimonio.objects.all().delete()
        testimonios = [
            {
                'nombre': 'Martha Patricia Cruz',
                'cargo': 'Productora cafetalera, San Juan Bautista Tuxtepuxos',
                'texto': 'Gracias a las capacitaciones de la Escuela Oaxaqueña del Café, hemos mejorado la calidad de nuestro grano en un 40% y hemos podido comercializar directamente a precios justos.',
                'orden': 1,
            },
            {
                'nombre': 'Heladio García España',
                'cargo': 'Barista y tostador, Taller de Barismo Oaxaca',
                'texto': 'La Escuela Oaxaqueña del Café nos enseñó a identificar los perfiles sensoriales de cada región. Ahora nuestros cafés destacan en todo el país.',
                'orden': 2,
            },
            {
                'nombre': 'Efraín Aragón Ibáñez',
                'cargo': 'Coordinador Escuela Oaxaqueña del Café, Sefader Oaxaca',
                'texto': 'Oaxaca continúa consolidándose como referente nacional al obtener el primer lugar en el Certamen Nacional Taza de Excelencia en 2023 y 2024.',
                'orden': 3,
            },
        ]
        for i, test in enumerate(testimonios):
            Testimonio.objects.create(**test)
        self.stdout.write(self.style.SUCCESS('  - Testimonios creados'))

    def cargar_galeria(self):
        GaleriaItem.objects.all().delete()
        galeria = [
            {'titulo': 'Cafetal en Oaxaca', 'descripcion': 'Cultivo bajo sombra'},
            {'titulo': 'Tostado de café', 'descripcion': 'Procesamiento'},
            {'titulo': 'Barista preparando café', 'descripcion': 'Barismo'},
            {'titulo': 'Café recién servido', 'descripcion': 'Degustación'},
            {'titulo': 'Productores cafetaleros', 'descripcion': 'Productores'},
            {'titulo': 'Café de especialidad', 'descripcion': 'Especialidad'},
        ]
        for i, item in enumerate(galeria):
            GaleriaItem.objects.create(**item)
        self.stdout.write(self.style.SUCCESS('  - Galería creada'))
