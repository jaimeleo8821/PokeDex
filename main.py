import flet as ft
import aiohttp
import asyncio

actual_pokemon = 1

async def main(page: ft.Page):

    #Configuración de la ventana principal
    page.window_width = 720
    page.window_height = 1080
    page.window_resizable = False
    page.scroll = True
    page.padding = 0

    # Functions
    async def fetch(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def evento_vacio(e: ft.ContainerTapEvent):
        global actual_pokemon
        print("Evento!", e)
        if e.control == upArrow:
            actual_pokemon += 1
        elif e.control == downArrow:
            actual_pokemon -= 1    

        maxPkmNumber = (actual_pokemon%150) + 1
        result = await fetch(f"https://pokeapi.co/api/v2/pokemon/{maxPkmNumber}")
        
        texto.value = f"Id: {result['id']}\nName: {result['name']}"
        pkmImage.src = result['sprites']['front_default']
        await page.update_async()


    # ft Containers

    blue_button = ft.Stack([
            ft.Container(width=80, height=80, bgcolor=ft.colors.WHITE, border_radius=50),
            ft.Container(width=70, height=70, left=5, top=5, bgcolor=ft.colors.BLUE, border_radius=50)
    ])

    #Elementos del container 'upper'
    upper_items = [
        ft.Container(blue_button, width=80, height=80),
        ft.Container(width=40, height=40, bgcolor=ft.colors.RED_200, border_radius=50),
        ft.Container(width=40, height=40, bgcolor=ft.colors.YELLOW, border_radius=50),
        ft.Container(width=40, height=40, bgcolor=ft.colors.GREEN, border_radius=50),
    ]

    #Elementos del container 'middle'
    pkmImage = ft.Image(
            src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{actual_pokemon}.png",
            scale=6,
            width=50,
            height=50,
            top=350/2,
            left=550/2
        )
    middle_items = ft.Stack([
        ft.Container(width=600, height=400, bgcolor=ft.colors.WHITE),
        ft.Container(width=550, height=350, bgcolor=ft.colors.BLACK, top=25, left=25),
        pkmImage
    ])
    
    #Elementos del container 'bottom'
    upArrow = ft.Container(width=45, height= 55, bgcolor=ft.colors.BLUE, on_click=evento_vacio)
    downArrow = ft.Container(width=45, height= 55, bgcolor=ft.colors.YELLOW, on_click=evento_vacio)
    leftArrow = ft.Container(width=60, height= 40, bgcolor=ft.colors.WHITE, on_click=evento_vacio)
    rightArrow = ft.Container(width=60, height= 40, bgcolor=ft.colors.BLACK, on_click=evento_vacio)

    column1 = ft.Column([
        ft.Container(width=50, height= 45),
        leftArrow,
        ft.Container(width=50, height= 45)
    ], alignment=ft.alignment.center)

    column2 = ft.Column([
        upArrow,
        ft.Container(width=20, height= 20),
        downArrow
    ], alignment=ft.alignment.center)

    column3 = ft.Column([
        ft.Container(width=50, height= 45),
        rightArrow,
        ft.Container(width=50, height= 45)
    ], alignment=ft.alignment.center)

    texto = ft.Text(
        value="...",
        color= ft.colors.BLACK,
        size= 22,

    )
    bottom_items = [
        ft.Container(width=50, border=ft.border.all()), #Margen Izquierdo
        ft.Container(texto, padding=5, width=300, height=150, bgcolor=ft.colors.GREEN_200, border_radius=20), #Green Screen
        ft.Container(content=ft.Row([column1, column2, column3]), width=170, height=150, alignment=ft.alignment.center), #Arrow Buttons
        ft.Container(width=50, border=ft.border.all()) #Margen Derecho
    ]


    #Containers interiores
    upper = ft.Container(content=ft.Row(upper_items), width=600, height=80, margin=ft.margin.only(top=40))
    center = ft.Container(content=middle_items, width=600, height=400, margin=ft.margin.only(top=40), alignment=ft.alignment.center)
    bottom = ft.Container(content=ft.Row(bottom_items), width=600, height=400, margin=ft.margin.only(top=40), border=ft.border.all())

    #Columnas de la interfaz
    col = ft.Column(spacing=0, controls=[
        upper,
        center,
        bottom
    ])

    #Contenedor principal
    contenedor = ft.Container(col, width=720, height=1280, bgcolor=ft.colors.RED, alignment=ft.alignment.top_center)

    await page.add_async(contenedor)

ft.app(target=main)