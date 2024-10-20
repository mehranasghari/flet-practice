
import flet as ft

def ui(page: ft.Page):
    page.title = 'test page'
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    dummy_text = ft.Text(value="Hello, it's me", text_align=ft.MainAxisAlignment.CENTER, opacity=.5)

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (', '.join(map(lambda f: f.name, e.files)) if e.files else 'canceled')
        selected_files.update()

    file_picker_dialog = ft.FilePicker(on_result=pick_files_result)

    selected_files = ft.Text()
    
    page.overlay.append(file_picker_dialog)

    t = ft.Tabs(
        selected_index=0,
        animation_duration=200,
        tabs=[
            ft.Tab(
                text='backup',
                content=ft.Text("Hello this is tab1"),
            ),
            ft.Tab(
                text='restore',
                content=ft.Text("Restore tab2"),
            ),
        ],
        expand=1
    )

    page.add(t)
    # page.add(ft.Row([
    #     dummy_text, ft.ElevatedButton('select file', icon=ft.icons.UPLOAD_FILE, on_click=file_picker_dialog.pick_files), selected_files
    # ]))

ft.app(target=ui)
