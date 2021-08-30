comida_bebida(1, 'Swai restaurant and bar', 'comida_bebida', 'restaurante', 'Puerto Plata', 'Playa Cabarete', 225, 650, ['Mariscos'], ['Dine In', 'Takeaway'], 5, 22, 5, 21).
comida_bebida(2, 'The Honey Company', 'comida_bebida', 'restaurante', 'Puerto Plata', 'Playa Cabarete', 60, 450, ['Cafe', 'Postres'], ['Dine In', 'Takeaway', 'Delivery'], 10, 14, 10, 14).
comida_bebida(3, 'Front Loop Cabarete', 'comida_bebida', 'restaurante', 'Puerto Plata', 'Playa Cabarete', 150, 780, ['Mariscos', 'Cafe', 'Grill', 'Criolla'], ['Dine In', 'Takeaway'], 8, 21, 8, 21).
comida_bebida(4, 'Bliss', 'evento', 'comida_bebida', 'Puerto Plata', 'Playa Cabarete', 690, 2390, ['Mariscos', 'Grill', 'Criolla'], ['Dine In', 'Takeaway', 'Al aire libre', ' Delivery '], 5, 22, 5, 21).
comida_bebida(5, 'La Casita de Papi', 'comida_bebida', 'restaurante', 'Puerto Plata', 'Playa Cabarete', 380, 970, ['Mariscos', 'Grill', 'Criolla'], ['Dine In', 'Takeaway'], 23, 23, 23, 23).

bar('Lovera Bar','Santiago',2500,2).
bar('Tgi Fridays','Santiago',4000,4).
bar('Soda','Santiago',3500,4).
bar('Galipote','Santiago',3500,5).
bar('Cheers','Santiago',2500,4).

baresydiscotecas(Lista):- findall(Bar,bar(Bar,_Ciudad,_PrecioAvg,_Puntuacion),Lista).
mibuscar(_Presupuesto,_Perimetro,_DineroNecesitoDia,_Ciudad,_CriterioCaro,[],Res,Res):-!.
mibuscar(Presupuesto, Perimetro, DineroNecesitoDia,Ciudad,CriterioCaro,[X|Y],Pares,Res):-
   bar(X,Ciudad,PrecioAvg,Puntuacion),
   aquiOcerca(X, Perimetro),
   Puntuacion > 3,
   CriterioCaro =< PrecioAvg,
   PrecioAvg =< DineroNecesitoDia,
   NuevaCantidadDinero is Presupuesto - PrecioAvg,
   mibuscar(NuevaCantidadDinero,Perimetro,DineroNecesitoDia,Ciudad,CriterioCaro,Y,[X|Pares],Res).
mibuscar(Presupuesto,Perimetro,DineroNecesitoDia,Ciudad,CriterioCaro,[_|Y],Pares,Res):-
   mibuscar(Presupuesto,Perimetro,DineroNecesitoDia,Ciudad,CriterioCaro,Y,Pares,Res).


distancia('Playa Cabarete', 'Swai restaurant and bar', 350).
distancia('Swai restaurant and bar', 'Playa Cabarete', 350).
distancia('Playa Cabarete', 'The Honey Company', 450).
distancia('The Honey Company', 'Playa Cabarete', 450).
distancia('Playa Cabarete', 'Front Loop Cabarete', 950).
distancia('Front Loop Cabarete', 'Playa Cabarete', 950).
distancia('Playa Cabarete', 'Bliss', 250).
distancia('Bliss', 'Playa Cabarete', 250).
distancia('Playa Cabarete', 'La Casita de Papi', 950).
distancia('La Casita de Papi', 'Playa Cabarete', 950).

distancia('Lovera Bar','Tgi Fridays',500).
distancia('Tgi Fridays', 'Soda', 200).
distancia('Soda','Galipote',300).
distancia('Galipote','Cheers',150).
distancia('Cheers','Galipote',150).
distancia('Lovera Bar','Amnesia',41).
distancia('Lovera Bar','Pachanga',250).
distancia('Lovera Bar','Ricos Plaza',1310).
distancia('Lovera Bar','punto sport',851).
distancia('Lovera Bar','BIRRAS',785).
distancia('Lovera Bar','Yaas!',1540).

