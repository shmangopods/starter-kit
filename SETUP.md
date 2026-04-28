# Setup (one-time, per new repo)

After creating a new repo from this template, run through this checklist before starting work.

## 1. Add the Anthropic API key

```bash
gh secret set ANTHROPIC_API_KEY --repo shmangopods/<this-repo>
```

(Paste the key when prompted. Get it from https://console.anthropic.com → API Keys.)

## 2. Install the Claude GitHub App

In a Claude Code session in this repo, run:

```
/install-github-app
```

This connects the @claude bot to this repo so it can open PRs and post review comments.

## 3. Apply branch protection to `main`

```bash
gh api repos/shmangopods/<this-repo>/branches/main/protection \
  --method PUT \
  --input - <<'JSON'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["tests", "claude-pr-review", "security-scan"]
  },
  "enforce_admins": false,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_conversation_resolution": true
}
JSON
```

Note: The branch must have at least one commit before protection can be applied. Push an initial commit first if needed.

## 4. Fill in project-level CLAUDE.md

Open `.claude/CLAUDE.md` and replace every `<PLACEHOLDER>`. Required:
- Project name + one-line description
- Stack (language, framework, DB, deploy target)
- Commands (install / dev / test / lint / format / build)

## 5. Verify everything works

1. Open Claude Code in this repo. Check `/status` shows the project-level config loaded.
2. File a small test issue. Comment `@claude` on it. Watch:
   - A PR opens with the change
   - The 3 reviewer subagents post inline comments
   - The tests workflow runs
   - The security scan runs
3. Try to push directly to `main` from CLI — branch protection should reject.

If any step fails, fix it before starting real work. Update `docs/decisions.md` if you had to deviate from the standard setup.
