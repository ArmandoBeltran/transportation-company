import flet as ft 

from models import Driver
from .drivers_table_view import DriversTableView
from .graph_view import GraphView

class FormView: 
    
    def clean_form(self):
        self.tf_name.value = ""
        self.tf_age.value = ""
        self.tf_city.value = ""
        self.tf_km_monday.value = ""
        self.tf_km_tuesday.value = ""
        self.tf_km_wednesday.value = ""
        self.tf_km_thursday.value = ""
        self.tf_km_friday.value = ""
        self.tf_km_saturday.value = ""
        
    #event
    def register_new_driver(self, e): 
        #Save data
        name = self.tf_name.value
        age  = self.tf_age.value
        city = self.tf_city.value
        kilometers = {
            'monday': float(self.tf_km_monday.value),
            'tuesday': float(self.tf_km_tuesday.value),
            'wednesday': float(self.tf_km_wednesday.value),
            'thursday': float(self.tf_km_thursday.value),
            'friday': float(self.tf_km_friday.value),
            'saturday': float(self.tf_km_saturday.value)
        }
        total = sum(kilometers.values())
        
        driver = Driver(name, age, city, kilometers, total) 
        DriversTableView().add(driver)
        GraphView().add(driver)
        
        #Clean form 
        self.clean_form()
            
    #form design - inputs
    tf_name = ft.TextField(label="Nombre del chofer", width=1000)
    tf_age  = ft.TextField(label="Edad", width=160)
    tf_city = ft.TextField(label="Ciudad de origen", width=1170)
    tf_km_monday    = ft.TextField(label="Km", width=190, height=30, cursor_height=15)
    tf_km_tuesday   = ft.TextField(label="Km", width=190, height=30, cursor_height=15)
    tf_km_wednesday = ft.TextField(label="Km", width=190, height=30, cursor_height=15)
    tf_km_thursday  = ft.TextField(label="Km", width=190, height=30, cursor_height=15)
    tf_km_friday    = ft.TextField(label="Km", width=190, height=30, cursor_height=15)
    tf_km_saturday  = ft.TextField(label="Km", width=190, height=30, cursor_height=15)

    btn_register = ft.ElevatedButton(text="Registrar chofer", width=200, bgcolor='#395144', color=ft.colors.WHITE)
    
    #initialize form - design
    def init_form(self): 
        form = ft.Container(
            width=1200,
            margin=ft.margin.all(20),
            border=ft.border.all(1, ft.colors.BLACK87),
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.colors.BLACK45,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            padding=15,
            content=ft.Column(
                expand=True, 
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Datos del Chofer", size=40)
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.tf_name, self.tf_age
                        ], 
                        alignment=ft.CrossAxisAlignment.CENTER
                    ), 
                    ft.Row(
                        controls=[
                            self.tf_city
                        ]
                    ), 
                    ft.Row(
                        controls=[
                            ft.Text("Kilometros recorridos por día", size=40)    
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.DataTable(
                                width=1170,
                                height=250,
                                columns=[
                                    ft.DataColumn(ft.Text("Lunes")),
                                    ft.DataColumn(ft.Text("Martes")),
                                    ft.DataColumn(ft.Text("Miércoles")),
                                    ft.DataColumn(ft.Text("Jueves")),
                                    ft.DataColumn(ft.Text("Viernes")),
                                    ft.DataColumn(ft.Text("Sábado")),
                                ], 
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(self.tf_km_monday),
                                            ft.DataCell(self.tf_km_tuesday),
                                            ft.DataCell(self.tf_km_wednesday),
                                            ft.DataCell(self.tf_km_thursday),
                                            ft.DataCell(self.tf_km_friday),
                                            ft.DataCell(self.tf_km_saturday),
                                        ]
                                    )
                                ]
                            )
                        ]
                    ), 
                    ft.Row(
                        controls=[
                            self.btn_register
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ) 
        )
        
        self.btn_register.on_click = self.register_new_driver
        
        return form