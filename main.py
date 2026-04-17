from nicegui import ui, app
from pages.home import build_home_page
from pages.practice import build_practice_page
from pages.briefing import build_briefing_page
from pages.ai_profiles import build_ai_profiles_page
from pages.companion import build_companion_page
from pages.insights import build_insights_page
from pages.history import build_history_page
from pages.settings import build_settings_page

app.add_static_files('/static', 'static')

ui.add_head_html('''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/styles.css">
''', shared=True)

@ui.page('/')
def home():
    build_home_page()

@ui.page('/practice')
def practice():
    build_practice_page()

@ui.page('/briefing')
def briefing():
    build_briefing_page()

@ui.page('/ai-profiles')
def ai_profiles():
    build_ai_profiles_page()

@ui.page('/companion')
def companion():
    build_companion_page()

@ui.page('/insights')
def insights():
    build_insights_page()

@ui.page('/history')
def history():
    build_history_page()

@ui.page('/settings')
def settings():
    build_settings_page()

ui.run(title='Conver', favicon='🎤', reload=True)