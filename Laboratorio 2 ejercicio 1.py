#Anthony Dialessandro Ortiz Calderon Jhonatan Enrique Hernandez Pineda
#Datos de el costo de un articulo vendido y la cantidad de dinero entregado al cliente
#El cambio que se debe entregar si sobra
#cuando lo da exacto
#la cantidad de dinero que falta por pagar si no es exacto
menu = input ('''
            Menu de articulo de herramienta
            1-Aceite motul.....$35
            2-Llanta.....$70
            3-Fajas.....$11
            4-Llave cruz.....$17
            5-Jack 2 ton.....$50
            ingresa el articulo que quieras comprar -> ''').lower

pre=float(input("Ingrese el precio del artículo: "))
pag=float(input("'¿Cuánto ha pagado el cliente? "))

cambio=pag-pre
faltante=pre-pag


if (cambio<0):
    print ("Falta dinero en el pago. El dinero faltante es ",faltante)

elif (cambio==0):
    print ("Se ha completado exitosamente su compra")

if (cambio>0):
    print ("Se ha completado exitosamente su compra, el cambio a dar es ",cambio)

