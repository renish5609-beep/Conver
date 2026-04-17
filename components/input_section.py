from nicegui import ui
from core.state import get_state, set_value

def render_input_section(on_analyze):
    state = get_state()

    with ui.element('section').classes('panel-card'):
        ui.label('Practice Session').classes('section-title')

        with ui.row().classes('input-grid'):
            with ui.column().classes('left-pane'):
                mode = ui.select(
                    ['Interview', 'Pitch', 'Debate', 'Casual Conversation', 'Leadership', 'Networking'],
                    value=state['selected_scenario'],
                    label='Scenario',
                ).classes('full-width modern-field')

                def on_mode_change():
                    set_value('selected_scenario', mode.value)

                mode.on('update:model-value', lambda e: on_mode_change())

                with ui.element('div').classes('info-card'):
                    ui.label('Mode Focus').classes('info-title')
                    ui.label(
                        'The selected scenario affects your briefing context, future coaching style, and how the app will eventually analyze your communication.'
                    ).classes('info-text')

                with ui.element('div').classes('mini-stat-card'):
                    ui.label('Active Coach').classes('mini-stat-label')
                    ui.label(state['selected_profile']).classes('mini-stat-value')
                    ui.label(
                        'Your selected AI profile will later influence tone, strictness, and speaking style.'
                    ).classes('mini-stat-subvalue')

            with ui.column().classes('right-pane'):
                text = ui.textarea(
                    label='Response Draft',
                    value=state['last_input'],
                    placeholder='Type or paste a response here...',
                ).props('outlined autogrow').classes('full-width response-box modern-field')

                def handle_click():
                    set_value('selected_scenario', mode.value)
                    set_value('last_input', text.value or '')
                    on_analyze({
                        'mode': mode.value,
                        'text': text.value or '',
                    })

                ui.button('Analyze Response', on_click=handle_click).classes('analyze-btn')