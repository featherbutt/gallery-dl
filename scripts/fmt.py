#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2026 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

import re
import sys
import subprocess

w = sys.stdout.write
ROOT = "https://codeberg.org"
REPO = "mikf/gallery-dl"
RE_ISSUE = r"(?:gh|cb|)#\d+"
RE_COMMIT = (
    fr"\s*"
    fr"(?:merge ({RE_ISSUE}):\s+)?"
    fr"((?:\[[^\]]+\]\s+)?.+?)"
    fr"(?:\s*\(([^\)]+)\))?\s*$"
)


def git(command, *args):
    return subprocess.Popen(
        ["git", command, *args],
        stdout=subprocess.PIPE,
    ).communicate()[0].strip().decode()


def fmt_issues(issues, pr=None):
    results = []
    if issues:
        results.extend(fmt_issue(i) for i in issues.strip().split())
    if pr:
        results.append(fmt_issue(pr, "pr"))
    return results


def fmt_issue(issue, pr=False):
    src, _, num = issue.rpartition("#")
    if not src:
        src, domain = \
            ("gh", "github.com") if int(num) > 128 else ("cb", "codeberg.org")
    elif src == "gh":
        domain = "github.com"
    else:
        src = "cb"
        domain = "codeberg.org"
    if pr:
        return (f"[`pr#{num}`](https://{domain}/{REPO}/"
                f"{'pull' if src == 'gh' else 'pulls'}/{num})")
    return f"[`{src}#{num}`](https://{domain}/{REPO}/issues/{num})"


def fmt_subject(subject):
    subject = re.sub(
        r"""\s+""", r" ", subject.strip())
    subject = re.sub(
        r"""\s+"(.+?)"(\s+)""", replace_quoted, subject)
    subject = re.sub(
        r"""\s+"(.+?)"$()""", replace_quoted, subject)
    subject = re.sub(
        r"""'([^']+)'""", r"`\1`", subject)
    return subject.replace("<SINGLEQUOTE>", "'")


def fmt_commit(pr, subject, issues, suffix=""):
    subject = fmt_subject(subject) + suffix
    if pr:
        subject = f"merge {fmt_issue(pr, True)}: {subject}"
    if issues:
        subject = f"{subject} ({' '.join(fmt_issues(issues))})"
    return subject


def replace_quoted(match):
    quoted = match[1].replace("'", "<SINGLEQUOTE>")
    return f" `{quoted}`{' ' if match[2] else ''}"


def process_issue(num):
    w(fmt_issue(num) + "\n")
    return 0


def process_commit(pr, subject, issues):
    w(fmt_commit(pr, subject, issues) + "\n")
    return 0


def process_ref(ref):
    HASH, sep, subject = git(
        "log", "-1", "--format=%H|%s", ref).partition("|")
    if not sep:
        return 1
    m = re.match(RE_COMMIT, subject)
    s = f"]({ROOT}/{REPO}/commit/{HASH})"
    w(f"[`{HASH[:8]}` {fmt_commit(*m.groups(), s)}\n")
    return 0


def main():
    try:
        arg = sys.argv[1]
    except Exception:
        return process_ref("HEAD")

    if m := re.match(RE_ISSUE, arg):
        return process_issue(arg)

    if len(arg) < 8 and arg.isdecimal():
        return process_issue(arg)

    if m := re.match(fr"{ROOT}/{REPO}/commit/([0-9a-f]{{8,}})", arg):
        return process_ref(m[1])

    if m := re.match(RE_COMMIT, arg):
        pr, subject, issues = m.groups()
        if not (pr is None and issues is None and " " not in subject):
            return process_commit(pr, subject, issues)

    return process_ref(arg)


if __name__ == "__main__":
    main()
