import flet as ft 

class DriversTableView(): 
    
    drivers = []
    
    def add(self, driver): 
        self.drivers.append(driver)
    
    def init_drivers_table(self): 
        if self.drivers: 
            drivers_table = ft.Container(
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
                content=ft.DataTable(
                    vertical_lines=ft.border.BorderSide(1, ft.colors.BLACK87),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.BLACK87),
                    columns=[
                        ft.DataColumn(ft.Text("Nombre")), 
                        ft.DataColumn(ft.Text("Lunes")),
                        ft.DataColumn(ft.Text("Martes")),
                        ft.DataColumn(ft.Text("Miércoles")),
                        ft.DataColumn(ft.Text("Jueves")),
                        ft.DataColumn(ft.Text("Viernes")),
                        ft.DataColumn(ft.Text("Sábado")),
                        ft.DataColumn(ft.Text("Total Km")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(driver.name)), 
                                ft.DataCell(ft.Text(driver.kilometers.get("monday"))),
                                ft.DataCell(ft.Text(driver.kilometers.get("tuesday"))),
                                ft.DataCell(ft.Text(driver.kilometers.get("wednesday"))),
                                ft.DataCell(ft.Text(driver.kilometers.get("thursday"))),
                                ft.DataCell(ft.Text(driver.kilometers.get("friday"))),
                                ft.DataCell(ft.Text(driver.kilometers.get("saturday"))),
                                ft.DataCell(ft.Text(driver.total))
                            ]
                        ) for driver in self.drivers
                    ]
                )
            )
        else: 
            drivers_table = ft.Container(
                height=600,
                content=ft.Column(
                    expand=True, 
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(name=ft.icons.HOURGLASS_EMPTY, size=100), 
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                             controls=[
                                ft.Text("No hay choferes registrados", size=40, text_align=ft.TextAlign.CENTER)
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER, 
                        ),
                        ft.Row(
                             controls=[
                                ft.Text("Registra choferes junto con sus kilometros recorridos para ver sus datos aquí", size=15)
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER, 
                        )
                    ], 
                ), 
            )
        
        return drivers_table
        