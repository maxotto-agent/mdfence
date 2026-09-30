import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from mdfence import lint, main


def test_clean():
    assert lint("```py\nx\n```\n") == []


def test_unclosed():
    assert lint("a\n```py\nx\n") == [(2, "unclosed code fence")]


def test_nested_longer_fence():
    assert lint("````md\n```py\nx\n```\n````\n") == []


def test_tilde_inside_backtick_ignored():
    assert lint("```\n~~~\n```\n") == []


def test_require_lang():
    assert lint("```\nx\n```\n", True) == [(1, "code fence has no language")]


def test_closing_fence_not_flagged_for_lang():
    assert lint("```py\nx\n```\n", True) == []


def test_cli(tmp_path):
    p = tmp_path / "a.md"
    p.write_text("```\nx\n")
    assert main([str(p)]) == 1
