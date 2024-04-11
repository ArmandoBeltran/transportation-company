import flet as ft
import random

class GraphView: 
    
    drivers = []
    
    def add(self, driver): 
        self.drivers.append(driver)
    
    def init_graph(self): 
        if self.drivers: 
            graph = ft.BarChart(
                height=700,
                bar_groups=[
                    ft.BarChartGroup(
                        x = i, 
                        bar_rods=[
                            ft.BarChartRod(
                                from_y=0, 
                                to_y=driver.total, 
                                width=40, 
                                color='#' + ''.join(random.choices('0123456789ABCDEF', k=6)), 
                                tooltip=f"{driver.name}", 
                                border_radius=0
                            ),
                        ],
                    ) for i, driver in enumerate(self.drivers)
                ], 
                border=ft.border.all(1, ft.colors.GREY_400), 
                left_axis=ft.ChartAxis(
                    labels_size=40, title=ft.Text("Total de Kilometros"), title_size=40
                ), 
                bottom_axis=ft.ChartAxis(
                    labels=[
                        ft.ChartAxisLabel(
                            value=i, label=ft.Container(ft.Text(driver.name), padding=10)
                        ) for i, driver in enumerate(self.drivers)
                    ], 
                    labels_size=40,
                ),
                horizontal_grid_lines=ft.ChartGridLines(
                    color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
                ),
                tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
                max_y=max([driver.total for driver in self.drivers]) + 10,
                interactive=True, 
                expand=True
            )
        else: 
            graph = ft.Container(
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
                                ft.Text("Registra choferes junto con sus kilometros recorridos para ver sus gráficas aquí", size=15)
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER, 
                        )
                    ], 
                ), 
            )
        
        return graph
    