from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "Nombre: {0} - {1}"
        return txt.format(self.nombre,self.categoria_id)


class Producto(models.Model):
    sku = models.CharField(primary_key=True,max_length=15)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=120)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagenUrl = models.ImageField(upload_to="imagenesProducto")

    def __str__(self):
        txt = "Producto N° {0} - Stock {1} - Precio {2} - fecha {3}"
        return txt.format(self.sku,self.stock,self.precio,self.fecha)
    
class Stock(models.Model):
    material = models.CharField(max_length=500)
    unidad = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        txt = "Producto N° {0} - Stock {1} - Precio {2} - fecha {3}"
        return txt.format(self.material,self.unidad,self.cantidad)


    