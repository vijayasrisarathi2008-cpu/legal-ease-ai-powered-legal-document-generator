import re


def sanitize_text(text):
    """
    Clean generated text before exporting.
    """

    text = text.replace("“", '"')
    text = text.replace("”", '"')
    text = text.replace("‘", "'")
    text = text.replace("’", "'")

    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    return text.strip()


def format_html_preview(text):

    text = sanitize_text(text)

    html = text.replace("\n", "<br>")

    return f"""
    <div style="
        background-color:#111827;
        color:white;
        padding:25px;
        border-radius:12px;
        line-height:1.7;
        font-family:Arial;
    ">
        {html}
    </div>
    """
