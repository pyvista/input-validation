"""Drop the lines coverage excludes from mypy's Cobertura typing report."""

from __future__ import annotations

from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

import tomllib


def excluded_lines(source: str, patterns: list[re.Pattern[str]]) -> set[int]:
    """Return the line numbers the patterns match, with the blocks that matched lines open."""
    lines = source.split('\n')
    excluded: set[int] = set()
    for pattern in patterns:
        for match in pattern.finditer(source):
            first = source.count('\n', 0, match.start()) + 1
            last = source.count('\n', 0, match.end()) + 1
            excluded.update(range(first, last + 1))
            opener = lines[last - 1]
            if opener.rstrip().endswith(':'):
                indent = len(opener) - len(opener.lstrip())
                for number in range(last + 1, len(lines) + 1):
                    line = lines[number - 1]
                    if line.strip() and len(line) - len(line.lstrip()) <= indent:
                        break
                    excluded.add(number)
    return excluded


def main(report: Path) -> None:
    """Rewrite ``report`` without the lines ``[tool.coverage.report]`` excludes."""
    config = tomllib.loads(Path('pyproject.toml').read_text())
    patterns = [
        re.compile(p, re.MULTILINE) for p in config['tool']['coverage']['report']['exclude_also']
    ]
    tree = ET.parse(report)
    for cls in tree.iter('class'):
        excluded = excluded_lines(Path(cls.get('filename', '')).read_text(), patterns)
        lines = cls.find('lines')
        if lines is None:
            continue
        for line in list(lines):
            if int(line.get('number', '0')) in excluded:
                lines.remove(line)
    tree.write(report)


if __name__ == '__main__':
    main(Path(sys.argv[1]))
