"""校验 agent/*.md 的 frontmatter 完整性。"""

import re
from pathlib import Path

import pytest

AGENT_DIR = Path(__file__).resolve().parent.parent / "agent"
REQUIRED_FIELDS = ("name", "model", "description")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

agent_files = sorted(AGENT_DIR.glob("*.md"))


@pytest.mark.parametrize("path", agent_files, ids=lambda p: p.name)
def test_agent_file_not_empty(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    assert content.strip(), f"{path.name} 是空文件，需要补充 frontmatter 与角色说明正文"


@pytest.mark.parametrize("path", agent_files, ids=lambda p: p.name)
def test_agent_has_required_frontmatter(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    assert match, f"{path.name} 缺少 --- frontmatter --- 头"
    frontmatter = match.group(1)
    for field in REQUIRED_FIELDS:
        assert re.search(rf"^{field}:\s*\S", frontmatter, re.MULTILINE), (
            f"{path.name} frontmatter 缺少必填字段 {field}"
        )


@pytest.mark.parametrize("path", agent_files, ids=lambda p: p.name)
def test_agent_has_body_after_frontmatter(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    assert match, f"{path.name} 缺少 frontmatter，无法校验正文"
    body = content[match.end():]
    assert body.strip(), f"{path.name} frontmatter 之后没有角色说明正文"
