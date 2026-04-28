#!/usr/bin/env python3
"""Call OpenAI with a prompt + diff, post result as a PR comment.

Used as a fallback when the Claude job fails (e.g. Anthropic outage,
expired token). Reads:
  OPENAI_API_KEY   - required
  OPENAI_MODEL     - optional, defaults to gpt-4o
  PR_NUMBER        - required (GitHub PR number)
  REPO             - required (owner/name)
  PROMPT_FILE      - required, path to the prompt markdown
  DIFF_FILE        - optional, path to a diff to append under "Diff:"
  COMMENT_HEADER   - optional, prepended to the comment body
"""
import json
import os
import subprocess
import sys
import urllib.request


def main() -> int:
    api_key = os.environ["OPENAI_API_KEY"]
    model = os.environ.get("OPENAI_MODEL", "gpt-4o")
    pr_number = os.environ["PR_NUMBER"]
    repo = os.environ["REPO"]
    prompt = open(os.environ["PROMPT_FILE"]).read()
    header = os.environ.get("COMMENT_HEADER", "## OpenAI fallback (Claude unavailable)")

    diff_file = os.environ.get("DIFF_FILE")
    if diff_file and os.path.exists(diff_file):
        prompt += "\n\n---\nDiff:\n```diff\n" + open(diff_file).read() + "\n```"

    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        }).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
    except urllib.error.HTTPError as e:
        print(f"OpenAI API error {e.code}: {e.read().decode()}", file=sys.stderr)
        return 1

    content = resp["choices"][0]["message"]["content"]
    body = f"{header}\n\n{content}"

    subprocess.run(
        ["gh", "pr", "comment", pr_number, "--repo", repo, "--body", body],
        check=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
