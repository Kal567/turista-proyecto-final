from pyswip import *
import ast
prolog = Prolog()
prolog.consult('turista_db.pl')

def get_list(l):
    res = []
    for e in l:
        res.append(e.value)
    return res


def buscar_restaurante(DondeEstoy, TipoEstablecimiento):
    res = []
    for restaurante in prolog.query("comida_bebida(Id,NombreEvento, TipoEvento,'" + TipoEstablecimiento + "', Provincia, '" + DondeEstoy + "', MinPrecioRango,MaxPrecioRango,TipoComida,Servicios, HoraIniciaLaboral, HoraFinalLaboral,HoraInicialFinde, HoraFinalFinde)"):
        tipo_comida = get_list(restaurante["TipoComida"])
        servicios = get_list(restaurante["Servicios"])
        res.append([restaurante['Id'],restaurante['NombreEvento'], 
        restaurante['TipoEvento'], TipoEstablecimiento, restaurante['Provincia'], 
        DondeEstoy, restaurante['MinPrecioRango'], restaurante['MaxPrecioRango'], 
        tipo_comida, servicios, restaurante['HoraIniciaLaboral'], restaurante['HoraFinalLaboral'], 
        restaurante['HoraInicialFinde'], restaurante['HoraFinalFinde']])
    return res

#print(buscar_restaurante('Playa Cabarete', 'restaurante'))     
 #============================================================================================================
#=============================================== EJERCICIO 1 ================================================
#============================================================================================================
"""
EJERCICIO 1 - 
    Con el presupuesto que tenemos para el día 
    ¿Hay algún sitio donde podríamos comer en 
    la playa de Cabarete, o cerca, que sea económico y 
    sirvan comida criolla y nos quede el 50% del mismo disponible 
    para otras actividades del día?
"""

def economico(Min, Max, Input):
    res = ''
    for e in prolog.query('economico(' + Min + ',' + Max + ',' + Input + ', Res)'):
        res = e['Res']
    if res == 'True':
        return True
    return False

#print(economico('5','10','5'))
#print(economico('5','10','1'))

def aqui_o_cerca(Lugar, Distancia):
    res = ''
    for e in prolog.query("distancia('"+Lugar+"',_Destino,Metros)"):
        res = e['Metros']
    if int(res) <= int(Distancia):
        return True
    return False

#print(aqui_o_cerca('Front Loop Cabarete', '100'))
#int(aqui_o_cerca('Galipote', '250'))

def ejercicio1(DondeEstoy: str, TipoEstablecimiento: str, ComidaBusco: str, Perimetro: str, 
                       Presupuesto: str, CriterioEconomico: str, Porciento: str):
    restaurantes = buscar_restaurante(DondeEstoy, TipoEstablecimiento)
    for r in restaurantes:
        if economico(str(r[6]), str(r[7]), str(CriterioEconomico)) and (ComidaBusco in r[8]) and int(CriterioEconomico) <= (int(Presupuesto) * float(Porciento)) and aqui_o_cerca(str(r[1]), str(Perimetro)):
            return "Si, existen restaurantes cerca con esta descripcion."
    return "No, no existen restaurantes cerca con esta descripcion."

print(ejercicio1('Playa Cabarete', 'restaurante', 'Criolla', '1000', '2200', '500', '0.5'))
print(ejercicio1('Playa Cabarete', 'restaurante', 'Criolla', '250', '2900', '60', '0.5'))

#============================================================================================================
#=============================================== EJERCICIO 2 ================================================
#============================================================================================================

"""
EJERCICIO 2 - 
    Con X cantidad de dinero ¿Qué actividades culturales 
    (obra de teatro, por ejemplo) podemos hacer esta semana 
    (cuáles y donde)?
"""
def arte_cultura_tipoEvento(TipoEvento):
    res = []
    for eventos in prolog.query("arte_cultura(IdEvento,Actividad,'" + TipoEvento + "',TipoEstablecimiento," +
        "Provincia,Ubicacion,Dias,Fecha,TipoTicket,TarifaTicket,Descripcion,HoraInicia,HoraTermina)"):
        res.append([eventos['IdEvento'],eventos['Actividad'], 
        TipoEvento, eventos['TipoEstablecimiento'], eventos['Provincia'], 
        eventos['Ubicacion'], eventos['Dias'], 
        eventos['Fecha'], eventos['TipoTicket'],
        eventos['TarifaTicket'], eventos['Descripcion'],
        eventos['HoraInicia'], eventos['HoraTermina']])
    return res

