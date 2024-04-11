import flet as ft

from views import appbar, FormView, MainMenuView, DriversTableView, GraphView

main_menu = MainMenuView()
form = FormView()
drivers_table = DriversTableView()
drivers_graph = GraphView()

def main(page: ft.Page):
    #Window settings
    page.window_width = 1280
    page.window_height = 720
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()
    page.window_maximizable = False
    page.window_resizable = False
    page.title = "Compañía de Transportes"
    
    #Routing setting
    def route_change(route): 
        page.views.clear()
        page.views.append(
            ft.View(
                "/", 
                [
                    appbar, 
                    main_menu.init_main_menu()
                ]
            )
        )
        
        if page.route == "/driver-form": 
            page.views.append(
                ft.View(
                    "/driver-form", 
                    [
                        appbar, 
                        form.init_form()
                    ]
                )
            )
            
        if page.route == "/drivers-table": 
            page.views.append(
                ft.View(
                    "/drivers-table", 
                    [
                        appbar, 
                        drivers_table.init_drivers_table()
                    ]
                )
            )   
            
        if page.route == "/drivers-graph": 
            page.views.append(
                ft.View(
                    "/drivers-graph", 
                    [
                        appbar, 
                        drivers_graph.init_graph()
                    ]
                )
            ) 
            
        page.update()
        
    def view_pop(view): 
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
    def go_to_driver_form(e): 
        page.go("/driver-form")
        
    def go_to_drivers_table(e): 
        page.go("/drivers-table")
    
    def go_to_drivers_graph(e): 
        page.go("/drivers-graph")
    
    appbar.actions[0].on_click = go_to_driver_form
    appbar.actions[1].on_click = go_to_drivers_table
    appbar.actions[2].on_click = go_to_drivers_graph
    
ft.app(target=main)