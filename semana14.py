
# "En este apartado se muestra el Mensaje de bienvenida del programa"
print("BIENVENIDOS AL PROGRAMA DONDE PODRÁ CONSULTAR INFORMACIÓN DE LOS DEPARTAMENTOS DE EL SALVADOR")
#"Aqui se le debe Preguntar al usuario si desea ejecutar el programa"
while True:
        respuesta = input("¿Desea ejecutar el programa? (si/no): ")
        if respuesta.lower() == "si":
            print("SE INICIÓ DEL PROGRAMA")
            #Aqui se debe Mostrar el menú de departamentos 
            print("Seleccione un departamento: ")
            lisT = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
            departamentos = ["Chalatenango", "Auachapán","Santa Ana","Sonsonate","La Libertad" , "San Salvador","Cuscatlán" , "Cabañas", "La Paz",
                           "San Vicente", "Usulután" ,"San Miguel", "Morazán" , "La Unión"]
            for l1, l2 in zip(lisT,departamentos):
                print(l1,l2)   
                    #Pedir al usuario que ingrese el nombre del departamento
                  #ARRAYS DE TODOS LOS DEPARTAMENTOS         
            intentos = 5
            while intentos > 0:
                departament = input("INGRESE EL NOMBRE DEL DEPARTAMENTO: ").upper()
                #DEPARTAMENTO 1
                if departament == "Chalatenango".upper():
                      print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
                      
                      print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :")
                      lista1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,28,29,30,31,32,33]
                      municipios1=["Agua Caliente" , "Arcatao" , "Azacualpa" , "Cancasque" ,"Chalatenango" , "Citalá" , "Comalapa"  , "Concepción" , "Quezaltepeque"
                            , "Dulce Nombre de María" ,  "El Carrizal" , "El Paraíso" , "La Laguna" , "La Palma" , "La Reina" , "Las Flores" , "Las Vueltas" , "Nombre de Jesús",
                            "Nueva Concepción" , "Nueva Trinidad" ,"Ojos de Agua" , "Potonico" , "San Antonio de la Cruz" , "San Antonio Los Ranchos", "San Fernando" ,
                            "San Francisco Lempa" ,"San Francisco Morazán", "San Ignacio" , "San Isidro Labrador"	"San Luis del Carmen" , "San Miguel de Mercedes" , "San Rafael",
                            "Santa Rita" , "Tejutla"""]
                      for l1 , l2 in zip(lista1,municipios1):
                           print(l1,l2)       
                                       #DEPARTAMENTO 2
                elif departament == "Ahuachapán".upper():
                      print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
                      
                      print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :")    
                      lista2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
                      municipios2=["Ahuachapán" , "Apaneca" , "Atiquizaya" , "Concepción de Ataco" , "El Refugio" , "Guaymango" , "Jujutla" ,
                           "San Francisco Menéndez" , "San Lorenzo" , "San Pedro" ,"Puxtla" , "Tacuba" , "Turín"]
                      for l1 , l2 in zip(lista2,municipios2):
                       print(l1,l2)
                      # DEPARTAMENTO 3
                elif departament == "Santa Ana".upper():
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :")  
                    lista3=[1,2,3,4,5,6,7,8,9,10,11,12,13]
                    municipios3=["Candelaria de la Frontera" , "Chalchuapa" , "Coatepeque" , "El Congo" 
                           ,"El Porvenir" , "Masahuat" , "Metapán" , "San Antonio Pajonal" , "San Sebastián Salitrillo"
                           ,"Santa Ana" , "Santa Rosa Guachipilín" ,"Santiago de la Frontera", "Texistepeque"]
                    for l1,l2 in zip(lista3,municipios3):
                        print(l1,l2)
                   # DEPARTAMENTO 4
                elif departament == "Sonsonate".upper():
                     print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
        
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :")  
                     lista4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
                     municipios4=["Acajutla" , "Armenia" ,  "Caluco", "Cuisnahuat", "Izalco", "Juayúa", 
                     "Nahuizalco" , "Nahulingo" , "Salcoatitán", "San Antonio del Monte" , "San Julián",
                     "Santa Catarina", "Masahuat", "Santa Isabel" , "Ishuatán" , "Santo Domingo de Guzmán" , 
                     "Sonsonate" , "Sonzacate"]
                     for l1,l2 in zip(lista4,municipios4):
                         print(l1,l2)
                      #DEPARTAMENTO 5
                elif departament == "La Libertad".upper():
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :")  
                    lista5=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
                    municipios5=["Antiguo Cuscatlan", "chilitupán", "Ciudad Arce", "Colón",
                          "Comasagua", "Huizúcar", "Jayaque", "Jicalapa", "La Libertad", "Santa Tecla",
                         "Nuevo Cuscatlan", "San Juan Opico", "Quezaltepeque", "Sacacoyo", " San José Villanueva"
                         "San Matias", "San Pablo Tacachico", "Talnique", "Teotepeque","Tepecoyo", "Zaragoza"]
                    for l1,l2 in zip(lista5,municipios5):
                        print(l1,l2)

                     #DEPARTAMENTO 6
                elif departament == "San Salvador".upper():
                     print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
        
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :")  
                     lista6=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21]
                     municipios6=["Aguilares","Apopa","Ayutuxtepeque","Cuscatancingo","Ciudad delgado","El Paisnal", "Guazapa"
                            ,"Ilopango","Mexicanos","Nejapa","Panchimalco", "Rosario de Mora","San Marcos","San Martín","San Salvador"
                            ,"Santiago","Texacuango","Santo Tomás","Soyapango","Tonacatepeque"]
                     for l1,l2 in zip(lista6,municipios6 ):
                         print(l1,l2)  
    
                     #DEPARTAMENTO 7
                elif departament == "Cuscatlán".upper():
                    
                     print(f"--- INFORMACION DEL DEPARTAMENTO DE {departament} ---")
    
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON:")
                     lista7=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17]          
                     municipios7=["Candelaria" , "Cojutepeque" , "El Carmen" , "El Rosario" , "Monte San Juan" , 
                           "Oratorio de Concepción" , "San Bartolomé Perulapía" , "San Cristóbal" ," San José Guayabal" ,
                           "San Pedro Perulapán" , "San Rafael Cedros" , "San Ramón"
                           , "Santa Cruz Analquito" , "Santa Cruz Michapa", "Suchitoto" , "Tenancingo"]
                     for l1,l2 in zip(lista7,municipios7):
                           print(l1,l2)
                    
                    #DEPARTAMENTO 8
                elif departament == "Cabañas".upper():
                     print(f"--- INFORMACION DEL DEPARTAMENTO DE {departament} ---")
    
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON:")
                     lista8=[1,2,3,4,5,6,7,8,9]   
                            
                     municipios8=["Cinquera" , "Dolores" , "Guacotecti" , "Ilobasco " , "Jutiapa " , "San Isidro " , "Sensuntepeque " , "Tejutepeque " , "Victoria"]
                     for l1,l2 in zip(lista8,municipios8):
                      print(l1,l2)
                
                    #DEPARTAMENTO 9
                elif departament == "La Paz".upper():
                    
                  print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
        
                  print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :") 
                  lista9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15,16,17,18,19,20,21,22]
                  municipios9 = ["Zacatecoluca", "Cuyultitán", "El Rosario", "Jerusalén", 
                              "Mercedes La Ceiba", "Olocuilta", "Paraíso de Osorio", 
                             "San Antonio Masahuat", "San Emigdio", "San Francisco Chinameca", 
                             "San Pedro Masahuat", "San Juan Nonualco","San Juan Talpa","San Juan Tepezontes","San Luis La Herradura"
                             ,"San Luis Talpa","San Miguel Tepezonte","San Pedro Nonualco","San Rafael Obrajuelo","San María Ostuma","Santiago Nonualco",
                             "Tapalhuaca"]
                  for l1,l2 in zip (lista9,municipios9):
                        print(l1, l2)
                      
                           #DEPARTAMENTO 10
                elif departament == "San Vicente".upper():
                    
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :") 
                    
                    lista10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13]
                    municipios10 = ["Apastepeque", "Guadalupe", "San Cayetano Istepeque", 
                             "San Esteban Catarina", "San Ildefonso", "San Lorenzo", 
                             "San Sebastián", "San Vicente", "Santa Clara", "Santo Domingo", 
                             "Tecoluca", "Tepetitán", "Verapaz"]
                    for l1,l2 in zip (lista10,municipios10):
                        print(l1, l2)
                
                      #DEPARTAMENTO 11
                elif departament == "Usulután".upper():
                  print(f"---INFORMACIÓN DEL DEPARTAMENTO DE: {departament}---")
     
                  print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON:")
                  lista11=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                  municipios11=["Alegría", "Berlín", "California", "Concepción Batres", "El Triunfo", "Ereguayquín", "Estanzuelas", 
                                "Jiquilisco", "Jucuapa", "Jucuarán", "Mercedes Umaña", "Nueva Granada", "Ozatlán", "Puerto El Triunfo", 
                                 "San Agustín", "San Buenaventura", "San Dionisio", "San Francisco Javier", "Santa Elena", 
                                "Santa María", "Santiago de María", "Tecapán", "Usulután"]
                  for l1,l2 in zip(lista11,municipios11):
                      print(l1,l2)
                    
                       #DEPARTAMENTO 12
                elif departament == "San Miguel".upper():
                    
                     print(f"---INFORMACIÓN DEL DEPARTAMENTO DE: {departament}---")
        
                     print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON:")
                     lista12=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
                     
                     municipios12=["Carolina", "Chapeltique", "Chinameca", "Chirilagua", "Ciudad Barrios", "Comacarán",
                              "El Tránsito", "Lolotique", "Moncagua", "Nueva Guadalupe", "Nuevo Edén de San Juan", "Quelepa", "San Antonio del Mosco",   
                             "San Gerardo", "San Jorge", "San Luis de la Reina", "San Miguel", "San Rafael Oriente", "Sesori", "Uluazapa",]
                     for l1,l2 in zip(lista12,municipios12):
                         print(l1,l2)
                    
                    #DEPARTAMENTO 13
                elif departament == "Morazán".upper():
                    print(f"--- INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
        
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE {departament} SON :")
                
                    lista13=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
                    municipios13=["Arambla", "Cacaopera", "Chilanga", "Corinto", "Delicias de concepción", 
                            "El Divisadero", "El Rosario", "Gualocoti", "Guatajiagua", "Joateca",
                             "Jocoatique", "Jocoro", "Lolotiquillo", "Osicala", "Perquin",
                            "San Carlos", "San Fernando", "San Francisco Gotera", "San Isidro", "Sam Simón",
                            "Sensembra", "Sociedad", "Torola", "Yamabla", "Yoloaiquin"]
                    for l1,l2 in zip(lista13,municipios13):
                        print(l1,l2)
             
                   #DEPARTAMENTO 14
                elif departament == "La Unión".upper():
                    
                    print(f"---INFORMACIÓN DEL DEPARTAMENTO DE {departament} ---")
    
                    print(f"LOS MUNICIPIOS DEL DEPARTAMENTO DE LA UNIÓN DE {departament} SON :")
                    lista14=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
                    municipios14=["Anamorós", "Bolívar", "Concepción de Oriente", "Conchagua", "El Carmen", "El Sauce", "Intipucá", "La Unión", "Lislique", 
                        	"Meanguera del Golfo", "Nueva Esparta", "Pasaquina", "Polorós", "San Alejo", "San José", "Santa Rosa de Lima", "Yayantique", "Yucuaiquín"]
                    for l1,l2 in zip (lista14,municipios14):
                        print(l1, l2)
                          
                else:
                 #ADVERTENCIA DE QUE EL DATO QUE EL USUARIO INGRESÓ NO FUE ENCONTRADO
                  intentos -= 1
                  if intentos > 0:
                        print(f"DEPARTAMENTO NO ENCONTRADO INGRESE UN NOMBRE VÁLIDO. LE QUEDAN  {intentos} INTENTOS.")
                        continue
                  else:
                        print("Número máximo de intentos finalizado.")
                            
                            #Preguntar si desea consultar datos de otro departamento
                
                respuesta = input("¿DESEA CONSULTAR INFORMACIÓN DE OTRO DEPARTAMENTO ? (si/no): ")
                if respuesta.lower() == "si":
                    continue
                elif respuesta.lower() == "no":
                    print("Programa finalizado.")
                    break
                else:
                     intentos -= 1
                     if intentos > 0:
                        print(f"DEPARTAMENTO NO ENCONTRADO INGRESE UN NOMBRE VÁLIDO. LE QUEDAN  {intentos} INTENTOS.")
                        continue
                  
                print("Fin del programa")
                break   
        else:            
            print("Fin del programa")
        break