#print(arte_cultura_tipoEvento('arte_cultura'))

def sort(Input, order):
    if order == 'asc':
        for e in prolog.query("sort(0,=<," + str(Input) + ",Output)"):
            return list(e['Output'])
    if order == 'desc':
        for e in prolog.query("sort(0,>=," + str(Input) + ",Output)"):
                return list(e['Output'])

#l = sort([1,2,3,5,8], 'desc')
#print(l, l[0])

def get_eventos(order):
    eventos = arte_cultura_tipoEvento('arte_cultura')
    res = list(prolog.query("findall([TarifaTicket, Dias, IdEvento], arte_cultura(IdEvento, _Actividad, 'arte_cultura', _TipoEstablecimiento,_Provincia, _Ubicacion, Dias, _Fecha, _TipoTicket,TarifaTicket, _Descripcion, _HoraInicial, _HoraTermina),X)"))
    res = res[0]['X']
    if res:
        return sort(res,order)

#print(get_eventos('desc'))

def dias_semanas(n):#|||||||||||||||||||||||||||||AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    Hoy = int(n)
    semana = ''
    if Hoy>=1 and Hoy <= 7:
        semana =  'primera'
    if Hoy>=8 and Hoy <= 14:
        semana =  'segunda'
    if Hoy>=15 and Hoy <= 21:
        semana =  'tercera'
    if Hoy>=22 and Hoy <= 28:
        semana =  'cuarta'
    if Hoy>=29 and Hoy <= 31:
        semana =  'quinta'

    eventos = arte_cultura_tipoEvento('arte_cultura')
    res = list(prolog.query("findall(X, semanas_agosto('"+ semana+ "'" + ",X, _), RestoDias)"))
    res = res[0]['RestoDias']
    if res:
        return res
    

#print(dias_semanas(12))

def esta_semana(Hoy):
    diasSemanas = dias_semanas(Hoy)
    for e in prolog.query("dias_disponibles(" + str(diasSemanas) + ",[],RestoDias," + str(Hoy) + ")"):
        return e['RestoDias']

#print(esta_semana(12))

def arte_cultura_IdEvento(IdEvento):
    res = []
    for eventos in prolog.query("arte_cultura(" + str(IdEvento) + ",Actividad,TipoEvento,TipoEstablecimiento," +
        "Provincia,Ubicacion,Dias,Fecha,TipoTicket,TarifaTicket,Descripcion,HoraInicial, HoraTermina)"):
        res.append([IdEvento,eventos['Actividad'], 
        eventos['TipoEvento'], eventos['TipoEstablecimiento'], eventos['Provincia'], 
        eventos['Ubicacion'], eventos['Dias'], 
        eventos['Fecha'], eventos['TipoTicket'],
        eventos['TarifaTicket'], eventos['Descripcion'],
        eventos['HoraInicial'], eventos['HoraTermina']])
    return res

#print(arte_cultura_IdEvento(1))

def eventos_semana(Presupuesto, Hoy):
    dias_esta_semana = esta_semana(Hoy)
    eventos = get_eventos('asc')
    ids = []
    for e in eventos:
        tarifa, dia_evento, id_evento = e[0], e[1], e[2]
        evento = arte_cultura_IdEvento(id_evento)
        if dia_evento in dias_esta_semana and int(tarifa) <= int(Presupuesto) and (int(Presupuesto) - int(tarifa)) >= 0:
            Presupuesto = str(int(Presupuesto) - int(tarifa))
            ids.append(id_evento)
    res = []
    for e in ids:
        res.append(arte_cultura_IdEvento(e))
    return res

#print(eventos_semana(1000,7))


#============================================================================================================
#=============================================== EJERCICIO 3 ================================================
#============================================================================================================

def pelicula(Pelicula):
    output = []
    res = list(prolog.query("pelicula('" + Pelicula + "',Tipos)"))
    for e in res[0]['Tipos']:
        output.append(e.value)
    return output

#print(pelicula('endgame'))

def tipo_pelicula(lista, Tipo):
    res = list(prolog.query("tipodepelicula(" + str(lista) + "," + Tipo+")"))
    if str(res) == "[{}]":
        return True
    return False

#print(tipo_pelicula(['accion', 'ficcion'], 'accion')) #es accion uno de los generos en la lista? return True or False

def iterar_pelicula(EnCartelera, Genero):#si hay una pelicula con ese genero en la cartelera
    for peli in EnCartelera:
        generos_peli = pelicula(peli)
        if tipo_pelicula(generos_peli, Genero):
            return True
    return False

