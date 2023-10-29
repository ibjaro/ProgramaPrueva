# programa de agenda, probando.

class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Mostrar contacto")
        print("4. Salir")

    def agregar(self, nombre, apellido, telefono, correo, direccion):
        #print("Agregar contacto")
        #nombre = input("Ingrese su Nombre: ")
        #apellido = input("Ingrese su Apellido: ")
        #telefono = input("Ingrese su Telefono: ")
        #correo = input("Ingrese su Correo: ")
        #direccion = input("Ingrese su direccion: ")
        self.contactos.append([nombre, apellido, telefono, correo, direccion])
        print("Contacto Agregado a la Agenda")

    def eliminar(self, nombre):
        #print("Eliminar contacto")
        #nombre = input("Ingrese el Nombre de contacto a eliminar: ")
        eliminado = False
        for i in self.contactos:
            if nombre in i:
                self.contactos.remove(i)
                print("Contacto eliminado de la Agenda")
                eliminado = True

        if not(eliminado):
            print("Contacto no encontrado en la Agenda")

    def mostrar(self):
        #print("Mostrar contactos")
        print("Contactos en la Agenda")
        for i in self.contactos:
            print(i)

    def salir(self):
        print("Gracias por usar la Agenda, hasta luego!")

    def principal(self, opcion, nombre="none", apellido="none", telefono="none", correo="none", direccion="none"):
        #while True:
            #self.menu()
            #opcion = int(input("Opcion: "))
        if opcion == 1:
            self.agregar(nombre, apellido, telefono, correo, direccion)
        elif opcion == 2:
            self.eliminar(nombre)
        elif opcion == 3:
            self.mostrar()
        elif opcion == 4:
            self.salir()
                #break
        else:
            print("Opcion no valida")

#agenda = Agenda()
#agenda.principal()