economico(Min,Max,Input,Res):- (Max=<Input); (Input>=Min, Input=<Max), Res = 'True'.
aquiOcerca(Lugar, Distancia):- distancia(Lugar, _Destino, Metros), Metros=<Distancia.
isInList([X],Target):- Target = X, !.
isInList([X|Y],Target):- Target = X, !; isInList(Y,Target).

cincuentaporciento(DondeEstoy, TipoEstablecimiento, ComidaBusco, Perimetro, Presupuesto, CriterioEconomico, Porciento, Res):-
    comida_bebida(_Id, NombreEvento, _TipoEvento, TipoEstablecimiento, _Provincia, DondeEstoy, MinPrecioRango, MaxPrecioRango,
                  TipoComida,_Servicios, _HoraIniciaLaboral, _HoraFinalLaboral, _HoraIniciaFinde, _HoraFinalFinde),
    economico(MinPrecioRango, MaxPrecioRango,CriterioEconomico),
    isInList(TipoComida,ComidaBusco),
    MitadPresupuesto is Presupuesto*Porciento, 
    CriterioEconomico=<MitadPresupuesto, aquiOcerca(NombreEvento, Perimetro),Res = 'True', !.
cincuentaporciento(_DondeEstoy, _TipoEstablecimiento, _ComidaBusco, _Perimetro, _Presupuesto, _CriterioEconomico, _Porciento, Res):- Res = 'False', !.

semanas_agosto(primera, 1, laboral).
semanas_agosto(primera, 2, laboral).
semanas_agosto(primera, 3, laboral).
semanas_agosto(primera, 4, laboral).
semanas_agosto(primera, 5, laboral).
semanas_agosto(primera, 6, laboral).
semanas_agosto(primera, 7, finde).
semanas_agosto(segunda, 8, finde).
semanas_agosto(segunda, 9, laboral).
semanas_agosto(segunda, 10, laboral).
semanas_agosto(segunda, 11, laboral).
semanas_agosto(segunda, 12, laboral).
semanas_agosto(segunda, 13, laboral).
semanas_agosto(segunda, 14, finde).
semanas_agosto(tercera, 15, finde).
semanas_agosto(tercera, 16, laboral).
semanas_agosto(tercera, 17, laboral).
semanas_agosto(tercera, 18, laboral).
semanas_agosto(tercera, 19, laboral).
semanas_agosto(tercera, 20, laboral).
semanas_agosto(tercera, 21, finde).
semanas_agosto(cuarta, 22, finde).
semanas_agosto(cuarta, 23, laboral).
semanas_agosto(cuarta, 24, laboral).
semanas_agosto(cuarta, 25, laboral).
semanas_agosto(cuarta, 26, laboral).
semanas_agosto(cuarta, 27, laboral).
semanas_agosto(cuarta, 28, finde).
semanas_agosto(quinta, 29, finde).
semanas_agosto(quinta, 30, laboral).
semanas_agosto(quinta, 31, laboral).

cual_semana(Hoy, Semana):- Hoy>=1, Hoy=<7, Semana = 'primera', !.
cual_semana(Hoy, Semana):- Hoy>=8, Hoy=<14, Semana = 'segunda', !.
cual_semana(Hoy, Semana):- Hoy>=15, Hoy=<21, Semana = 'tercera', !.
cual_semana(Hoy, Semana):- Hoy>=22, Hoy=<28, Semana = 'cuarta', !.
cual_semana(Hoy, Semana):- Hoy>=29, Hoy=<31, Semana = 'quinta', !.

dias_semana(Hoy, RestoDias):- cual_semana(Hoy,Semana), findall(X, semanas_agosto(Semana, X, _), RestoDias).%retorna todos los dias de esa semana
dias_disponibles([],Res,Res,_Hoy):- !,true.%retorna todos los dias de hoy y el futuro, es decir, sin los dias que ya pasaron en una lista que viene de la regla 'dias_semana'
dias_disponibles([X|Y],Pares,Res,Hoy):- X>=Hoy, dias_disponibles(Y,[X|Pares],Res,Hoy),!,true.
dias_disponibles([_|Y],Pares,Res,Hoy):- dias_disponibles(Y,Pares,Res,Hoy).

