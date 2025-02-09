from tkinter import Label, Entry, Button, ttk, StringVar, IntVar, messagebox
from tkcalendar import DateEntry
from estilos import *


def alerta_decorator(mensaje, color, fuente):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            alerta_msj = Label(self.ventana, text=mensaje, fg=color, font=fuente)
            alerta_msj.place(x=320, y=763)
            self.ventana.after(6000, lambda label: label.destroy(), alerta_msj)
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


class MainVentana:
    def __init__(self, ventana):
        self.master = ventana
        self.master.geometry("850x800")
        self.master.title("Lavadero - Calle Falsa 123")
        self.master.config(bg=MODO_CLARO)
        self.tema = True
        (
            self.v_nombre,
            self.v_telefono,
            self.v_tipo,
            self.v_cantidad,
            self.v_fecha,
            self.v_horario,
            self.v_precio,
            self.v_consulta,
            self.v_balance,
        ) = (
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            IntVar(),
        )

        # Encabezado
        self.encabezado = Label(
            self.master,
            text="Gestor de ordenes",
            bg="#2664FA",
            fg=COLOR_TITUTLO,
            font=TEXT_TITULO,
            relief="groove",
        )
        self.encabezado.grid(row=0, column=0, columnspan=8, sticky="we")

        # Seccion alta
        self.titulo_alta = Label(
            self.master,
            text="Generar o modificar orden:",
            fg=COLOR_SUBTITULO,
            font=TEXT_TITULO,
        )
        self.titulo_alta.grid(row=1, column=0, sticky="w", padx=20)

        # Nombre
        self.nombre = Label(self.master, text="Nombre", bg="#01F56A", font=TEXT_HEADER)
        self.nombre.grid(row=2, column=0, sticky="w", padx=20, pady=7)
        self.entry_nombre = Entry(self.master, textvariable=self.v_nombre)
        self.entry_nombre.grid(row=2, column=1, sticky="w")

        # Telefono
        self.telefono = Label(
            self.master, text="Telefono", bg="#01F56A", font=TEXT_HEADER
        )
        self.telefono.grid(row=3, column=0, sticky="w", padx=20, pady=7)
        self.entry_telefono = Entry(self.master, textvariable=self.v_telefono)
        self.entry_telefono.grid(row=3, column=1, sticky="w")

        # Tipo de lavado
        self.tipo = Label(
            self.master, text="Tipo de lavado", bg="#01F56A", font=TEXT_HEADER
        )
        self.tipo.grid(row=4, column=0, sticky="w", padx=20, pady=7)
        self.combo_tipo = ttk.Combobox(
            textvariable=self.v_tipo,
            state="readonly",
            values=["Completo", "Secado solo", "Plancha", "Tintoreria"],
        )
        self.combo_tipo.grid(row=4, column=1, sticky="w")

        # Cantidad de valet
        self.cantidad = Label(
            self.master, text="Cantidad", bg="#01F56A", font=TEXT_HEADER
        )
        self.cantidad.grid(row=5, column=0, sticky="w", padx=20, pady=7)
        self.entry_cantidad = Entry(self.master, textvariable=self.v_cantidad)
        self.entry_cantidad.grid(row=5, column=1, sticky="w")

        # Fecha de entrega
        self.fecha_entrega = Label(
            self.master, text="Fecha de entrega", bg="#01F56A", font=TEXT_HEADER
        )
        self.fecha_entrega.grid(row=6, column=0, sticky="w", padx=20, pady=7)
        self.fecha_entry = DateEntry(
            self.master,
            width=16,
            background="darkblue",
            foreground="white",
            date_pattern="dd-mm-yyyy",
            textvariable=self.v_fecha,
        )
        self.fecha_entry.grid(row=6, column=1, sticky="w")

        # Horario de entrega
        self.tipo = Label(
            self.master, text="Horario de entrega", bg="#01F56A", font=TEXT_HEADER
        )
        self.tipo.grid(row=7, column=0, sticky="w", padx=20, pady=7)
        self.combo_tipo = ttk.Combobox(
            textvariable=self.v_horario,
            state="readonly",
            values=["Mañana", "Mediodia", "Tarde"],
        )
        self.combo_tipo.grid(row=7, column=1, sticky="w")

        # Precio total
        self.precio = Label(self.master, text="Precio", bg="#01F56A", font=TEXT_HEADER)
        self.precio.grid(row=8, column=0, sticky="w", padx=20, pady=7)
        self.entry_precio = Entry(self.master, textvariable=self.v_precio)
        self.entry_precio.grid(row=8, column=1, sticky="w")

        # Sector consulta por cliente
        self.consultar = Label(
            self.master, text="Consultar por cliente:", font=TEXT_HEADER
        )
        self.consultar.grid(row=2, column=3, sticky="e")
        self.entry_consultar = Entry(self.master, textvariable=self.v_consulta)
        self.entry_consultar.grid(row=2, column=5, sticky="w")
        self.boton_consultar = Button(self.master, text="Buscar")
        self.boton_consultar.grid(row=2, column=4, ipadx=10)

        # Sector balance total
        self.balance = Label(self.master, text="Balance total:", font=TEXT_HEADER)
        self.balance.grid(row=4, column=3, sticky="e")
        self.entry_balance = Entry(self.master, textvariable=self.v_balance)
        self.entry_balance.grid(row=4, column=5, sticky="w")
        self.boton_calcular = Button(self.master, text="Calcular")
        self.boton_calcular.grid(row=4, column=4, ipadx=6, pady=5)

        # Boton exportar
        self.boton_exportar = Button(self.master, text="Exportar", font=TEXT_BUTTON)
        self.boton_exportar.grid(row=6, column=3)

        # Boton cambiar color
        self.boton_color = Button(
            self.master,
            text="Cambiar tema",
            font=TEXT_BUTTON,
            command=lambda: self.cambiar_tema(),
        )
        self.boton_color.grid(row=6, column=4)

        # Boton limpiar todo
        self.boton_borrar_todo = Button(
            self.master, text="Borrar todo", font=TEXT_BUTTON
        )
        self.boton_borrar_todo.grid(row=6, column=5)

        # Boton modificar
        self.boton_modificar = Button(self.master, text="Modificar", font=TEXT_BUTTON)
        self.boton_modificar.grid(
            row=9, column=0, pady=10, padx=50, ipadx=10, sticky="w"
        )

        # Boton alta
        self.boton_alta = Button(self.master, text="Alta", font=TEXT_BUTTON)
        self.boton_alta.grid(row=9, column=1, pady=10, padx=50, ipadx=10, sticky="w")

        # Boton borrar
        self.boton_borrar = Button(self.master, text="Borrar", font=TEXT_BUTTON)
        self.boton_borrar.grid(row=9, column=3, ipadx=10)

        # Boton ver todos
        self.boton_todos = Button(self.master, text="Ver todos", font=TEXT_BUTTON)
        self.boton_todos.grid(row=9, column=5, ipadx=10, padx=30, sticky="w")

        # Treeview
        self.tree = ttk.Treeview(self.master, height=19)
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
        self.tree.column("#0", width=50, minwidth=50, anchor="w")
        self.tree.heading("#0", text="Orden")
        self.tree.column("col1", width=200, minwidth=200, anchor="w")
        self.tree.heading("col1", text="Nombre")
        self.tree.column("col2", width=120, minwidth=120, anchor="w")
        self.tree.heading("col2", text="Telefono")
        self.tree.column("col3", width=100, minwidth=100, anchor="center")
        self.tree.heading("col3", text="Tipo de lavado")
        self.tree.column("col4", width=60, minwidth=60, anchor="center")
        self.tree.heading("col4", text="Cantidad")
        self.tree.column("col5", width=100, minwidth=100, anchor="center")
        self.tree.heading("col5", text="Fecha de entrega")
        self.tree.column("col6", width=80, minwidth=60, anchor="center")
        self.tree.heading("col6", text="Horario")
        self.tree.column("col7", width=80, minwidth=60, anchor="center")
        self.tree.heading("col7", text="Precio")
        self.tree.grid(row=11, column=0, columnspan=6, padx=30, pady=10)

    def limpiar_entrys(self):
        lista_entrys = [
            self.v_nombre,
            self.v_telefono,
            self.v_tipo,
            self.v_cantidad,
            self.v_fecha,
            self.v_horario,
            self.v_precio,
            self.v_consulta,
            self.v_balance,
        ]
        for var in lista_entrys:
            var.set("")

    def cambiar_tema(self):
        if self.tema:
            self.master.config(bg=MODO_OSCURO)
        else:
            self.master.config(bg=MODO_CLARO)
        self.tema = not self.tema
