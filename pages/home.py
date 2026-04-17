from nicegui import ui
from components.navbar import render_navbar
from components.hero import render_hero
from core.state import get_state

def build_home_page():
    state = get_state()

    with ui.element('div').classes('page-shell'):
        render_navbar('Overview')
        render_hero()

        with ui.row().classes('overview-grid'):
            with ui.element('div').classes('feature-card feature-card-large'):
                ui.label('Practice Lab').classes('feature-title')
                ui.label(
                    'Run scenario-based speaking sessions, analyze response drafts, and prepare for future live voice coaching.'
                ).classes('feature-text')
                ui.link('Open Practice Lab →', '/practice').classes('feature-link')

            with ui.element('div').classes('feature-card'):
                ui.label('Briefing').classes('feature-title')
                ui.label(
                    'Set up the situation before you practice so your future AI coaching has context.'
                ).classes('feature-text')
                ui.link('Open Briefing →', '/briefing').classes('feature-link')

            with ui.element('div').classes('feature-card'):
                ui.label('AI Profiles').classes('feature-title')
                ui.label(
                    'Choose who coaches you and how that coach will eventually speak, critique, and guide.'
                ).classes('feature-text')
                ui.link('Explore AI Profiles →', '/ai-profiles').classes('feature-link')

        with ui.row().classes('dashboard-grid'):
            with ui.element('div').classes('dashboard-card'):
                ui.label('Current Scenario').classes('dashboard-title')
                ui.label(state['selected_scenario']).classes('dashboard-metric')
                ui.label('This is shared across the app').classes('dashboard-subtext')

            with ui.element('div').classes('dashboard-card'):
                ui.label('Active Coach').classes('dashboard-title')
                ui.label(state['selected_profile']).classes('dashboard-metric')
                ui.label('Profile selection affects future feedback style').classes('dashboard-subtext')

            with ui.element('div').classes('dashboard-card'):
                ui.label('Companion State').classes('dashboard-title')
                ui.label('Enabled' if state['companion_enabled'] else 'Disabled').classes('dashboard-metric')
                ui.label('This setting will later affect live session behavior').classes('dashboard-subtext')

        with ui.row().classes('overview-grid'):
            with ui.element('div').classes('result-card wide-card'):
                ui.label('Connected Product Logic').classes('result-title')
                ui.label(
                    'Selections in Briefing, AI Profiles, and Settings now feed directly into Practice, Overview, Insights, and History through shared app state.'
                ).classes('result-text')