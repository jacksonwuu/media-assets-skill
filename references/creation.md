# Asset Creation

## When to Generate vs. When to Find

Generate when:
- The asset is highly specific to the project (product mockup, concept art, custom texture, transparent-background sprite).
- No existing source matches the style or subject.
- The asset is a simple graphic better produced in code (icon, chart, diagram, wireframe).
- AI quality is sufficient for the intended size and usage.

Find instead when:
- The asset requires photorealism of a real subject (a specific landmark, a real person, an actual product).
- Live-action video or recorded audio is needed.
- An existing asset already matches the brief and saves time.
- Brand consistency requires a specific artist's style.

## Creation Methods

| Asset type | Preferred method | Tool/skill |
| --- | --- | --- |
| Photos, illustrations, textures, sprites | AI image generation | imagegen skill |
| Icons, logos, simple diagrams | Code-native SVG | Direct file output |
| Charts, data visualizations | Code-native (canvas/SVG/matplotlib) | visualize skill |
| UI mockups, wireframes | Code-native HTML/CSS | Direct output |
| Documents/slides | Built-in authoring tools | documents/presentations skills |
| Spreadsheets | Built-in authoring tools | spreadsheets skill |
| Video, music, voiceover | Out of scope for direct generation | See handoff-brief.md |

## Limitations to Disclose

- AI-generated images may have anatomical inconsistencies, text artifacts, or style drift across variants.
- AI-generated images carry no inherent license restriction (the user owns the output), but may resemble copyrighted works; disclose this uncertainty.
- Code-native assets are deterministic and editable but limited to geometric/typographic compositions.
- Video generation and music composition are not available through this skill; always hand off.
