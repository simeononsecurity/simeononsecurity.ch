# AI collaboration lab

Run with Python 3.10 or later. No external packages or network access.

```bash
python3 -m unittest discover -s . -v
cp -R baseline candidate
python3 check.py capture --base baseline > candidate/context.json
python3 check.py validate --base baseline --candidate candidate
```

Keep baseline unchanged during an exercise. Modify candidate for the seven-to-thirty-day proposal.
Change requirement.json, config.json, proposal.json and the first runbook.md line together.
Increment the requirement revision to 2. Keep proposal base_revision at 1.

The checker tests consistency and captured source bytes. It does not verify identity, approvals,
vendor permissions, or real export deletion. Run the live sandbox denial tests in the course.
For CI, supply a separately checked-out protected base, not baseline from the proposal branch.