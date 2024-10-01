import flet as ft
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    # page.add(ft.Text('Hello world!'))

    # input_filed = ft.TextField(label="Please enter your magic word", text_align="left",\
    #     autofocus=True, multiline=True, border="none", filled=True, suffix_text="shiiiiiiiiit",\
    #     )
    # output_text = ft.Text()
    # def on_button_click(e):
    #     output_text.value = f"you enterd: {input_filed.value}"
    #     page.update()
    # submit_button = ft.OutlinedButton(text="Submit", on_click=on_button_click)
    # page.add(input_filed, submit_button, output_text)

    page.title = "COUNTER BOY"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'dark'

    text_number = ft.TextField(value='0', text_align=ft.TextAlign.RIGHT, width=100)

    def decrement(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=decrement), text_number,
             ft.IconButton(ft.icons.ADD, on_click=increment)
             ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)