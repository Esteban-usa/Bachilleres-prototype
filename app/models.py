from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Universidad(models.Model):
    nombre = models.CharField(max_length=30)
    nit = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    class Meta:
        db_table = 'Universidad'
    def __str__(self):
        return self.nombre

class Facultad (models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    class   Meta:
        db_table = 'Facultad'
    def __str__(self):
        return self.nombre

class Union_U_F(models.Model):
    univeridad = models.ForeignKey(Universidad,on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultad,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['univeridad', 'facultad'], name='unique_foraneas_union')
        ]
    def __str__(self):
        return str(self.univeridad)+"_"+str(self.facultad)
    
class Fundacion(models.Model):
    Entidad = 'Entidad'
    Universidad = 'Universidad'
    OPCIONES_TIPO = [
        (Entidad, 'Entidad'),
        (Universidad, 'Universidad'),
    ]
    nombre = models.CharField(max_length=30)
    tipo =  models.CharField(max_length=20,choices=OPCIONES_TIPO,default=Universidad)
    def __str__(self):
        return self.nombre

    
class Beca (models.Model):
    Nacional = 'Nacional'
    Extranjera = 'Extranjera'
    OPCIONES_TIPO = [
        (Nacional, 'Nacional'),
        (Extranjera, 'Extranjera'),
    ]
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10,choices=OPCIONES_TIPO,default=Nacional)
    monto = models.IntegerField()
    class Meta:
        db_table = 'Becas'
    def __str__(self):
        return self.nombre
    
class Configuracion_Becas(models.Model):
    Union_U_F = models.ForeignKey(Union_U_F, on_delete=models.CASCADE)
    Beca = models.ForeignKey(Beca, on_delete=models.CASCADE)
    Fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Union_U_F', 'Beca','Fundacion'], name='unique_foraneas_configuracion')
        ]
    def __str__(self):
        return str(self.Union_U_F)+"_"+str(self.Beca)+"_"+str(self.Fundacion)

    
class Favoritos (models.Model):
    facultad = 'facultad'
    beca = 'beca'
    OPCIONES_TIPO = [
        (facultad, 'facultad'),
        (beca, 'beca'),
    ]
    tipo = models.CharField(max_length=10,choices=OPCIONES_TIPO)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Configuracion_Becas = models.ForeignKey(Configuracion_Becas, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'Configuracion_Becas','tipo'], name='unique_foraneas_favoritos'),
        ]
    def __str__(self):
        return self.tipo+"_"+str(self.usuario)


