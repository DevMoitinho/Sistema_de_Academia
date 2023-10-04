import flet as ft
import BD

#testando git

BD.lerBD()
print(BD.usuarios)

def main(page: ft.Page):
    page.title = "Academia"

    page.window_width = 405
    page.window_height = 720

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    

    mat_txt = ft.Text(value='Matricula:', text_align=ft.TextAlign.CENTER, color='black')
    mat_button = ft.TextField(value="", text_align=ft.TextAlign.CENTER,height=50, width=200, color='black')
    senha_txt = ft.Text(value='Senha:', text_align=ft.TextAlign.CENTER, color='black')
    senha_button = ft.TextField(value="", text_align=ft.TextAlign.CENTER,height=50, width=200, color='black')

    enter = ft.Container(
        width=200,
        height=45,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN,
        border_radius=10,
        content=ft.Text(value='Entrar',size=15, color='white'),
        on_click=lambda e: BD.login(mat_button.value,senha_button.value),
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