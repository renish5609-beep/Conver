from core.mock_data import generate_mock_feedback
from core.state import set_value, append_history, get_state

def analyze_response(text: str, mode: str) -> dict:
    analysis = generate_mock_feedback(text, mode)
    set_value('last_analysis', analysis)

    if text.strip():
        state = get_state()
        append_history({
            'scenario': mode,
            'profile': state['selected_profile'],
            'input': text,
            'analysis': analysis,
        })

    return analysis