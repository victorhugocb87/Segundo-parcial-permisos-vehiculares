class permisos:
    def __init__(self):
        self.codigo = []
        self.conductor = []
        self.modelo = []
        self.marca = []
        self.placa = []
        self.ciudad = []
        self.fecha = []
        self.motivo = []
        self.habilitado = []
        self.estado = []

    def menu(self):
        opciones = """
      ***** GESTION DE REGISTRO DE PERMISO VEHICULAR *****

          1.- REGISTRO DE PERMISO
          2.- MENU DE PERMISOS SOLICITADOS 
          3.- HABILITAR LOS PERMISOS SOLICITADOS HASTA EL 31/05/2020
          4.- PERMISOS HABILITADOS
          5.- PERMISOS NO HABILITADOS
          6.- SALIR  
        """
        print(opciones)
        print("******** INGRESE DATOS EN LOS CAMPOS HABILITADOS **********")
        seleccion = int(input("SELECCIONE UNA OPCION DEL MENU: \n "))
        if (seleccion == 1):
            print(self.registrar())
            self.menu()
        elif (seleccion == 2):
            print(self.mostrar())
            print(self.volverMenu())
        elif (seleccion == 3):
            print()
            self.volverMenu()
        elif (seleccion == 4):
            print(self.mostrarHabilitados())
            print(self.volverMenu())
        elif (seleccion == 5):
            print(self.mostrarNoHabilitados())
            print(self.volverMenu())
        elif (seleccion == 6):
            print("******** GRACIAS POR USAR NUESTRO SISTEMA *******")
        else:
            print("******* SELECCIONE UNA OPCION DEL MENU *******")
            self.menu()

    def volverMenu(self):
        volver = input("Desea volver al menú: s/n \n")
        if (volver == "s" or volver == "S"):
            self.menu()
        return "******* GRACIAS POR USAR NUESTRO SISTEMA *******"

    def registrar(self):
        codigo = int(input("Ingrese Código: \n".format(self.codigo)))
        conductor = input("Ingrese Nombre: \n".format(self.conductor))
        modelo = input("Ingrese Modelo del auto: \n".format(self.modelo))
        marca = input("Ingrese Marca del auto: \n".format(self.marca))
        placa = input("Ingrese n° de Placa: \n".format(self.placa))
        ciudad = input("Ingrese Ciudad: \n".format(self.ciudad))
        fecha = input("Ingrese Fecha de Solicitud: \n".format(self.fecha))
        motivo = input("Motivo del Permiso: \n".format(self.motivo))
        print(self.guardar(codigo, conductor, modelo, marca, placa, ciudad, fecha, motivo))
        print("****************************************************")
        nuevo = input("Desea volver a registrar: s/n \n")
        if (nuevo == "s" or nuevo == "S"):
            self.registrar()

        return "******** REGISTRO AGREGADO CORRECTAMENTE A LA BASE DE DATOS ********"

    def guardar(self, codigo, conductor, modelo, marca, placa, ciudad, fecha , motivo):
        self.codigo.append(codigo)
        self.conductor.append(conductor)
        self.modelo.append(modelo)
        self.marca.append(marca)
        self.placa.append(placa)
        self.ciudad.append(ciudad)
        self.fecha.append(fecha)
        self.motivo.append(motivo)
        self.habilitado.append(0)
        self.estado.append(1)
        return " {} REGISTRO AGREGADO CORRECTAMENTE !! ".format(conductor)

    def detallePermisos(self, posicion):
        if (self.estado[posicion] == 1):
            print("*******************************************")
            print("Codigo : {} ".format(self.codigo[posicion]))
            print("Conductor: {} ".format(self.conductor[posicion]))
            print("Modelo del auto: {} ".format(self.modelo[posicion]))
            print("Marca del auto: {} ".format(self.marca[posicion]))
            print("placa del auto: {} ".format(self.placa[posicion]))
            print("Ciudad: {} ".format(self.ciudad[posicion]))
            print("fecha: {} ".format(self.fecha[posicion]))
            print("Motivo: {} ".format(self.motivo[posicion]))
            if (self.habilitado[posicion] == 1):
                print("Habilitado : Si")
            else:
                print("Habilitado : No")
            return "********************************************"

    def mostrar(self):
        if (self.conductor):
            for i in range(len(self.conductor)):
                self.detallePermisos(i)
            return "*********************************************"
        else:
            return "******* LA LISTA DE REGISTRO DE ENCUENTRA VACIA ******* "
        pass

    def mostrarHabilitados(self):
        habil = False
        for i in range(len(self.conductor)):
            if (self.habilitado[i] == 1):
                self.detallePermisos(i)
                habil = True
        if (habil == False):
            return "******* SU PERMISO NO ESTA HABILITADO ********"
        return "**************************************"

    def mostrarNoHabilitados(self):
        habil = False
        for i in range(len(self.conductor)):
            if (self.habilitado[i] == 0):
                self.detallePermisos(i)
                habil = True
        if (habil == False):
            print("******* SU PERMISO ESTA HABILITADO ********")
        return "**************************************"


permisos = permisos()
permisos.guardar(1, 'JOSE MERCADO', 'COROLLA', 'TOYOTA', '2504TDA', 'SANTA CRUZ', '15/06/2020',
                 'PERMISO PARA IR AL TRABAJO')
permisos.guardar(2, 'ALBERTO MERCADO', 'HILUX', 'TOYOTA', '2640SDA', 'TARIJA', '12/04/2020',
                 'PERMISO PARA IR AL MEDICO')
permisos.guardar(3, 'GABRIEL MELGAR', 'SENTRA', 'NISSAN', '3204NTS', 'BENI', '30/05/2020', 'PERMISO PARA IR AL CENTRO')
permisos.guardar(4, 'CARLA MEDINA', 'LANCER', 'MITSUBISHI', '2207SBA', 'CHUQUISACA', '02/05/2020',
                 'PERMISO PARA IR A LA UNIVERSIDAD')
permisos.guardar(5, 'PABLO AGUILAR', 'ACCORD', 'HONDA', '3504ATD', 'COCHABAMBA', '09/04/2020',
                 'PERMISO PARA IR AL CINE')
permisos.guardar(6, 'CARLOS MONTERO', 'CIVIC', 'HONDA', '2804STA', 'SANTA CRUZ', '10/06/2020',
                 'PERMISO PARA IR AL TEATRO')
permisos.guardar(7, 'PABLO ALEMAN', 'YARIS', 'TOYOTA', '2054PDA', 'LA PAZ', '02/06/2020', 'PERMISO PARA IR AL BANCO')
permisos.menu()