from core.state import get_state

def generate_mock_feedback(text: str, mode: str) -> dict:
    state = get_state()
    profile = state['selected_profile']

    lowered = text.lower()
    filler_words = ['um', 'uh', 'like', 'you know', 'basically', 'actually']
    filler_count = sum(lowered.count(word) for word in filler_words)
    word_count = len(text.split()) if text.strip() else 0

    clarity = max(5, min(10, 9 - filler_count))
    confidence = max(5, min(10, 6 + word_count // 25))
    persuasion = 7 if mode in ['Interview', 'Pitch', 'Debate', 'Leadership', 'Networking'] else 6

    if profile == 'Blaze':
        strengths = [
            'Your response had a clear point.',
            'You sounded more decisive than passive.',
            'The answer had decent forward momentum.'
        ]
        improvements = [
            'Cut softer language and get to the point faster.',
            'Use a sharper example that proves your value.',
            'End more forcefully instead of drifting out.'
        ]
    elif profile == 'Echo':
        strengths = [
            'Your response felt calm and approachable.',
            'You maintained a steady tone.',
            'The answer felt natural and not overly forced.'
        ]
        improvements = [
            'Be a little more direct with your key point.',
            'Add one concrete example to build trust.',
            'Close with more confidence so the response lands better.'
        ]
    else:
        strengths = [
            'Your response had a visible central idea.',
            'Your tone felt measured rather than rushed.',
            'The answer generally matched the selected scenario.'
        ]
        improvements = [
            'Tighten filler phrases so the delivery feels sharper.',
            'Use one concrete example to make the point more believable.',
            'End on a stronger closing line instead of fading out.'
        ]

    if not text.strip():
        return {
            'clarity': 0,
            'confidence': 0,
            'persuasion': 0,
            'strengths': ['No response has been analyzed yet.'],
            'improvements': ['Enter a response to begin getting communication feedback.'],
            'filler_feedback': 'Conver is ready, but no content has been analyzed yet.',
            'rewrite': 'Your stronger version will appear here after you submit a response.',
        }

    return {
        'clarity': clarity,
        'confidence': confidence,
        'persuasion': persuasion,
        'strengths': strengths,
        'improvements': improvements,
        'filler_feedback': f'We detected {filler_count} likely filler phrase(s). The response would sound cleaner with more deliberate phrasing.',
        'rewrite': f'[{profile} coach style] I focused on the core issue, kept my response structured, and made sure my point landed clearly and confidently.',
    }