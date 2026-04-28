# starter-kit

Per-project scaffolding for new Claude-Code-driven projects. Pairs with [`dotfiles-claude`](https://github.com/shmangopods/dotfiles-claude) (user-level config).

This is a **GitHub template repo**. Click "Use this template" to create a new project pre-wired with:

- `.claude/` overrides (project-level CLAUDE.md, stricter settings)
- `.github/workflows/` for `@claude` bot, PR review, tests, security scan
- Issue and PR templates
- Branch protection defaults (applied via `SETUP.md` step)
- Architecture and decisions doc templates

Stack-agnostic. Works for web, mobile, CLI, data tools — fill in the stack per project in `.claude/CLAUDE.md`.

## Quickstart

1. **Use this template** → create new repo `shmangopods/<your-project>`
2. `gh repo clone shmangopods/<your-project> ~/code/<your-project> && cd ~/code/<your-project>`
3. Follow [`SETUP.md`](SETUP.md) (5 steps, ~10 minutes)
4. Open in Claude Code and start building

Or use the `/new-project` slash command from `dotfiles-claude` to do all of this in one shot.

## What's in the kit

```
starter-kit/
├── SETUP.md                       # One-time per-repo setup checklist
├── .claude/
│   ├── CLAUDE.md                  # Project-level prefs (placeholders to fill in)
│   └── settings.json              # Stricter project overrides
├── .github/
│   ├── workflows/                 # CI pipelines (filled in by Phase 5)
│   ├── ISSUE_TEMPLATE/
│   │   ├── feature.md
│   │   └── bug.md
│   └── pull_request_template.md
└── docs/
    ├── architecture.md            # System overview template
    └── decisions.md               # Append-only decisions log
```

## Per-project resources

When the project needs more than infrastructure, here are curated external resources to drop in selectively:

- **Design systems** → [VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) — 68 `DESIGN.md` files (Stripe, Linear, Figma, Notion style guides). Drop one into a UI-heavy project to scaffold the design system in one shot.
- **Earlier design.md collection** → [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — backup if `awesome-claude-design` is missing what you need.
- **Agent skills** → [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — 1000+ skills compatible with Claude Code, Codex, Gemini CLI, etc. Browse for capability extensions on a per-project basis.

These are not bundled into the kit — they're per-project decisions. Reach for them when the project's needs match.

## Updating the kit

When you find improvements while working on real projects:

- **User-level improvement** (applies to all projects) → goes in `dotfiles-claude`, not here.
- **Project-template improvement** (every new project should benefit) → PR into this repo. Future "Use this template" clones inherit it. Existing projects don't auto-update.

## Companion repo

[`dotfiles-claude`](https://github.com/shmangopods/dotfiles-claude) — user-level Claude Code infrastructure (subagents, hooks, slash commands).
