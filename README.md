# mdfence

Tiny pure-stdlib linter for fenced code blocks in Markdown. Part of [mdtools](https://github.com/maxotto-agent/mdtools).

```sh
mdfence README.md docs/*.md            # reports unclosed fences
mdfence --require-lang README.md       # also flags fences with no language tag
```

Handles ``` and ~~~ fences, longer outer fences (nesting), and exits 1 on problems.
Also usable as a pre-commit hook (`id: mdfence`).

MIT licensed. Written by an AI agent (Claude).
