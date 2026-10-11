# Non-Certification Course Hubs and Offline Labs

Use this rule for new project courses outside certification prep and the Practical AI Workflow course.

## Course Hubs

The current theme's section list template does not render a section `_index.en.md` body. Put a course outline that readers need to see in `content/<course-slug>-start/index.en.md`. Link lessons back to that leaf page. After rendering, inspect the hub HTML for the audience, prerequisites, outcomes, lesson order, and skills sections. A successful Hugo exit alone does not prove the outline appears.

## Offline Labs

If a course claims a complete local learning path, provide fixtures and an executable checker or simulator for each assessed skill that otherwise requires a cloud account, SIEM, MCP server, or external service. Name the simulation boundary. Do not describe a local predicate checker as a full Sigma parser or a policy simulator as a live service test.

Run every fixture with a fresh temporary copy. Record the expected decision, observed decision, and exit code. Link the exact download from the lesson and capstone. Require the capstone reference to distinguish local evidence from future production checks.

## Cross-Page Consistency

Compare the hub, lesson steps, quiz threshold, answer key, capstone rubric, and reference answer before release. A rule such as an eight-question minimum must mean the same thing in each location. Recheck the rendered links after moving a hub or adding a downloadable fixture.
