import flet as ft

async def main(page: ft.Page):

    #Configuración de la ventana principal
    page.window_width = 720
    page.window_height = 1280
    page.window_resizable = False
    page.padding = 0

    #Elementos del container 'upper'
    upper_items = [
        ft.Container(width=80, height=80, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
        ft.Container(width=40, height=40, border=ft.border.all()),
    ]


    #Containers interiores
    upper = ft.Container(content=ft.Row(upper_items), width=600, height=80, margin=ft.margin.only(top=40), border=ft.border.all())
    center = ft.Container(width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all())
    bottom = ft.Container(width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all())

    #Columnas de la interfaz
    col = ft.Column(spacing=0, controls=[
        upper,
        center,
        bottom
    ])

    #Contenedor principal
    contenedor = ft.Container(col, width=720, height=1280, bgcolor=ft.colors.RED, alignment=ft.alignment.top_center)

ft.app(target=main)