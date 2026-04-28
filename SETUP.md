# Setup (one-time, per new repo)

After creating a new repo from this template, run through this checklist before starting work.

## 0. (First-time GitHub account only) Clear default $0 budgets

GitHub creates new accounts with several **$0 budgets that have "Stop usage: Yes"** on Actions, Codespaces, Packages, Git LFS, and Premium SKUs. These block all workflow runs — even free-tier minutes — until removed.

Go to https://github.com/settings/billing/budgets_and_alerts and delete every default $0 budget (the page should read "No budgets created"). Your overage **spending limit** (separate setting) stays at $0, so you still cannot be billed beyond your plan's free allowance.

You only need to do this once per account. Skip if your Budgets page is already empty.

> Heads up: brand-new GitHub accounts also have a silent Actions hold that can delay first workflow runs by several hours. If runs sit queued after budgets are clear, just wait.

## 1. Add the Anthropic API key

```bash
gh secret set ANTHROPIC_API_KEY --repo shmangopods/<this-repo>
```

(Paste the key when prompted. Get it from https://console.anthropic.com → API Keys.)

## 2. Install the Claude GitHub App

Open https://github.com/apps/claude/installations/new in a browser → pick your account → choose "Only select repositories" → select this repo → Install.

(The `/install-github-app` slash command in Claude Code opens this same flow if you'd rather start from there.)

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
