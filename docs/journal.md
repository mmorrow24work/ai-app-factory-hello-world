# Build Journal

Per-issue record of the unattended (Lane B) build of this project. One entry per Claude run, appended automatically by `.github/workflows/claude.yml` via `.github/scripts/journal-entry.sh`.

## How this file is written

**Entries are appended by the workflow, not by Claude inside its PR.** This is deliberate: having Claude append a journal entry within each PR means every open PR touches the same file, so almost every one goes `CONFLICTING` the moment any other PR merges — leaving green, auto-merge-enabled PRs sitting unmerged indefinitely. Patching from the workflow after the run sidesteps that entirely: Claude's branches never touch `docs/journal.md`.

## What "Estimated Cost" means

This pipeline authenticates via a **Claude subscription** (OAuth), not pay-per-token API billing. The cost figure is notional — what the run *would* cost at standard list rates — useful as a consistent yardstick for comparing runs, not an actual charge.

---

## Build velocity

Recomputed by `.github/scripts/journal-entry.sh` on every run.

<!-- VELOCITY_START -->
| Metric | Value |
|---|---|
| Issues with recorded metrics | 3 |
| Successful runs | 2 |
| Mean time per issue | 1m 55s |
| Mean turns per issue | 34 |
| Mean output tokens per issue | 9,048 |
| Mean estimated cost per issue | $0.1360 |
<!-- VELOCITY_END -->

---

## Entries

<!-- ENTRIES_START -->
<!-- New entries are appended below this marker, newest last. -->

## 2026-08-17 — Issue #1: Add index.html and style.css

- **Result:** failure
- **PR:** —
- **Milestone:** M1: The page
- **Model:** claude-sonnet-5
- **Execution Duration:** 4 seconds
- **Turns:** 0
- **Input Tokens:** 0
- **Output Tokens:** 0
- **Estimated Cost:** $0.0000 (notional — see above)
- **Run:** https://github.com/mmorrow24work/ai-app-factory-hello-world/actions/runs/32068729438

## 2026-08-17 — Issue #1: Add index.html and style.css

- **Result:** success
- **PR:** #4
- **Milestone:** M1: The page
- **Model:** claude-sonnet-5
- **Execution Duration:** 104 seconds
- **Turns:** 47
- **Input Tokens:** 154
- **Output Tokens:** 6530
- **Estimated Cost:** $0.0984 (notional — see above)
- **Run:** https://github.com/mmorrow24work/ai-app-factory-hello-world/actions/runs/32071875494

## 2026-08-17 — Issue #2: Add the pytest suite for the site's HTML

- **Result:** success
- **PR:** #5
- **Milestone:** M2: Tests
- **Model:** claude-sonnet-5
- **Execution Duration:** 238 seconds
- **Turns:** 56
- **Input Tokens:** 178
- **Output Tokens:** 20614
- **Estimated Cost:** $0.3097 (notional — see above)
- **Run:** https://github.com/mmorrow24work/ai-app-factory-hello-world/actions/runs/32073085210
