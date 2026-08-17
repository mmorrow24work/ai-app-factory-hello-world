# ai-app-factory-hello-world

Create a simple hello-world site to test the ai-app-factory build process Built and evolved via the unattended (Lane B) Claude Code pipeline: label an issue `claude-go` and `.github/workflows/claude.yml` implements it, opens a PR, and records the run in `docs/journal.md`.

This is a **factory smoke test, not a maintained project** — it exists to
exercise the ai-app-factory pipeline end to end, not to be a real
application. See `about.html` (or [`/about.html`](https://mmorrow24work.github.io/ai-app-factory-hello-world/about.html) live) for how it was built.

## Live site

https://mmorrow24work.github.io/ai-app-factory-hello-world/

## Viewing locally

Serve the repo root over HTTP rather than opening the HTML files directly,
since production (GitHub Pages) is what exercises the relative paths
between pages and `style.css`:

```sh
python3 -m http.server
```

Then visit `http://localhost:8000/`.

## Support & Handoff

### Support

Open an issue, or comment on an existing one:

- Apply the `claude-go` label (or comment `@claude`) to have the unattended pipeline attempt a fix.
- Mention `@mmorrow24work` for anything the pipeline can't or shouldn't handle unattended — design decisions, ambiguous requirements, anything labeled `lane:manual`.

### Handoff

Once this project's milestones are complete, fork the repo to take ownership.

GitHub forks do **not** inherit the parent repo's Actions secrets, so `claude-go` stops working on the fork the instant it's created — no separate revoke step needed on the original owner's side. To keep the unattended pipeline running, the new owner sets up their own `CLAUDE_CODE_OAUTH_TOKEN`/`GH_PAT` secrets on their fork (same `claude setup-token` / `gh secret set` steps documented in the `ai-app-factory` repo's own `README.md`).
