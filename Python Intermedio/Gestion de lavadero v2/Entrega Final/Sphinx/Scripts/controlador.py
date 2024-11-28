#Modulos internos
from vista import *
from modelo import *

class Controller:
    """
        Clase que contiene toda la interaccion con la interfaz de usuario.
        --- Constructor --- 
            -Crea la ventana principal y la vista.
            -Llama a la funcion actualizar_tree para actualizar el arbol de la base de datos.
            -Conecta los botones de vista.py con los metodos de la clase.
            
    """
    def __init__(self):
        self.ventana = Tk()
        self.vista = MainVentana(self.ventana)
        self.modelo = OperacionesCRUD()
        self.actualizar_tree()
        
        self.vista.boton_todos.config(command=lambda:self.actualizar_tree())
        self.vista.boton_alta.config(command=lambda:self.alta())
        self.vista.boton_borrar.config(command=lambda:self.borrar())
        self.vista.boton_modificar.config(command=lambda:self.modificar())
        self.vista.boton_consultar.config(command=lambda:self.consultar())
        self.vista.boton_calcular.config(command=lambda:self.balance_total())
        self.vista.boton_exportar.config(command=lambda:self.exportar())
        self.vista.boton_borrar_todo.config(command=lambda:self.borrar_todo())

    def alta(self):
        """
            Funcion que permite generar una nueva orden.
            ---------------------------------------------
            Conecta las variables de tkinter para pasarlos como parametros a la funcion alta_orden de la clase modelo.
            
            Parametros:
                -nombre: Nombre de la orden.
                -telefono: Telefono de la orden.
                -tipo: Tipo de la orden.
                -cantidad: Cantidad de la orden.
                -fecha: Fecha de la orden.
                -horario: Horario de la orden.
                -precio: Precio de la orden.
        """
        try:
            nombre, telefono, tipo, cantidad, fecha, horario, precio = self.vista.v_nombre.get(),self.vista.v_telefono.get(),self.vista.v_tipo.get(),self.vista.v_cantidad.get(),self.vista.v_fecha.get(),self.vista.v_horario.get(),self.vista.v_precio.get()
            if re.match(r'^\d+$', telefono) and re.match(r'^\d+$', precio): #RegEx solo numeros ni vacio para precio y telefono
                self.modelo.alta_orden(nombre, telefono, tipo, cantidad, fecha, horario, precio)
                self.actualizar_tree()
                self.vista.limpiar_entrys()
                self.vista.alerta("Nueva orden generada",COLOR_OK,TEXT_INFO)
                
            else:
                messagebox.showerror("Error en el alta","El campo 'Telefono' y 'Precio' solo deben contenter numeros ni deben estar vacios!")
                print("El campo 'Telefono' y 'Precio' solo deben contenter numeros ni deben estar vacios!")
        except Exception as err:
            print("Error al dar de alta en ventana:",err)
    
    
    def borrar(self):
        """
            Funcion que permite borrar una orden.
            -------------------------------------
            Obtiene la seleccion de la vista del treeview y la borra de la base de datos.
        """
        try:
            seleccion = self.vista.tree.selection()
            orden = self.vista.tree.item(seleccion)
            id_orden = orden['text']
            if not id_orden:
                messagebox.showerror("Error al borrar orden","No se selecciono ninguna orden para borrar.")
                print("No se selecciono ninguna orden para borrar.")
            else:
                self.modelo.borrar_orden(id_orden)
                self.actualizar_tree()
                self.vista.alerta(f"La orden {id_orden} fue eliminada",COLOR_ERROR, TEXT_INFO)
        except Exception as err:
            print("No se pudo eliminar la orden:", err)
    
    
    def modificar(self):
        """
            Funcion que permite modificar una orden.
            ----------------------------------------
            Conecta las variables de tkinter para pasarlos como parametros a la funcion modificar_orden de la clase modelo.
            
            Parametros:
                -id_orden: Identificador de la orden que se selcciona del treeview de tkinter.
                -nombre: Nombre de la orden.
                -telefono: Telefono de la orden.
                -tipo: Tipo de la orden.
                -cantidad: Cantidad de la orden.
                -fecha: Fecha de la orden.
                -horario: Horario de la orden.
                -precio: Precio de la orden.
        """
        try:
            seleccion = self.vista.tree.selection()
            orden = self.vista.tree.item(seleccion)
            id_orden = orden['text']
            nombre, telefono, tipo, cantidad, fecha, horario, precio = self.vista.v_nombre.get(),self.vista.v_telefono.get(),self.vista.v_tipo.get(),self.vista.v_cantidad.get(),self.vista.v_fecha.get(),self.vista.v_horario.get(),self.vista.v_precio.get()
            if id_orden == "":
                messagebox.showerror("Error en modificacion","No se selecciono ninguna orden para modificar!")
            elif nombre == "" or telefono == "" or tipo == "" or cantidad == "" or fecha == "" or horario == "" or precio == "":
                messagebox.showerror("Error en modificacion","No se debe dejar ningun campo vacio para modificar!")
            elif not re.match(r'^\d+$', telefono) or not re.match(r'^\d+$', precio):
                messagebox.showerror("Error en el alta","El campo 'Telefono' y 'Precio' solo deben contenter numeros ni deben estar vacios!")
                print("El campo 'Telefono' y 'Precio' solo deben contenter numeros ni deben estar vacios!")
            else:
                self.modelo.modificar_orden(id_orden, nombre, telefono, tipo, cantidad, fecha, horario, precio)
                self.actualizar_tree()
                self.vista.limpiar_entrys()
                self.vista.alerta(f"La orden {id_orden} fue modificada", COLOR_INFO, TEXT_INFO)
        except Exception as err:
            print("Ocurrio un errro al modificar la orden", err)


    def consultar(self):
        """
            Funcion que permite realizar una consulta por nombre.
            ------------------------------------------------------
            Obtiene el nombre del campo de busqueda y lo pasa a la funcion consulta_nombre de la clase modelo.
            
            Parametros:
                -nombre: Nombre de la orden que se busca.
        """
        try:
            nombre = self.vista.v_consulta.get()
            resultado = self.modelo.consulta_nombre(nombre)
            if nombre == "":
                messagebox.showerror("Error en la consulta","El campo 'Consulta por cliente' no debe estar vacio.")
                print("El campo de busqueda se encuentra vacio.")
            elif len(resultado) == 0:
                messagebox.showerror("Error en la consulta",f"No se encontraron ordenes de: {nombre}")
            else:
                self.ordenes = self.vista.tree.get_children()
                for orden in self.ordenes:
                    self.vista.tree.delete(orden)
                for orden in resultado:
                    self.vista.tree.insert("", 0, text=orden['id'], values=(orden["nombre"], orden["telefono"], orden["tipo"], orden["cantidad"], orden["fecha"], orden["horario"], orden["precio"]))
                    self.vista.alerta(f"Ordenes de {nombre}", COLOR_INFO, TEXT_INFO)
        except Exception as err:
            print("Error al consultar ordenes:",err)


    def borrar_todo(self):
        """
            Funcion que permite borrar todas las ordenes.
            ---------------------------------------------
            Pregunta al usuario si desea borrar todas las ordenes y si es asi, se borran todas las ordenes.
        """
        try:
            respuesta = messagebox.askyesno("Borrar todas las ordenes","Desea borrar todas las ordenes?")
            if respuesta == True:
                self.modelo.borrar_todo()
                self.vista.alerta("Se han eliminado todas las ordenes.",COLOR_INFO, TEXT_INFO)
            else:
                print("Operacion cancelada (Borrar todo)")
        except Exception as err:
            print("Error al borrar todos los registros:",err)
    
    
    def balance_total(self):
        """
            Funcion que permite calcular el balance a cobrar total de las ordenes.
            ----------------------------------------------------------------------
            Obtiene el resultado del metodo consulta_ordenes de la clase modelo y el resultado lo inserta en el entry de balance.
        """
        total = 0
        resultado = self.modelo.consulta_ordenes()
        for orden in resultado:
            total += orden['precio']
            if self.vista.entry_balance == "":
                self.vista.entry_balance.insert(0, f"$ {total}")
                self.vista.alerta(f"El total a recuadar es de ${total}",COLOR_INFO, TEXT_INFO)
            else:
                self.vista.v_balance.set("")
                self.vista.entry_balance.insert(0, f"$ {total}")
                self.vista.alerta(f"El total a recuadar es de ${total}",COLOR_INFO, TEXT_INFO)
    
    def exportar(self):
        """
            Funcion que permite exportar todas las ordenes.
            -----------------------------------------------
            Llama a la funcion exportar_ordenes de la clase modelo.
        """
        self.modelo.exportar_ordenes()
        messagebox.showinfo("Exportar ordenes", "Se han exportado todas las ordenes.")
    
    
    def actualizar_tree(self):
        """
            Funcion que permite actualizar el treeview de tkinter.
            ------------------------------------------------------
            Obtiene el resultado de la consulta de la base de datos y lo inserta en el arbol del treeview.
        """
        try:
            self.ordenes = self.vista.tree.get_children()
            for orden in self.ordenes:
                self.vista.tree.delete(orden)
            resultados = self.modelo.consulta_ordenes()
            for fila in resultados:
                self.vista.tree.insert("", 0, text=fila["id"], values=(fila["nombre"], fila["telefono"], fila["tipo"], fila["cantidad"], fila["fecha"], fila["horario"], fila["precio"]))
        except Exception as err:
            print("Error al actualizar el treeview:",err)
