# Decisions Log

Project-specific decisions log. Append-only — never edit existing entries.

Format:
```
## YYYY-MM-DD: Title
**Decision:** What we chose
**Alternatives considered:** Other options
**Reasoning:** Why this one
**Revisit if:** Conditions that would make us reconsider
```

When to add an entry:
- A non-obvious technical or product call you'd otherwise have to re-explain in 6 months
- A choice that locked the project into a path (database, framework, auth model)
- A "don't do X" rule with a reason

When NOT to add an entry:
- Routine implementation choices that the code itself documents
- Reversals of recent decisions — instead, write a new entry that supersedes the old one

---

## YYYY-MM-DD: Initial setup

**Decision:** Bootstrapped from `shmangopods/starter-kit` template.
**Alternatives considered:** N/A
**Reasoning:** Inherited the standard kit (Claude Code config, GitHub Actions for review, branch protection).
**Revisit if:** Project needs diverge significantly from the kit's defaults.
