import flet as ft

def main(page: ft.Page):
    page.title = "Academia"

    page.window_width = 405
    page.window_height = 720

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def login(mt,sh):
        if mt.value=='231080174'and sh.value == '12345':
            ft.app(target=usuario)
            print('Entrou')
            print(mt.value,sh.value)
        else:
            print('Informações inválidas')
            print(mt.value,sh.value)

    mat_txt = ft.Text(value='Matricula:', text_align=ft.TextAlign.CENTER, color='black')
    mat_button = ft.TextField(value="", text_align=ft.TextAlign.CENTER,height=50, width=200, color='black')
    senha_txt = ft.Text(value='Senha:', text_align=ft.TextAlign.CENTER, color='black')
    senha_button = ft.TextField(value="", text_align=ft.TextAlign.CENTER,height=50, width=200, color='black')
    #enter = ft.FilledButton(text="Entrar", icon_color=ft.colors.GREEN, )

    enter = ft.Container(
        width=200,
        height=45,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN,
        border_radius=10,
        content=ft.Text(value='Entrar',size=15, color='white'),
        on_click=lambda e: login(mat_button,senha_button),
    )

    bv = ft.Text(value='Bem Vindo', text_align=ft.TextAlign.CENTER,size=30, color='black')

    page.add(
        ft.Row(
            controls=[
                ft.Column([
                    bv,
                    mat_txt,
                    mat_button,
                    senha_txt,
                    senha_button,
                    enter
                ])
            ], alignment=ft.MainAxisAlignment.CENTER)
    )

def usuario(page: ft.Page):
    page.title = "Academia"

    page.window_width = 405
    page.window_height = 720

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(ft.Text('Area aluno'))

ft.app(target=main)