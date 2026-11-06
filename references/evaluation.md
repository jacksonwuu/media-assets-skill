# Asset Evaluation

## Acceptance Checklist

### Rights and provenance

- Confirm the creator or upstream source, source URL, and retrieval date.
- Confirm license name/version and permitted uses: commercial use, modification, redistribution, training, and territory if stated.
- Confirm whether attribution, a license link, a change notice, or a share-alike obligation applies.
- Avoid assets with incomplete provenance unless the user explicitly accepts the risk.

### Technical quality

**Images:** resolution, aspect ratio, color profile, compression artifacts, transparency, noise, focus, composition, and cropping headroom.

**Video:** resolution, frame rate, duration, codec, bitrate, color profile, audio presence, scene cuts, camera motion, and deliverable constraints.

**Audio:** sample rate, bit depth, channels, loudness, trimming headroom, loopability, transient quality, and music mix suitability.

**Vector/icon/font/3D:** source-file format, layer/component organization, licensing of embedded assets, compatibility, and unit/scale where relevant.

### Fit to brief

- Subject, framing, perspective, color, lighting, era, and visual style.
- Cultural and contextual appropriateness.
- Technical fit with the intended layout, video pipeline, or design system.

## Documentation Pattern

For assets needing provenance, create or append `assets-manifest.md` beside the files:

```markdown
| File | Medium | Source | Source URL | License | Attribution required | Retrieved | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hero.jpg | image | Unsplash | https://... | Unsplash License | no | 2026-11-06 | 4000x2667, landscape |
```
