#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

WORKFLOW_DIR = Path('.github/workflows')
USE_RE = re.compile(r'^\s*-?\s*uses:\s*([^\s#]+)')
SHA_REF_RE = re.compile(r'^[^@]+@[0-9a-fA-F]{40}$')


def main() -> int:
    violations: list[str] = []
    for path in sorted(WORKFLOW_DIR.glob('*.y*ml')):
        for line_no, line in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
            match = USE_RE.match(line)
            if not match:
                continue
            target = match.group(1)
            if target.startswith('./') or target.startswith('docker://'):
                continue
            if not SHA_REF_RE.fullmatch(target):
                violations.append(f'{path}:{line_no}: mutable or non-SHA action reference: {target}')

    if violations:
        print('GitHub Actions must be pinned to immutable 40-character commit SHAs.', file=sys.stderr)
        for violation in violations:
            print(violation, file=sys.stderr)
        return 1

    print('All external GitHub Actions references are pinned to immutable commit SHAs.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
