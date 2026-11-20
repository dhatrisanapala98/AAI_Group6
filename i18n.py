"""Local interface translations. Dify alone generates/translates final reports.

Stable English values stay in routes, action IDs and API payloads. Only display
text passes through t(). Questions, evidence and approved plans stay verbatim.
"""
from __future__ import annotations
import json
from pathlib import Path
import re
import streamlit as st

# (Dify report_language value, native label, code, right-to-left)
# The 22 scheduled languages of India plus English. The Dify value is what the
# published workflow receives, so it must match its report_language options.
_LANG_TABLE = [
    ('English', 'English', 'en', False),
    ('Hindi हिन्दी', 'हिन्दी', 'hi', False),
    ('Bengali বাংলা', 'বাংলা', 'bn', False),
    ('Telugu తెలుగు', 'తెలుగు', 'te', False),
    ('Marathi मराठी', 'मराठी', 'mr', False),
    ('Tamil தமிழ்', 'தமிழ்', 'ta', False),
    ('Urdu اردو', 'اردو', 'ur', True),
    ('Gujarati ગુજરાતી', 'ગુજરાતી', 'gu', False),
    ('Kannada ಕನ್ನಡ', 'ಕನ್ನಡ', 'kn', False),
    ('Odia ଓଡ଼ିଆ', 'ଓଡ଼ିଆ', 'or', False),
    ('Malayalam മലയാളം', 'മലയാളം', 'ml', False),
    ('Punjabi ਪੰਜਾਬੀ', 'ਪੰਜਾਬੀ', 'pa', False),
    ('Assamese অসমীয়া', 'অসমীয়া', 'as', False),
    ('Maithili मैथिली', 'मैथिली', 'mai', False),
    ('Santali ᱥᱟᱱᱛᱟᱲᱤ', 'ᱥᱟᱱᱛᱟᱲᱤ', 'sat', False),
    ('Kashmiri کٲشُر', 'کٲشُر', 'ks', True),
    ('Nepali नेपाली', 'नेपाली', 'ne', False),
    ('Sindhi سنڌي', 'سنڌي', 'sd', True),
    ('Konkani कोंकणी', 'कोंकणी', 'kok', False),
    ('Dogri डोगरी', 'डोगरी', 'doi', False),
    ('Manipuri (Meitei) ꯃꯤꯇꯩꯂꯣꯟ', 'ꯃꯤꯇꯩꯂꯣꯟ', 'mni', False),
    ('Bodo बड़ो', 'बड़ो', 'brx', False),
    ('Sanskrit संस्कृतम्', 'संस्कृतम्', 'sa', False),
]
LANGUAGES = [row[0] for row in _LANG_TABLE]
LANGUAGE_LABELS = {row[0]: row[1] for row in _LANG_TABLE}
LANGUAGE_CODES = {row[0]: row[2] for row in _LANG_TABLE}
RTL_CODES = {row[2] for row in _LANG_TABLE if row[3]}
LOCALES_DIR = Path(__file__).parent / 'locales'


def language() -> str:
    selected = st.session_state.get('ui_language', 'English')
    return selected if selected in LANGUAGES else 'English'


def has_interface_translation(code: str) -> bool:
    """True when the interface has a message catalog for this language.

    Report generation covers every language through Dify. Interface labels are
    translated for the languages that have a catalog; the rest show English labels.
    """
    return code == 'en' or (LOCALES_DIR / (code + '.json')).is_file()


@st.cache_data(show_spinner=False)
def catalog(code: str) -> dict[str, str]:
    path = LOCALES_DIR / (code + '.json')
    if code == 'en' or not path.is_file():
        return {}
    return json.loads(path.read_text(encoding='utf-8'))


def t(message: str, *, locale: str | None = None, **values) -> str:
    message = str(message)
    code = LANGUAGE_CODES.get(locale or language(), 'en')
    translated = catalog(code).get(message, message)
    return translated.format(**values) if values else translated


def localize_diagnostic(message: str) -> str:
    """Translate our messages, preserving the server's original technical detail."""
    output = []
    for line in str(message).splitlines():
        if line.startswith('Dify response: '):
            output.append(t('Dify response:') + ' ' + line[len('Dify response: '):])
        else:
            output.append(t(line))
    return '\n'.join(output)


def localize_review_content(content: str) -> str:
    """Translate known template labels/instructions without rewriting source data.

    Match exact standalone lines or known bold label prefixes. Never translate
    a student's name, a retrieved quotation, a draft or a reviewer's submitted text.
    """
    lines = []
    in_source_records = False
    for line in content.splitlines():
        heading = re.match(r'^(#{1,6} )(.+)$', line)
        prefix = re.match(r'^\*\*([^*]+):\*\*(.*)$', line)
        if heading and heading[2] == 'Record extract or verified school correction':
            in_source_records = False
        if in_source_records:
            lines.append(line)
            continue
        if heading:
            lines.append(heading[1] + t(heading[2]))
            if heading[2] == 'Relevant record extracts':
                in_source_records = True
        elif prefix:
            tail = prefix[2]
            if prefix[1] in {'Confirm existing record', 'Use supplied school record', 'Request missing records'}:
                tail = ' ' + t(tail.strip())
            lines.append('**' + t(prefix[1]) + ':**' + tail)
        else:
            lines.append(t(line))
    return '\n'.join(lines)