#print(iterar_pelicula(['endgame', 'avatar', 'marriage story', 'cinderella'], 'horror'))

def buscar_cines(Ubicacion, GeneroBusco, ToqueQueda):
    cines = []
    for e in prolog.query("buscarcines(Cine,'" + Ubicacion + "','" + GeneroBusco + "'," + str(ToqueQueda) +")"):
        #print(e['Cine'])
        cines.append(e['Cine'])
    return cines

#print(buscar_cines('Santo Domingo','ficcion',12))

#============================================================================================================
#=============================================== EJERCICIO 4 ================================================
#============================================================================================================

def bares_y_discotecas():
    output = []
    res = list(prolog.query("findall(Bar, bar(Bar,Ciudad,PrevioAvg,Puntuacion),Lista)"))
    res = res[0]['Lista']
    for e in res:
        output.append(e.value)
    return output

#print(bares_y_discotecas())

def buscar_bar_discoteca(Nombre):
    bd = []
    for e in prolog.query("bar('" + Nombre + "',Cuidad,PrecioAvg,Puntuacion)"):
        bd.append([Nombre, e['Cuidad'], e['PrecioAvg'],e['Puntuacion']])
    return bd

#print(buscar_bar_discoteca('Galipote'))

def buscar_bares_y_discotecas(a,b,c,Ciudad,e):
    Presupuesto, Perimetro, DineroNecesitoDia, CriterioCaro = int(a), int(b), int(c), int(e)
    output = []
    bardiscos = bares_y_discotecas()
    for e in bardiscos:
        bd = buscar_bar_discoteca(e)
        Nombre, Ciudad, PrecioAvg, Puntuacion = e, bd[0][1], bd[0][2], bd[0][3]
        #print(Nombre, Ciudad, PrecioAvg, Puntuacion)
        if aqui_o_cerca(str(Nombre),str(Perimetro)) and Puntuacion > 3 and CriterioCaro <= PrecioAvg and (PrecioAvg <= DineroNecesitoDia) and (Presupuesto - PrecioAvg) >= 0:
            Presupuesto -= PrecioAvg
            output.append(Nombre)
    return output

#print(buscar_bares_y_discotecas('5000', '250','4000','Santiago','1000'))
#print(buscar_bares_y_discotecas('8000', '250','4000','Santiago','1000'))

#============================================================================================================
#=============================================== PREGUNTAS EXTRA ================================================
#============================================================================================================

#============================================================================================================
#=============================================== PREGUNTA EXTRA: BUSCAR HOTELES POR CANTIDAD DE ESTRELLAS Y/O LUGAR ================================================
#============================================================================================================
def buscar_hoteles(Estrella, Lugar):
    cines = []
    if Lugar != ' ':
        for e in prolog.query("hotel(Hotel," + str(Estrella) + ",'" + str(Lugar) +"')"):
            cines.append(e['Hotel'])
    else:
        for e in prolog.query("hotel(Hotel," + str(Estrella) + ",Lugar)"):
            cines.append(e['Hotel'])
    return cines

#print(buscar_hoteles('5','Santo Domingo'))

#============================================================================================================
#=============================================== PREGUNTAS EXTRA: EVENTOS DE HOY ================================================
#============================================================================================================
def eventos_hoy(x, y, z):
    Presupuesto, Hoy, HoraActual = int(x), int(y), int(z)
    dias_esta_semana = esta_semana(Hoy)
    eventos = get_eventos('asc')
    ids = []
    for e in eventos:
        tarifa, dia_evento, id_evento = e[0], e[1], e[2]
        evento = arte_cultura_IdEvento(id_evento)
        horaInicia = evento[0][11]
        if dia_evento in dias_esta_semana and tarifa <= Presupuesto and Presupuesto - tarifa >= 0 and HoraActual <= int(horaInicia):
            Presupuesto -= tarifa
            ids.append(id_evento)
    res = []
    for e in ids:
        res.append(arte_cultura_IdEvento(e))
    return res

#print(eventos_hoy('1000','7','8'))

#============================================================================================================
#=============================================== PREGUNTA EXTRA: BUSCAR LUGARES EN MI PERIMETRO ================================================
#============================================================================================================
def miperimetro(DondeEstoy,Perimetro):
    res = []
    for e in prolog.query("distancia('"+DondeEstoy+"',Lugar,Metros)"):
        if int(e['Metros']) <= int(Perimetro):
            res.append(e['Lugar'])
    return res

#print(miperimetro('Lovera Bar', '1000'))