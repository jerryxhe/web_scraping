from polyglot.text import Text

def get_pos_tags(sentence, lang='en'):
    text = Text(sentence)
    text.hint_language_code=lang
    return text.pos_tags
