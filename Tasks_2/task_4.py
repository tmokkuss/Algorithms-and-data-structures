import sys


def format_comment(line_number, comment):
    return f"Line {line_number}: {comment.strip()}"


def process_comments(lines):
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("#"):
            comment = line.strip("#").strip()
            yield format_comment(i, comment)


lines = [
    "import sys",
    "for line in sys.stdin:",
    "    # rstrip(’\n’) 'отрезает' от строки line,",
    "    # идущий справа символ перевода строки,",
    "    # ведь print сам переводит строку"
]

comments = process_comments(lines)
for comment in comments:
    print(comment)
