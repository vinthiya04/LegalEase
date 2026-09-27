def format_html_preview(text):

    return f"""
    <div style="
        background:#1e1e1e;
        color:white;
        padding:20px;
        border-radius:10px;
        overflow:auto;
        height:500px;">
        <pre>{text}</pre>
    </div>
    """