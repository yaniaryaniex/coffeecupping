# === Stage 11: Текстовый поиск ===
# Project: CoffeeCupping
import re
import difflib


def normalize(text):
    if text is None:
        return ""
    return text.lower().strip()


def build_regex_from_query(query, case_sensitive=False):
    if not query:
        return re.compile("")
    normalized_query = query.lower() if not case_sensitive else query
    escaped = re.escape(normalized_query)
    flags = 0 if case_sensitive else re.IGNORECASE
    return re.compile(escaped, flags)


def highlight_matches(text, query, case_sensitive=False):
    if not text or not query:
        return text or ""
    regex = build_regex_from_query(query, case_sensitive)
    if not regex:
        return text
    pattern = r"(.*?)(?:%s|.*?)(.*?)(?:%s)(.*?)" % (regex.pattern, regex.pattern)
    return re.sub(
        pattern,
        lambda m: "%s%s%s" % (m.group(1), m.group(2), _mark(m.group(3), regex)),
        text,
    )


def _mark(fragment, regex):
    if not fragment:
        return ""
    matches = list(re.finditer(regex, fragment))
    if not matches:
        return fragment
    result = ""
    cursor = 0
    for match in matches:
        start = match.start()
        end = match.end()
        result += fragment[cursor:start]
        result += "<mark>%s</mark>" % fragment[start:end]
        cursor = end
    result += fragment[cursor:]
    return result


class BatchSearcher:
    def __init__(self, batches, case_sensitive=False):
        self._batches = list(batches)
        self._case_sensitive = case_sensitive

    def matches(self, query):
        query = query or ""
        regex = build_regex_from_query(query, self._case_sensitive)
        for batch in self._batches:
            text = self._field_text(batch)
            if regex.search(text):
                yield batch, highlight_matches(text, query, self._case_sensitive)

    def all(self, query):
        query = query or ""
        regex = build_regex_from_query(query, self._case_sensitive)
        for batch in self._batches:
            text = self._field_text(batch)
            if regex.search(text):
                yield batch, highlight_matches(text, query, self._case_sensitive)

    def _field_text(self, batch):
        parts = []
        for field_name in ("name", "country", "roast", "date"):
            value = getattr(batch, field_name, None)
            if value:
                parts.append(str(value))
        return " ".join(parts)
