---
name: media-assets-skill
description: Locate, evaluate, download, and organize reusable media assets. Use when the user asks to find stock photos, videos, audio, icons, fonts, 3D models, or other creatives; compare sources or licenses; retrieve a specific asset; or organize downloaded media for a project.
---

# Media Assets

## Workflow

1. Clarify the brief only when it materially affects selection: medium, subject, style, quantity, technical constraints, and license requirements.
2. For each asset need, decide the execution path using the decision tree below.
3. If finding: choose sources with [references/sources.md](references/sources.md), verify with [references/evaluation.md](references/evaluation.md), and retrieve via the most reliable method.
4. If creating: follow [references/creation.md](references/creation.md) to generate assets using available tools.
5. If neither is feasible: produce a creative brief with [references/handoff-brief.md](references/handoff-brief.md) for the user to commission externally.
6. Organize all outputs with [scripts/organize_downloads.py](scripts/organize_downloads.py) and record provenance.

## Execution Decision Tree

For each asset need, evaluate in order:

1. **Can I generate it directly?** AI image generation (via imagegen), code-native SVG/canvas, or built-in document/spreadsheet tools. Choose this when the asset is a raster image, simple vector, texture, mockup, or diagram, and when the model can produce adequate quality for the brief.
2. **Can I find a suitable existing asset?** Use [references/sources.md](references/sources.md). Choose this when the asset is photography, live-action video, recorded audio, or a complex illustration where existing creators offer better quality than AI generation.
3. **Neither?** Produce a handoff brief. Choose this when the required asset needs a human specialist (custom video production, commissioned illustration, original music composition, brand-specific photography) or when no free/licensed source matches the brief.

When generating an image, load the imagegen skill. When generating a vector, diagram, or UI asset, prefer code-native output (SVG, HTML/CSS/canvas) over AI-generated bitmaps.

## Operating Rules

- Never misrepresent a license, attribution requirement, or source.
- Preserve source metadata when it is available or easy to obtain.
- Do not bypass paywalls, authentication, regional restrictions, or platform terms.
- Prefer lossless or highest-quality originals when bandwidth and storage allow.
- Store outputs in a project-owned directory unless the user specifies another location.

## Resources

- `references/sources.md`: source selection by medium, licensing, and access method.
- `references/evaluation.md`: technical and legal checks for accepted assets.
- `references/creation.md`: strategies and limitations for generating assets.
- `references/handoff-brief.md`: template for creative briefs when the skill cannot deliver directly.
- `scripts/organize_downloads.py`: normalize filenames and arrange assets by medium.
