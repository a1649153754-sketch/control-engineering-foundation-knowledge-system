# AGENTS.md

## Scope

This file applies to the entire repository. More specific `AGENTS.md` files may override it only within their own subtrees.

## Project purpose

Maintain a versioned, machine-checkable control-engineering knowledge system that connects textbook structure, formula conditions, worked exercises, Tsinghua 822 exam metadata and analyses, recurring problem families, experiments, and review data.

## Read before editing

1. `README.md`
2. `ROADMAP.md`
3. `CONTRIBUTING.md`
4. `docs/21-project-maintenance.md`
5. `docs/22-source-map.md`
6. `docs/CODEX_HANDOFF.md`

## Non-negotiable contracts

- Preserve stable `C / K / Q / EX / TH / KP / B / J` identities. Do not silently renumber released nodes, cards, exercises, exam units, or source cards.
- Clearly separate source-derived facts, independent derivation, model inference, and unresolved uncertainty.
- For figure-dependent or unclear scans, use evidence states such as `verified`, `route-only`, or `ambiguous-scan`; never guess unreadable parameters.
- Do not commit source PDFs, scans, full exam sheets, complete copied question text, or long third-party solution passages. Publish copyright-safe summaries, locators, original derivations, short checkable results, and original diagrams.
- Use renderable LaTeX for formulas. Every important result should state assumptions, units or normalization, failure boundary, and at least one verification route.
- A controller-design answer is incomplete until stability, steady-state error, time response, frequency response, control effort, and implementation limits have been checked as applicable.
- Generated catalogs and bundles must be rebuilt from canonical sources rather than hand-edited.

## Required checks

Run from the repository root:

```bash
python scripts/validate_project.py
python scripts/build_bundle.py
zensical build --clean
git diff --check
```

For numerical-verification work, also run the relevant Python/MATLAB scripts and preserve reproducible inputs, tolerances, and outputs.

## Editing workflow

1. Inspect current `VERSION`, branch, `git status --short --branch`, and remote divergence.
2. Work on a dedicated branch; keep one reviewable milestone per branch.
3. Edit canonical Markdown/data first, then rebuild catalogs and bundles.
4. When changing a result, trace it back to its source locator and state whether the new value is source-derived or independently recomputed.
5. Add validation for new ID types, evidence states, generated diagrams, or machine-readable fields.
6. Review the final diff for leaked PDFs, copied source text, unsupported numerical certainty, broken links, ID drift, and generated-file noise.
7. Update release metadata only when the milestone is ready to ship.

## Current direction

A local v1.2.0 candidate may be present in the multi-repository Codex workspace while the remote repository still reports v1.1.0. Do not reset or discard that candidate. Audit, validate, sample-review, and commit it on a dedicated branch before moving to v1.3 numerical verification and original diagrams.

## Definition of done

A change is complete only when validation and the documentation build pass, source and inference boundaries are explicit, numerical claims are reproducible, copyright boundaries remain intact, and the final report lists modified files, checks run, unresolved evidence gaps, and the next recommended step.
