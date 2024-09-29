from nicegui import ui

from libs.bvcclasses import Role

with ui.grid(columns=3).classes('w-full'):
    with ui.column():
        pass
    with ui.column():
        select = ui.select([role.value for role in Role], label='请选择：').props("borderless").classes('w-full')
    with ui.column():
        pass

ui.run()
