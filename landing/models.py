from django.db import models


class Coordinador(models.Model):
    nombre = models.CharField(max_length=120, verbose_name='Nombre')
    cargo = models.CharField(max_length=120, verbose_name='Cargo / Rol')
    bio = models.TextField(verbose_name='Biografía')
    foto = models.ImageField(upload_to='coordinadores/', blank=True, null=True, verbose_name='Foto')
    orden = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Coordinador'
        verbose_name_plural = 'Coordinadores'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.cargo})'


class Programa(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    descripcion_corta = models.TextField(verbose_name='Descripción corta')
    descripcion_completa = models.TextField(blank=True, verbose_name='Descripción completa')
    icono = models.CharField(max_length=50, blank=True, verbose_name='Clase de icono (opcional)')
    imagen = models.ImageField(upload_to='programas/', blank=True, null=True, verbose_name='Imagen')
    publicado = models.BooleanField(default=True, verbose_name='¿Publicado?')
    orden = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo


class Evento(models.Model):
    titulo = models.CharField(max_length=150, verbose_name='Título')
    fecha = models.DateField(verbose_name='Fecha')
    ubicacion = models.CharField(max_length=200, verbose_name='Ubicación')
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True, verbose_name='Imagen')
    enlace = models.URLField(blank=True, verbose_name='Enlace externo')
    publicado = models.BooleanField(default=True, verbose_name='¿Publicado?')
    orden = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['fecha', 'orden']

    def __str__(self):
        return self.titulo


class Testimonio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    cargo = models.CharField(max_length=100, blank=True, verbose_name='Cargo / Empresa')
    texto = models.TextField(verbose_name='Testimonio')
    foto = models.ImageField(upload_to='testimonios/', blank=True, null=True, verbose_name='Foto')
    publicado = models.BooleanField(default=True, verbose_name='¿Publicado?')
    orden = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class GaleriaItem(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='galeria/', blank=True, null=True, verbose_name='Imagen')
    descripcion = models.CharField(max_length=200, blank=True, verbose_name='Descripción')
    publicado = models.BooleanField(default=True, verbose_name='¿Publicado?')
    orden = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Elemento de galería'
        verbose_name_plural = 'Galería'
        ordering = ['orden', 'titulo']

    def __str__(self):
        return self.titulo
