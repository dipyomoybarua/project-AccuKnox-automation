def extract_message(response):
    """Extracts and returns the message from the JSON response."""
    try:
        return response.json().get('message', '')
    except ValueError:
        return ''
