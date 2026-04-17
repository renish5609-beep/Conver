from nicegui import ui
from core.state import get_state

def render_hero():
    state = get_state()

    with ui.element('section').classes('hero-card'):
        ui.label('AI Conversation Intelligence').classes('hero-badge')
        ui.label('Conver').classes('hero-title')
        ui.label('Turn conversations into intelligence.').classes('hero-subtitle')
        ui.label(
            'A modern communication workspace for practicing, analyzing, and improving how you sound across interviews, pitches, debates, leadership scenarios, and real-world conversations.'
        ).classes('hero-description')

        with ui.row().classes('hero-chip-row'):
            ui.label(f"Scenario: {state['selected_scenario']}").classes('hero-chip')
            ui.label(f"Coach: {state['selected_profile']}").classes('hero-chip')
            ui.label(
                f"Companion: {'Enabled' if state['companion_enabled'] else 'Disabled'}"
            ).classes('hero-chip')