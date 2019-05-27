from django.db import models

class Productos(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()
    origen = models.CharField(max_length=50)
    imagen = models.URLField(default="")
    precio = models.PositiveIntegerField(default="0")
    paypal_id = models.CharField(max_length=10, default='0')


    def __str__(self):
        return '{0} / {1} / Quedan: {2}'.format(self.codigo,self.nombre,self.cantidad)


class Cliente(models.Model):
    id= models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=40,verbose_name='Nombre(s)')
    apellido = models.CharField(max_length=40,verbose_name='Apellido')
    email = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.TextField(default="Escriba su direccion..")


    def __str__(self):
        return '{0} / {1}'.format(self.id,self.nombre)

class Pago(models.Model):
    idpago = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False,blank=False)
    PAGOS_ACEPTADOS = (
        ('Credito', 'Tarjeta de credito'),
        ('PayPal', 'Paypal')
    )
    Tipo_pago = models.CharField(max_length=40,choices=PAGOS_ACEPTADOS,default='Credito')
    fecha=models.DateField(auto_now=True)

    def build_id(self):
        return (('CROCOMX-' + self.fecha) + '-' + str(self.idpago))
    codigo_rastreo = models.CharField(max_length=15, default=(build_id))


class Compra(models.Model):
    No_Compra = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False,blank=False)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE,null=False,blank=False)
    fecha=models.DateField(auto_now=True)

    def __str__(self):
        return '{0} / ${1} / Cliente: {2}'.format(self.No_Compra,self.monto,self.cliente)

