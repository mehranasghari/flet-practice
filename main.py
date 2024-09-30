import flet as ft

def main(page: ft.Page):
    # page.add(ft.Text('Hello world!'))

    input_filed = ft.TextField(label="Please enter your magic word", text_align="left",\
        autofocus=True, multiline=True, border="none", filled=True, suffix_text="shiiiiiiiiit",\
        )
    
    output_text = ft.Text()

    def on_button_click(e):
        output_text.value = f"you enterd: {input_filed.value}"
        page.update()

    submit_button = ft.TextButton(text="Submit", on_click=on_button_click)

    page.add(input_filed, submit_button, output_text)


ft.app(target=main)