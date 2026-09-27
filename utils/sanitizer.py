def sanitize_text(text):

    text = text.replace("“", '"')
    text = text.replace("”", '"')
    text = text.replace("’", "'")

    return text.strip()