from Facturacion.models import *

#FORMA 1
#INSERTAR PRODUCTO
P= Producto(descripcion='Aceite Girazol',precio=1.50,stock=200)
P.save()

P1= Producto(descripcion='Aceite la favorita',precio=1.70,stock=200)
P1.save()

P2= Producto(descripcion='Aceite El oro',precio=1.20,stock=200)
P2.save()

P3= Producto(descripcion='Aceite amarillo',precio=1.40,stock=200)
P3.save()
#FORMA 2 INSERTAR PRODUCTO
Producto.objects.create(descripcion='Coca Cola',precio=0.90,stock=10000)

Producto.objects.create(descripcion='Cola Pepsy',precio=0.90,stock=10000)

Producto.objects.create(descripcion='Cola Fanta',precio=0.90,stock=10000)

Producto.objects.create(descripcion='Cola Manzana',precio=0.90,stock=10000)



#INSERTAR CLIENTE FORMA 1
c1=Cliente(nombre='david cortez',ruc='0123456789',direccion='milagro')
c1.producto_set=P1
c1.save()

c2=Cliente(nombre='pepe piguabe',ruc='9876543210',direccion='milagro')
c2.producto_set=P2
c2.save()

c3=Cliente(nombre='maria rosa',ruc='7896541230',direccion='milagro')
c3.producto_set=P3
c3.save()

c4=Cliente(nombre='estefi',ruc='1478523690',direccion='milagro')
c4.producto_set=P
c4.save()
#INSERTAR CLIENTE FORMA 2
c5=Cliente.objects.create(nombre='maria magdale',ruc='753159846210',direccion='milagro')
c6=Cliente.objects.create(nombre='alita perez',ruc='359628754102',direccion='milagro')
c7=Cliente.objects.create(nombre='lola piguabez',ruc='321458779541',direccion='milagro')
c8=Cliente.objects.create(nombre='greyci rendon',ruc='852159365487',direccion='milagro')

#INSERTAR FACTURA FORMA 1
f1=Factura(cliente=c5,fecha='2016-02-05',total=10.00)
f1.save()

f2=Factura(cliente=c6,fecha='2016-02-04',total=10.00)
f2.save()

f3=Factura(cliente=c7,fecha='2016-02-03',total=10.00)
f3.save()

f4=Factura(cliente=c8,fecha='2016-02-07',total=10.00)
f4.save()
#INSERTAR FACTURA FORMA 2
f5=Factura.objects.create(cliente=c1,fecha='2020-03-01',total=10.00)
f6=Factura.objects.create(cliente=c2,fecha='2019-04-02',total=100.00)
f7=Factura.objects.create(cliente=c3,fecha='2018-05-03',total=120.00)
f8=Factura.objects.create(cliente=c4,fecha='2017-06-04',total=130.00)


#INSERTAR DETALLEFACTURA FORMA 1
d1=DetalleFactura(factura=f1,producto=P,cantidad=50,precio=150,subtotal=800)
d1.save()
d2=DetalleFactura(factura=f2,producto=P1,cantidad=20,precio=70,subtotal=700)
d2.save()
d3=DetalleFactura(factura=f3,producto=P2,cantidad=10,precio=10,subtotal=200)
d3.save()
d4=DetalleFactura(factura=f4,producto=P3,cantidad=15,precio=10,subtotal=2900)
d4.save()

#INSERTAR DETALLEFACTURA FORMA 2
d5=DetalleFactura.objects.create(factura=f5,producto=P1)
d6=DetalleFactura.objects.create(factura=f6,producto=P2)
d7=DetalleFactura.objects.create(factura=f7,producto=P3)
d8=DetalleFactura.objects.create(factura=f8,producto=P)

#MODIFICAR REGISTROS PRODUCTO
#FORMA 1
p1 = Producto.objects.get(id=1)
p1.precio=1.3
p1.save()

p2 = Producto.objects.get(id=2)
p2.precio=2.3
p2.save()
#FORMA 2
Producto.objects.filter(id=3).update(precio=2.6)
Producto.objects.filter(id=4).update(precio=4.3)

#MODIFICAR REGISTRO CLIENTE
#FORMA 1
C1 = Cliente.objects.get(id=1)
C1.direccion='manuel azcazubi'
C1.save()

C2 = Cliente.objects.get(id=2)
C2.direccion='av 17 de septiembre'
C2.save()
#FORMA 2
Cliente.objects.filter(id=3).update(direccion='Milagro modificado')
Cliente.objects.filter(id=4).update(direccion='Modificado Troncal')

#MODIFICAR REGISTRO FACTURA
#FORMA 1
F1 = Factura.objects.get(id=1)
F1.total=1500
F1.save()

F2 = Factura.objects.get(id=2)
F2.total=1600
F2.save()
#FORMA 2
Factura.objects.filter(id=3).update(total=350)
Factura.objects.filter(id=4).update(total=250)


#MODIFICAR REGISTRO FACTURA
#FORMA 1
F1 = Factura.objects.get(id=1)
F1.total=1500
F1.save()

F2 = Factura.objects.get(id=2)
F2.total=1600
F2.save()
#FORMA 2
Factura.objects.filter(id=3).update(total=350)
Factura.objects.filter(id=4).update(total=250)

#MODIFICAR REGISTRO DETALLEFACTURA
#FORMA 1
d1 = DetalleFactura.objects.get(id=1)
d1.cantidad=15
d1.save()

d2 = DetalleFactura.objects.get(id=2)
d2.cantidad=16
d2.save()
#FORMA 2
DetalleFactura.objects.filter(id=3).update(cantidad=35)
DetalleFactura.objects.filter(id=4).update(cantidad=25)


#ELIMINAR REGISTRO  PRODUCTO
#FORMA 1
p=Producto.objects.get(id=1)
p.delete()
#FORMA 2
Producto.objects.filter(id=2).delete()

#ELIMINAR REGISTRO  CLIENTE
#FORMA 1
c=Cliente.objects.get(id=1)
c.delete()
#FORMA 2
Cliente.objects.filter(id=2).delete()

#ELIMINAR REGISTRO  FACTURA
#FORMA 1
F=Factura.objects.get(id=1)
F.delete()
#FORMA 2
Factura.objects.filter(id=2).delete()

#ELIMINAR REGISTRO  DETALLEFACTURA
#FORMA 1
D=DetalleFactura.objects.get(id=1)
D.delete()
#FORMA 2
DetalleFactura.objects.filter(id=2).delete()

#Querys de un modelo
p=Producto.objects.all()
p=Producto.objects.get(id=2)
Producto.objects.filter(id__lte=2)
Producto.objects.exclude(descripcion__icontains='Cola')
Producto.objects.filter(id__gte=4)
Producto.objects.filter(id__gt=4).values('id','descripcion')
Producto.objects.filter(id__lt=4).values('id','descripcion')
Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')

#Querys de varios modelos (relacionados)
Factura.objects.filter(cliente__nombre='')
c= Cliente.objects.get(nombre='greyci rendon')
c.factura_set.all()
c.factura_set.filter(id=2)
Factura.objects.select_related('cliente').filter(cliente__nombre='Daniel Vera')
Cliente.objects.prefetch_related('producto').filter(nombre='greyci rendon').values('nombre','producto__descripcion')
