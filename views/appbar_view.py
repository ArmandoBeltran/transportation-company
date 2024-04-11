import flet as ft 

appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.FIRE_TRUCK),
            leading_width=40, 
            title=ft.Text("Compañía de Transportes"), 
            center_title=True, 
            bgcolor='#395144', 
            actions=[
                ft.IconButton(ft.icons.ADD_CIRCLE_ROUNDED),
                ft.IconButton(ft.icons.TABLE_CHART),
                ft.IconButton(ft.icons.AUTO_GRAPH),
            ]
        )