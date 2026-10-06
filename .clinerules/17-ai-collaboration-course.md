# AI Collaboration Implementation Course

The non-certification course hub lives at `content/ai-collaboration-course-start/index.en.md`.
Its nine implementation lessons live under `content/articles/ai-collaboration-*/index.en.md`.
Do not apply certification domain weights or quiz-bank requirements to this course.

## Synthetic Lab

`static/downloads/ai-collaboration-lab/` supplies the source files for the downloadable ZIP.
Rebuild `static/downloads/ai-collaboration-lab.zip` after editing lab files. Exclude `__pycache__`.
Run `python3 -m unittest discover -s static/downloads/ai-collaboration-lab -v`.
Test the extracted ZIP separately before publishing.

The checker validates consistency and hashes against a supplied base. It does not validate
identity, approval, live Cloud permissions, or runtime deletion. Mixed-track repository
requirement copies remain snapshots. They do not establish Confluence authority.

## Review Boundaries

CODEOWNERS with several names accepts one matching owner, not every named owner.
Numeric review thresholds do not establish business roles. Jira transition restrictions
control the transition actor, not two-owner approval. Label procedural role checks explicitly.
Confluence Free lacks content restrictions. Jira Free lacks configurable permission schemes.
Verify current official plan documentation before revising dependent exercises.

## Authoring and Rendering

Split large content edits into small patches. Shell command inputs are capped at 12,000
characters. An oversized heredoc fails before writing the intended content.
Use existing validated cover assets unless a new cover pipeline is explicitly required.
Record section-to-cognitive-level review separately from reader headings.

The course review maps terms/Key Takeaways to Remember and Understand, setup and
worked procedures to Apply, evidence/comparison tables to Analyze, control choices
and rollback decisions to Evaluate, and exercises/capstone records to Create.
Keep expected reasoning separate from observed tenant results. Local unit tests do
not replace live access-denial tests. Verify rendered navigation and parse JSON-LD
objects on all ten pages after a course-wide render.

## Practical Depth

Each lesson needs a worked workflow between setup and verification, not only a control
checklist. Include a distinct artifact, evidence interpretation, failure diagnosis, and
completion check. Preserve the shared export-service scenario across both tracks.
Run executable examples against a fresh extracted archive. Label proposed outcomes as
expected until a sandbox produces evidence. The candidate requirement's `approved`
schema field does not establish owner approval. Explain this next to candidate edits.