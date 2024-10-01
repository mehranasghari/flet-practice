import flet as ft
from flet_core import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Sign up"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    text_username = ft.TextField(label="Username", text_align=ft.TextAlign.LEFT, width=200)
    text_password = ft.TextField(label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup = ft.Checkbox(label="I agree to stuff", value=False)
    button_submit = ft.ElevatedButton(text="Sign up", width=200, disabled=True)

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()

    def submit(e: ControlEvent) -> None:
        print('Username', text_username.value)
        print('Password', text_password.value)

        page.clean()
        page.add(
            ft.Row(
                controls = [ft.Text(value=f"Welecom {text_username.value}", size=20)],
                alignment = ft.MainAxisAlignment.CENTER
            )
        )

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit
    
    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    [text_username, 
                     text_password,
                     checkbox_signup,
                     button_submit]
                )
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)