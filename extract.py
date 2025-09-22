import re

def extract_skills(text):
    skills = ['Python', 'Java', 'SQL', 'Machine Learning', 'JavaScript', 'HTML', 'CSS']
    found = [skill for skill in skills if skill.lower() in text.lower()]
    return found

def extract_languages(text):
    langs = ['English', 'Mandarin', 'Hindi', 'French']
    return [lang for lang in langs if lang.lower() in text.lower()]
