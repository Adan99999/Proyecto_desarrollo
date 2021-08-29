from app.wsgi import *

from django.test import TestCase
from core.models import Type, Employee
from core.models import *
# Create your tests here.
# Listar

 ################### video 10 ###############
#select * from Tabla #################
#query = Type.objects.all()
#print(query)

# insert ################
#t = Type()
#t.name = 'Prueba'
#t.save()


#Edit

#t = Type.objects.get(pk=1)
#t.name = 'President'
#t.save()

#try:
#     t = Type.objects.get(pk=1)
#     t.name = 'Prueva3'
#     t.save()
#except Exception as e:
#    print(e)



#eliminar/

#t = Type.objects.get(pk=1)
#t.delete()


#obj = Type.objects.filter(name__icontains='pre')


########### video 11 ##########################
##funciones basicas deun crud

#que enpiesen con.........espesificado si es con mayuscula o minuscla
#obj = Type.objects.filter(name__contains='Pre')
#print(obj)

#que enpiesen con. letra en especifico
#obj = Type.objects.filter(name__istartswith='P')
#print(obj)

#que empiezen con vocal o letra.........
#obj = Type.objects.filter(name__endswith='a')
#print(obj)

#muestra el query de la consulta
#obj = Type.objects.filter(name__icontains='terry').query
#print(obj)

#muestra el query de la consulta,,,excluye
#obj = Type.objects.filter(name__endswith='a').exclude(id=5)
#print(obj)


#iteracion
#for i in Type.objects.filter(name__endswith='a')[:2]:
#    print(i.name)


##que me excluya el empleado
#Employee.objects.filter(type_id=1)

#for i in Type.objects.filter(name__endswith='a')[:2]:
#    print(i.name)


for i in Category.objects.filter():
    print(i)