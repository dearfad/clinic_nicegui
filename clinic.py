from nicegui import ui

select = ui.select([1,2,4], label='请选择：').props("standard").classes('w-1/3 justify-center')

ui.run()
