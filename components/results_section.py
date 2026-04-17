from nicegui import ui

def score_card(title: str, value: int, caption: str):
    with ui.element('div').classes('score-card'):
        ui.label(title).classes('score-label')
        ui.label(str(value)).classes('score-value')
        ui.label(caption).classes('score-caption')

def bullet_block(title: str, items: list[str]):
    with ui.element('div').classes('result-card'):
        ui.label(title).classes('result-title')
        with ui.column().classes('bullet-list'):
            for item in items:
                ui.label(f'• {item}').classes('bullet-item')

def render_results_section(analysis: dict):
    with ui.element('div').classes('results-shell'):
        ui.label('Session Analysis').classes('section-title results-title')

        with ui.row().classes('score-grid'):
            score_card('Clarity', analysis['clarity'], 'how clearly your ideas landed')
            score_card('Confidence', analysis['confidence'], 'how assured you came across')
            score_card('Persuasion', analysis['persuasion'], 'how convincing your response felt')

        with ui.row().classes('results-grid'):
            with ui.column().classes('results-col'):
                bullet_block('What worked', analysis['strengths'])
                bullet_block('Areas to improve', analysis['improvements'])

            with ui.column().classes('results-col'):
                with ui.element('div').classes('result-card'):
                    ui.label('Communication Read').classes('result-title')
                    ui.label(analysis['filler_feedback']).classes('result-text')

                with ui.element('div').classes('result-card'):
                    ui.label('Stronger Version').classes('result-title')
                    ui.label(analysis['rewrite']).classes('result-text')