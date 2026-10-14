# Non-Certification Course Hubs and Offline Labs

Use this rule for new project courses outside certification prep and the Practical AI Workflow course.

## Course Hubs

The current theme's section list template does not render a section `_index.en.md` body. Put a course outline that readers need to see in `content/<course-slug>-start/index.en.md`. Link lessons back to that leaf page. After rendering, inspect the hub HTML for the audience, prerequisites, outcomes, lesson order, and skills sections. A successful Hugo exit alone does not prove the outline appears.

Put lessons, labs, quizzes, capstones, and answer keys for one course in `content/<course-slug>/<lesson-slug>/index.en.md`. Keep those pages out of `content/articles/` so the source layout and rendered paths match the other non-certification courses. When moving a published course page, update every course link and add redirects from both forms of its former URL. Check the old URLs, new URLs, and article listing in the rendered output.

## Offline Labs

If a course claims a complete local learning path, provide fixtures and an executable checker or simulator for each assessed skill that otherwise requires a cloud account, SIEM, MCP server, or external service. Name the simulation boundary. Do not describe a local predicate checker as a full Sigma parser or a policy simulator as a live service test.

Run every fixture with a fresh temporary copy. Record the expected decision, observed decision, and exit code. Link the exact download from the lesson and capstone. Require the capstone reference to distinguish local evidence from future production checks.

## Cross-Page Consistency

Compare the hub, lesson steps, quiz threshold, answer key, capstone rubric, and reference answer before release. A rule such as an eight-question minimum must mean the same thing in each location. Recheck the rendered links after moving a hub or adding a downloadable fixture.

Check the learning path in order. Introduce terms before relying on them, install a tool before showing commands that use it, and give each supported platform a working verification route. Match each hub outcome and capstone rubric to the evidence the learner actually collects. Label offline and live routes separately.

Keep scored quiz questions and their answer key on separate pages. Keep a capstone prompt and its full reference decision on separate pages. Link the key only after the learner's attempt instructions. State the pass threshold, any required core questions, and the correction or retest route on the hub as well as the assessment page.

An offline simulator must label its boundary and produce observed decisions from a fresh local copy. Check allow, deny, revocation, and cleanup where the lesson claims those outcomes. Refuse input/output path collisions and preexisting evidence files before writing or removing files. Give a paper-only plan partial credit when the outcome requires observed simulator evidence. Do not present local cleanup as proof that a live cloud object was removed.

Keep course review sign-off JSON, source snapshots, and validation reports in temporary or ignored report paths. Do not add these records to Hugo `data/` or commit them with the course. Before committing, check `git ls-files data/course_release_signoffs` returns no files.