arte_cultura(1,'Hay que Deshacer la Casa','arte_cultura','obra de teatro','Santo Domingo','Teatro Nacional Eduardo Brito',5,'05-08-2021', 'General',1085,'Dos hermanas distanciadas por los anos y las experiencias vividas, se rencuentran en la casa familiar tras la muerte de su madre, porque hay que repartir la herencia y deshacer la casa. La obra se presenta a beneficio de la Fundacion Manos Arrugadas.',20,22).
arte_cultura(2,'Hay que Deshacer la Casa','arte_cultura','obra de teatro','Santo Domingo','Teatro Nacional Eduardo Brito',6,'06-08-2021', 'General',1085,'Dos hermanas distanciadas por los anos y las experiencias vividas, se rencuentran en la casa familiar tras la muerte de su madre, porque hay que repartir la herencia y deshacer la casa. La obra se presenta a beneficio de la Fundacion Manos Arrugadas.',20,22).
arte_cultura(3,'Hay que Deshacer la Casa','arte_cultura','obra de teatro','Santo Domingo','Teatro Nacional Eduardo Brito',7,'07-08-2021', 'General',1085,'Dos hermanas distanciadas por los anos y las experiencias vividas, se rencuentran en la casa familiar tras la muerte de su madre, porque hay que repartir la herencia y deshacer la casa. La obra se presenta a beneficio de la Fundacion Manos Arrugadas.',20,22).
arte_cultura(4,'Leones de Santo Domingo', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',4,'04-08-2021', 'General', 230, 'Liga Nacional de Baloncesto', 21,23).
arte_cultura(5,'Leones de Santo Domingo', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',11,'11-08-2021', 'General', 230, 'Liga Nacional de Baloncesto', 21,23).
arte_cultura(6,'Leones de Santo Domingo', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',15,'15-08-2021', 'General', 230, 'Liga Nacional de Baloncesto', 20,23).
arte_cultura(7,'Leones de Santo Domingo', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',25,'25-08-2021', 'General', 230, 'Liga Nacional de Baloncesto', 19,23).
arte_cultura(8,'Leones de Santo Domingo', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',4,'04-08-2021', 'General', 230, 'Liga Nacional de Baloncesto', 21,23).
arte_cultura(9,'Obsesiones', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Casa de Teatro',6,'06-08-2021', 'General', 760, 'Obra de teatro para mayores de 13 años',19,21).
arte_cultura(10,'Obsesiones', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Casa de Teatro',7,'07-08-2021', 'General', 760, 'Obra de teatro para mayores de 13 años',19,21).
arte_cultura(11,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'PLATEA DERECHA (Filas A Hasta N)', 7415, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(12,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'PLATEA CENTRO (Filas A Hasta N)', 7415, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(13,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'PLATEA IZQDA (Filas A Hasta N)', 7415, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(14,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'PLATEA DERECHA (Filas O Hasta BB)', 6355, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(15,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'PLATEA CENTRO (Filas O Hasta BB)', 6355, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(16,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'PLATEA IZQDA (Filas O Hasta BB)', 6355, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(17,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'BALCON DERECHO', 4240, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(18,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'BALCON CENTRO', 4240, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(19,'Fito Paez Un Hombre Con Un Piano Tour 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Teatro Nacional',6,'06-08-2021', 'BALCON IZQDO', 4240, 'Fito Paez Un Hombre Con Un Piano Tour 2021',19,21).
arte_cultura(20,'La Reina Banda Homenaje a Queen', 'arte_cultura', 'concierto', 'Santo Domingo', 'Hard Rock Cafe Bluemall',6,'06-08-2021', 'FRONT STAGE', 2980, 'La Reina Banda Homenaje a Queen. Evento para mayores de 18 años.',20,23).
arte_cultura(21,'La Reina Banda Homenaje a Queen', 'arte_cultura', 'concierto', 'Santo Domingo', 'Hard Rock Cafe Bluemall',6,'06-08-2021', 'SPECIAL GUEST', 2435, 'La Reina Banda Homenaje a Queen. Evento para mayores de 18 años.',20,23).
arte_cultura(22,'La Reina Banda Homenaje a Queen', 'arte_cultura', 'concierto', 'Santo Domingo', 'Hard Rock Cafe Bluemall',6,'06-08-2021', 'MEZZANINE', 1950, 'La Reina Banda Homenaje a Queen. Evento para mayores de 18 años.',20,23).
arte_cultura(23,'Jueves con Bebeto: Bachatazo 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Hard Rock Cafe',12,'12-08-2021', 'VIP', 1625, 'Concierto de bachata tributo a Yoskar Sarante. Evento para mayores de 18 años.',20,23).
arte_cultura(24,'Jueves con Bebeto: Bachatazo 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Hard Rock Cafe',12,'12-08-2021', 'GENERAL - 1ER PISO', 1085, 'Concierto de bachata tributo a Yoskar Sarante. Evento para mayores de 18 años.',20,23).
arte_cultura(25,'Jueves con Bebeto: Bachatazo 2021', 'arte_cultura', 'concierto', 'Santo Domingo', 'Hard Rock Cafe',12,'12-08-2021', 'GENERAL - 2DO PISO', 1085, 'Concierto de bachata tributo a Yoskar Sarante. Evento para mayores de 18 años.',20,23).
arte_cultura(26,'Jueves con Bebeto: Diomedes y El Grupo Mio & Amarfis', 'arte_cultura', 'concierto', 'Santo Domingo', 'Hard Rock Cafe',5,'05-08-2021', 'VIP', 1085, 'Concierto de bachata tributo a Yoskar Sarante. Evento para mayores de 18 años.',20,23).
arte_cultura(27,'La Golondrina', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Teatro Nacional',13,'13-08-2021', 'PLATEA', 1085, 'Obra de teatro',20,22).
arte_cultura(28,'La Golondrina', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Teatro Nacional',14,'14-08-2021', 'PLATEA', 1085, 'Obra de teatro',20,22).
arte_cultura(29,'La Golondrina', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Teatro Nacional',15,'15-08-2021', 'PLATEA', 1085, 'Obra de teatro',18,20).
arte_cultura(30,'La Golondrina', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Teatro Nacional',19,'19-08-2021', 'PLATEA', 1085, 'Obra de teatro',20,22).
arte_cultura(31,'La Golondrina', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Teatro Nacional',20,'20-08-2021', 'PLATEA', 1085, 'Obra de teatro',20,22).
arte_cultura(32,'La Golondrina', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Teatro Nacional',21,'21-08-2021', 'PLATEA', 1085, 'Obra de teatro',20,22).
arte_cultura(33,'Caligula Moon', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Casa de Teatro',13,'13-08-2021', 'GENERAL', 760, 'Monologo de Jorge Carrigan, dirigido y actuado por Emir Cruz.',19,21).
arte_cultura(34,'Caligula Moon', 'arte_cultura', 'obra de teatro', 'Santo Domingo', 'Casa de Teatro',14,'14-08-2021', 'GENERAL', 760, 'Monologo de Jorge Carrigan, dirigido y actuado por Emir Cruz.',19,21).
arte_cultura(35,'Sunday Brunch', 'arte_cultura', 'concierto', 'Santo Domingo', 'Casa de Teatro',15,'15-08-2021', 'GENERAL - 1ER PISO', 2165, 'Sunday Brunch junto a Yiyo Sarante. Evento para mayores de 18 años.',20,22).
arte_cultura(36,'Titanes del Distrito', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',18,'18-08-2021', 'PALCOS', 180, 'Titanes Vs Indios',19,21).
arte_cultura(37,'Titanes del Distrito', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',22,'18-08-2021', 'PALCOS', 180, 'Titanes Vs Reales',20,22).
arte_cultura(38,'Titanes del Distrito', 'deportes', 'evento deportivo', 'Santo Domingo', 'Palacio de los Deportes',26,'18-08-2021', 'PALCOS', 180, 'Titanes Vs Leones',21,23).

eventos_semana(_CantidadDinero,_DiasSemana,[],Res,Res):-!.
eventos_semana(CantidadDinero, DiasSemana,[X|Y],Pares,Res):- X = [TarifaTicket,DiaEvento,IdEvento],
    arte_cultura(IdEvento, _Actividad, _TipoEvento, _TipoEstablecimiento,_Provincia, _Ubicacion, DiaEvento, _Fecha, _TipoTicket,
                 TarifaTicket, _Descripcion,_HoraInicia, _HoraTermina), TarifaTicket=<CantidadDinero, NuevaCantidadDinero is CantidadDinero - TarifaTicket,
    eventos_semana(NuevaCantidadDinero,DiasSemana,Y,[IdEvento|Pares],Res).
eventos_semana(CantidadDinero,DiasSemana,[_|Y],Pares,Res):- eventos_semana(CantidadDinero,DiasSemana,Y,Pares,Res).

sort(List, Order, Sorted):- Order = 'asc', sort(0,=<,List,Sorted), !.
sort(List, Order, Sorted):- Order = 'desc',sort(0,>=,List,Sorted), !.
get_eventos(Order, Sorted, Dias):- findall([TarifaTicket, Dias, IdEvento], arte_cultura(IdEvento, _Actividad, 'arte_cultura', _TipoEstablecimiento,_Provincia, _Ubicacion, Dias, _Fecha, _TipoTicket,TarifaTicket, _Descripcion),X), sort(X,Order,Sorted).

eventos_hoy(_CantidadDinero, _HoraActual,[],Res,Res):-!.
eventos_hoy(CantidadDinero,HoraActual,[X|Y],Pares,Res):- X = [TarifaTicket,DiaEvento,IdEvento],
    arte_cultura(IdEvento, _Actividad, _TipoEvento, _TipoEstablecimiento,_Provincia, _Ubicacion, DiaEvento, _Fecha, _TipoTicket,
                 TarifaTicket, _Descripcion, HoraInicia, _HoraTermina), HoraActual =< HoraInicia, TarifaTicket=<CantidadDinero, NuevaCantidadDinero is CantidadDinero - TarifaTicket, eventos_hoy(NuevaCantidadDinero,HoraActual,Y,[IdEvento|Pares],Res).
eventos_hoy(CantidadDinero,HoraActual,[_|Y],Pares,Res):- eventos_hoy(CantidadDinero,HoraActual,Y,Pares,Res).

%nombre, provincia, cartelera, hora_abre, hora_cierra
cine('Palacio del cine', 'Santo Domingo', ['endgame', 'avatar', 'marriage story', 'cinderella'], 2, 11).
cine('Cine Colonial', 'Santo Domingo', ['barbie', 'el camino'], 2, 10).
cine('Cine de Agora', 'Santo Domingo', ['endgame', 'avatar', 'marriage story', 'cinderella'], 2, 11).

pelicula('endgame', ['accion','ficcion']).
pelicula('avatar', ['accion','ficcion']).
pelicula('marriage story', ['drama', 'romance']).
pelicula('cinderella', ['romance', 'fantasia']).
pelicula('barbie', ['romance', 'fantasia']).
pelicula('el camino', ['drama']).

tipodepelicula([X|Y], Tipo):- X = Tipo -> !; tipodepelicula(Y,Tipo).
tipodepelicula([]).
iterarpelicula([X|_Y], Tipo):-  pelicula(X, Tipos), tipodepelicula(Tipos, Tipo).
iterarpelicula([]).
buscarcines(Cine, Ubicacion, Tipo, ToqueQueda):- cine(Cine,Ubicacion, X, _HoraIni, HoraCierre), HoraCierre < ToqueQueda ,iterarpelicula(X, Tipo).

%Regla extra buscar hoteles en base a una cantidad de estrellas
hotel('Dominican Fiesta Hotel & Casino', 5, 'Santo Domingo').
hotel('Hotel Santander',2 ,'Santo Domingo').
hotel('Ramada by Wyndham Princess Santo Domingo',3,'Santo Domingo').
hotel('El Embajador', 5,'Santiago').
hotel('Hotel Renacer',2,'Santiago').
hotel('Holiday Inn Santo Domingo Hotel & Suites',4,'Santo Domingo').
hotel('Hotel Maison Gautreaux',3,'Monte Cristi').
hotel('Hotel Aladino',3,'Santo Domingo').
hotel('Barcelo Santo Domingo',5,'Santo Domingo').
hotel('Dominican Fiesta Hotel & Casino',5,'Santiago').

buscartodosloshoteles(Hotel, Estrellas, Lugar, Retorno):- findall((Hotel),hotel(Hotel,Estrellas, Lugar), Retorno).

%regla extra 3, buscar lugares en mi perimetro.
miperimetro(DondeEstoy,Perimetro,Lugar):- distancia(DondeEstoy,Lugar,Metros), Metros =< Perimetro.






