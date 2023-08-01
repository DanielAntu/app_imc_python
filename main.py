import flet as ft
from calculadora import calcular_imc, mens_sit

def main(page: ft.Page):
    page.title = 'IMC'

    # resultado
    res_imc = 0
    res = 'Não Informado'

    # controle
    peso = ft.TextField(label='Exemplo 70', bgcolor=ft.colors.WHITE, border=None)
    altura = ft.TextField(label='Exemplo 1.80', bgcolor=ft.colors.WHITE, border=None)
    resultado_imc = ft.TextField(value=str(res_imc), read_only=True, text_align=ft.alignment.center, text_size=25, color=ft.colors.WHITE, border_color=ft.colors.BLUE)
    resultado = ft.TextField(value=str(res), read_only=True, text_align=ft.alignment.center, text_size=25, color=ft.colors.WHITE, border_color=ft.colors.BLUE)

    def click(e):
        res_imc = calcular_imc(peso.value, altura.value)
        res = mens_sit(res_imc)

        resultado_imc.value = str(f'{res_imc:.2f}')
        resultado.value = str(res)
        page.update()

    botao = ft.ElevatedButton(text='Calcular', bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, width=400, on_click=click)

    #container
    c1 = ft.Container(
        ft.Column(
            [
                peso,
                altura,
                botao
            ]
        ),
        bgcolor=ft.colors.BLUE,
        padding=10,
        width=400,
        border_radius=10,
    )
    c2 = ft.Container(
        ft.Column(
            [
                ft.Text('O seu IMC esta abaixo', color=ft.colors.WHITE, text_align=ft.alignment.center, size=20),
                resultado_imc,
                resultado
            ],
        ),
        bgcolor=ft.colors.BLUE,
        padding=10,
        width=400,
        border_radius=10,
        alignment=ft.alignment.center
    )

    page.add(c1, c2)



ft.app(target=main)