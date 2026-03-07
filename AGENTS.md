# AGENTS.md

You are working in this repository as a coding agent.

Primary objective:
Implement the requested feature safely and produce a reviewable result.

Hard constraints:
- Only modify files inside this repository.
- Do not touch OS settings, shell profiles, user home, browser data, cloud-sync folders, or SSH keys.
- Do not add global dependencies.
- Prefer minimal, reversible diffs.
- Preserve existing architecture unless change is necessary.
- If requirements are ambiguous, choose the smallest correct implementation and document assumptions.

Required workflow:
1. Read README and project structure first.
2. Make a short plan before large edits.
3. Implement in small coherent commits.
4. Run tests, lint, and build if available.
5. Update docs for any user-visible change.
6. Summarize what changed, risks, and follow-up work.

Coding standards:
- Follow existing style and naming.
- Add tests for new logic.
- Avoid unnecessary refactors.
- Do not silently delete files unless clearly obsolete and replaced.

Output expectations:
- Final summary must include:
  - changed files
  - commands run
  - test results
  - unresolved issues
  - suggested next steps
