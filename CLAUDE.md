# CLAUDE.md

Conventions for unattended (Lane B) work on `ai-app-factory-hello-world`.

Create a simple hello-world site to test the ai-app-factory build process

## Repo map

```
index.html                    Main script — the thing this project does
tests/                             Test suite for index.html
docs/journal.md                    Per-issue build metrics, appended by the workflow only — never edit by hand
.github/workflows/claude.yml       The Lane B driver
.github/scripts/journal-entry.sh   Metrics-append script the workflow calls
.env                               Local secrets — never commit, see .env.example
```

## Conventions

- **Never edit `docs/journal.md` by hand or from within a PR branch.** It's appended by `.github/workflows/claude.yml` *after* your PR merges, via `.github/scripts/journal-entry.sh`. Editing it in your branch means every open PR touches the same file and goes conflicting the moment any other PR merges.
- Keep commit and PR scope to the files named in the issue or in the repo map above.
- (none yet — add project-specific conventions here as they come up)

## Definition of done

- The issue's acceptance criteria are met.
- Tests pass: `pytest`.
- Any shell script added is `bash -n`-clean and executable (`chmod +x`).
- Any JSON added is valid (`jq . <file>` succeeds).
- PR description explains what you implemented, what you verified, and anything you could not verify unattended.
