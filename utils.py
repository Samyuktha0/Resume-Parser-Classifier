def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())

def load_resume(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
