# Skill Evals

Run each test case manually in a fresh conversation, or use `scripts/run_evals.py` to orchestrate multiple cases.

## Directory Structure

```
evals/
├── README.md          # This file
├── cases/             # Test case definitions
│   ├── trigger-positive/    # Should trigger the skill
│   ├── trigger-negative/    # Should NOT trigger the skill
│   └── quality/             # Full-workflow quality checks
└── results/           # Recorded outputs and scores (gitignored)
```

## Case Format

Each case is a YAML file with:

```yaml
name: descriptive-case-name
type: trigger-positive | trigger-negative | quality
prompt: "The exact user message to send"
expectations:
  skill_triggered: true|false        # For trigger cases
  criteria:                           # For quality cases
    - id: license-verified
      description: "License is stated before any download link"
      required: true
    - id: source-attributed
      description: "Source URL and license name are both present"
      required: true
```

## Scoring

- **Trigger cases**: pass/fail — did the skill fire (or not fire)?
- **Quality cases**: score 0–1 per criterion; pass if all required criteria score ≥ 0.5.

Record results in `results/<date>/<case-name>.json`.
