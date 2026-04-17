from nicegui import ui
from pages.home import build_home

ui.add_head_html('''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/styles.css">
''')

build_home()

ui.run(
    title='Conver',
    favicon='🎤',
    reload=True,
)
