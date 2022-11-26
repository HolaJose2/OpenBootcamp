from django.db import models

class Salario(models.Model):
    monto = models.IntegerField(null=False,blank=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)

    def __str__(self):
        return self.monto

class Trabajo(models.Model):
    titulo = models.CharField(max_length=15, blank=False,null=False)
    descripcion = models.TextField(null=True)
    salario = models.ForeignKey(Salario,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Pais(models.Model):
    nombre = models.CharField(max_length=15, blank=False,null=False)
    codigo_pais = models.CharField(max_length=6, blank=False,null=False)

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=30, blank=False,null=False)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    

class Lugar(models.Model):
    nombre = models.CharField(max_length=30, blank=False,null=False)
    direccion = models.CharField(max_length=50, blank=False,null=False)
    codigo_postal = models.CharField(max_length=5, blank=False,null=False)
    Ubicacion = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Empleado(models.Model):
    id_number = models.CharField(max_length=10, blank=False,null=False)
    nombre = models.CharField(max_length=30, blank=False,null=False)
    apellido = models.CharField(max_length=30, blank=False,null=False)
    email = models.EmailField(max_length=30,blank=False,null=False)
    direccion = models.CharField(max_length=50,blank=False,null=False)
    trabajo = models.ForeignKey(Trabajo,on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name




