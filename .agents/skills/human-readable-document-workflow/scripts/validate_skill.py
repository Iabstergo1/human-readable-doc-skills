#!/usr/bin/env python3
"""Validate the human-readable-document-workflow skill package."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


REQUIRED_REFERENCES = [
    "references/00-routing-policy.md",
    "references/01-writing-loop.md",
    "references/02-human-readable-style.md",
    "references/03-anti-ai-slop-zh.md",
    "references/04-anti-ai-slop-en.md",
    "references/05-academic-writing.md",
    "references/06-document-layout.md",
    "references/07-markdown-authoring.md",
    "references/10-quality-gates.md",
    "references/11-upstream-attribution.md",
    "references/12-document-type-profiles.md",
    "references/13-style-distillation.md",
]

REQUIRED_SCRIPTS = [
    "scripts/detect_doc_intent.py",
    "scripts/lint_ai_style.py",
    "scripts/normalize_markdown.py",
    "scripts/validate_markdown_source.py",
    "scripts/validate_skill.py",
]

REQUIRED_README_SECTIONS = [
    "## Core capability",
    "## Out of scope",
    "## Handoff policy",
]

SKILL_FORBIDDEN_TERMS = [
    "render_with_pandoc.py",
    "Pandoc",
    "Quarto",
    "Typst",
    "reference.docx",
]

REQUIRED_DESCRIPTION = (
    "Trigger when the user asks to create, draft, revise, polish, structure, "
    "export, typeset, or generate a document, report, article, paper, proposal, "
    "README, Markdown file, Word document, PDF, academic writing, technical "
    "documentation, business document, meeting notes, or other long-form written "
    "artifact. Do not trigger for short casual answers unless the user explicitly "
    "asks for a reusable document."
)

UPSTREAM_URLS = [
    "https://github.com/xxsang/writers-loop",
    "https://github.com/xxsang/writers-loop/tree/main/skills/writers-loop",
    "https://github.com/lulucatdev/codex-be-serious",
    "https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious",
    "https://github.com/lulucatdev/codex-be-serious/tree/main/skills/be-serious-review",
    "https://github.com/MohamedAbdallah-14/unslop",
    "https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop",
    "https://github.com/MohamedAbdallah-14/unslop/tree/main/skills/unslop-review",
    "https://github.com/adenaufal/anti-slop-writing",
    "https://github.com/adenaufal/anti-slop-writing/tree/main/english",
    "https://github.com/adenaufal/anti-slop-writing/blob/main/english/SKILL.md",
    "https://github.com/LifelongLazyLearner/qu-ai-wei",
    "https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md",
    "https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/references",
    "https://github.com/LifelongLazyLearner/qu-ai-wei/tree/main/scripts",
    "https://github.com/op7418/humanizer-zh",
    "https://github.com/op7418/humanizer-zh/blob/main/SKILL.md",
    "https://github.com/shyuan/writing-humanizer",
    "https://github.com/shyuan/writing-humanizer/tree/main/skills/writing-humanizer",
    "https://github.com/f/prompts.chat",
    "https://github.com/ahmetbersoz/chatgpt-prompts-for-academic-writing",
]


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def parse_frontmatter(skill_path: Path) -> dict[str, object]:
    text = skill_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    result: dict[str, object] = {
        "ok": False,
        "has_opening": bool(lines and lines[0] == "---"),
        "has_closing": False,
        "name": None,
        "description": None,
        "errors": [],
    }
    errors: list[str] = result["errors"]  # type: ignore[assignment]
    if not result["has_opening"]:
        errors.append("frontmatter-first-line-must-be-exactly-dashes")
        return result
    closing = None
    for index, line in enumerate(lines[1:], start=2):
        if line == "---":
            closing = index
            break
        if line.strip() == "---" and line != "---":
            errors.append(f"frontmatter-closing-not-standalone:{index}")
    if closing is None:
        errors.append("frontmatter-missing-closing")
        return result
    result["has_closing"] = True
    frontmatter_lines = lines[1 : closing - 1]
    data: dict[str, str] = {}
    scalar_key: str | None = None
    scalar_lines: list[str] = []

    for line in frontmatter_lines:
        if scalar_key is not None and (line.startswith(" ") or line == ""):
            scalar_lines.append(line.strip())
            continue
        if scalar_key is not None:
            data[scalar_key] = " ".join(part for part in scalar_lines if part)
            scalar_key = None
            scalar_lines = []
        if ":" not in line or line.startswith(" "):
            errors.append(f"frontmatter-invalid-line:{line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key == "description" and value in {">", ">-"}:
            scalar_key = key
            scalar_lines = []
        else:
            data[key] = value

    if scalar_key is not None:
        data[scalar_key] = " ".join(part for part in scalar_lines if part)

    result["name"] = data.get("name")
    result["description"] = data.get("description")
    if result["name"] != "human-readable-document-workflow":
        errors.append("frontmatter-name-invalid")
    if result["description"] != REQUIRED_DESCRIPTION:
        errors.append("frontmatter-description-invalid")
    allowed_keys = {"name", "description"}
    extra_keys = sorted(set(data) - allowed_keys)
    if extra_keys:
        errors.append(f"frontmatter-extra-keys:{','.join(extra_keys)}")
    if not result["description"]:
        errors.append("frontmatter-description-missing")
    result["ok"] = not errors
    return result


def references_from_skill(skill_path: Path) -> list[str]:
    text = skill_path.read_text(encoding="utf-8")
    refs = re.findall(r"references/[A-Za-z0-9_.\-/]+\.md", text)
    return sorted(set(refs))


def check_script_help(script: Path) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(script), "--help"],
        text=True,
        capture_output=True,
        check=False,
        timeout=10,
    )
    return {
        "script": script.name,
        "returncode": completed.returncode,
        "ok": completed.returncode == 0 and "usage:" in completed.stdout.lower(),
    }


def py_compile_script(script: Path) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="hrdw-pycache-") as pycache_dir:
        env = os.environ.copy()
        env["PYTHONPYCACHEPREFIX"] = pycache_dir
        completed = subprocess.run(
            [sys.executable, "-m", "py_compile", str(script)],
            text=True,
            capture_output=True,
            check=False,
            timeout=15,
            env=env,
        )
    return {
        "script": script.name,
        "returncode": completed.returncode,
        "ok": completed.returncode == 0,
        "stderr": completed.stderr.strip(),
    }


def python_line_issues(skill_dir: Path) -> dict[str, object]:
    warnings: list[dict[str, object]] = []
    errors: list[dict[str, object]] = []
    for path in (skill_dir / "scripts").glob("*.py"):
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(path.read_text(encoding="utf-8")) > 500 and len(lines) < 10:
            errors.append(
                {
                    "path": rel(path, skill_dir),
                    "line": None,
                    "issue": "compressed-python",
                    "line_count": len(lines),
                }
            )
        for line_no, line in enumerate(lines, start=1):
            if len(line) > 400:
                errors.append(
                    {
                        "path": rel(path, skill_dir),
                        "line": line_no,
                        "issue": "python-line-too-long",
                        "length": len(line),
                    }
                )
            elif len(line) > 240:
                warnings.append(
                    {
                        "path": rel(path, skill_dir),
                        "line": line_no,
                        "issue": "python-line-long",
                        "length": len(line),
                    }
                )
    return {"ok": not errors, "warnings": warnings, "errors": errors}


def markdown_issues(repo_root: Path, max_line_length: int) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    for path in repo_root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        stripped = text.strip()
        if not stripped:
            issues.append({"path": rel(path, repo_root), "line": None, "issue": "empty-markdown"})
            continue
        if re.fullmatch(r"(TODO|TBD|PLACEHOLDER|待补充|FIXME)[\s#\-:。.]*", stripped, flags=re.I):
            issues.append({"path": rel(path, repo_root), "line": None, "issue": "placeholder-only"})
        lines = text.splitlines()
        critical = (
            path.name in {"README.md", "SKILL.md", "AGENTS.md"}
            or "references" in path.parts
            or "assets" in path.parts
            or "tests" in path.parts
        )
        if critical and len(text) > 500 and len(lines) < 8:
            issues.append(
                {
                    "path": rel(path, repo_root),
                    "line": None,
                    "issue": "compressed-markdown",
                    "line_count": len(lines),
                }
            )
        for line_no, line in enumerate(lines, start=1):
            if len(line) > max_line_length and not re.search(r"https?://", line):
                issues.append(
                    {
                        "path": rel(path, repo_root),
                        "line": line_no,
                        "issue": "long-line",
                        "length": len(line),
                    }
                )
    return issues


def readme_attribution(readme_path: Path) -> dict[str, object]:
    text = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    missing = [url for url in UPSTREAM_URLS if url not in text]
    return {"ok": not missing, "missing_urls": missing}


def readme_scope(readme_path: Path) -> dict[str, object]:
    text = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    missing = [section for section in REQUIRED_README_SECTIONS if section not in text]
    return {"ok": not missing, "missing_sections": missing}


def skill_scope(skill_path: Path) -> dict[str, object]:
    text = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
    forbidden = [term for term in SKILL_FORBIDDEN_TERMS if term in text]
    lowered = text.lower()
    has_handoff = "handoff" in lowered or "official document-generation skill" in lowered
    return {
        "ok": not forbidden and has_handoff,
        "forbidden_terms": forbidden,
        "has_handoff_boundary": has_handoff,
    }


def validate(repo_root: Path, max_line_length: int) -> dict[str, object]:
    skill_dir = repo_root / ".agents" / "skills" / "human-readable-document-workflow"
    skill_path = skill_dir / "SKILL.md"
    refs = references_from_skill(skill_path)
    missing_required_refs = [ref for ref in REQUIRED_REFERENCES if not (skill_dir / ref).exists()]
    missing_linked_refs = [ref for ref in refs if not (skill_dir / ref).exists()]
    missing_scripts = [script for script in REQUIRED_SCRIPTS if not (skill_dir / script).exists()]
    script_paths = [skill_dir / script for script in REQUIRED_SCRIPTS if (skill_dir / script).exists()]
    script_help = [check_script_help(script) for script in script_paths]
    script_compile = [py_compile_script(script) for script in script_paths]
    md_issues = markdown_issues(repo_root, max_line_length)
    py_line_issues = python_line_issues(skill_dir)
    readme_path = repo_root / "README.md"
    attribution = readme_attribution(readme_path)
    readme_scope_check = readme_scope(readme_path)

    checks = {
        "frontmatter": parse_frontmatter(skill_path),
        "skill_scope": skill_scope(skill_path),
        "required_references": {
            "ok": not missing_required_refs,
            "missing": missing_required_refs,
        },
        "linked_references": {
            "ok": not missing_linked_refs,
            "linked": refs,
            "missing": missing_linked_refs,
        },
        "required_scripts": {
            "ok": not missing_scripts,
            "missing": missing_scripts,
        },
        "script_help": {
            "ok": all(item["ok"] for item in script_help),
            "items": script_help,
        },
        "python_compile": {
            "ok": all(item["ok"] for item in script_compile),
            "items": script_compile,
        },
        "python_line_lengths": py_line_issues,
        "markdown_readability": {
            "ok": not md_issues,
            "issues": md_issues,
        },
        "readme_scope": readme_scope_check,
        "readme_upstream_attribution": attribution,
    }
    ok = all(check["ok"] for check in checks.values())  # type: ignore[index]
    return {"ok": ok, "checks": checks}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the human-readable-document-workflow skill package.")
    parser.add_argument("--repo-root", type=Path, default=None, help="Repository root. Defaults to script-relative root.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    parser.add_argument("--max-line-length", type=int, default=220, help="Maximum non-URL Markdown line length.")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    default_root = script_path.parents[4]
    repo_root = (args.repo_root or default_root).resolve()
    result = validate(repo_root, args.max_line_length)
    print(json.dumps(result, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
