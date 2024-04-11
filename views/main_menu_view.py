import flet as ft

class MainMenuView(): 
    
    def init_main_menu(self): 
        main_menu = ft.Container(
            height=600,
            content=ft.Column(
                expand=True, 
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Bienvenido al sistema de administración de Transportes", size=40, text_align=ft.TextAlign.CENTER)
                        ], 
                        alignment=ft.MainAxisAlignment.CENTER, 
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.ADD_CIRCLE_ROUNDED, size=48), 
                            ft.Icon(name=ft.icons.TABLE_CHART, size=48),
                            ft.Icon(name=ft.icons.AUTO_GRAPH, size=48)
                        ], 
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ], 
            ), 
        )
        
        return main_menu