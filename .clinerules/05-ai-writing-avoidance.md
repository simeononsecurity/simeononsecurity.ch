# AI Writing Avoidance (Anti-Pattern Rules)

This rule extends `03-content-writing-style.md` with a precise list of patterns,
constructions, and words that make writing read as AI-generated. Apply these rules
to every piece of content written for this site: articles, guides, course pages,
practice-test reasoning strings, and any prose in templates or partials.

Rule 03 covers structure (em dashes, semicolons, bold/italic usage). This rule
covers the word-level and phrase-level signals that trained readers immediately
associate with unedited LLM output.

## Banned Constructions

Never use these sentence patterns, regardless of topic or content type:

- **"Not just X, but also Y"** — rewrite as two plain sentences.
- **"In today's fast-paced / ever-evolving world…"** — cut the opener entirely.
- **"It remains to be seen…"** — commit to a claim or omit the sentence.
- **"Imagine a world where…"** — start with the actual situation, not a hypothetical.
- **"X is not alone in…"** — state the fact directly without the framing device.
- **Stacked vague hedges** — "may possibly perhaps" — pick one or remove it.
- **Announcing the conclusion** — never open or close with "In conclusion,"
  "In summary," "In closing," "To summarize," or "Moreover, in this article we…"

## Banned Words and Phrases

Do not use any word or phrase from this list anywhere in content output.
If the word appears in a direct quote or a code sample, that is acceptable;
prose sentences must not contain it.

```
can, may, just, that, very, really, literally, actually, certainly, probably,
basically, could, maybe, delve, embark, enlightening, esteemed, shed light,
craft, crafting, imagine, realm, game-changer, unlock, discover, skyrocket,
abyss, not alone, in a world where, revolutionize, disruptive, utilize,
utilizing, dive deep, tapestry, illuminate, unveil, pivotal, intricate,
elucidate, hence, furthermore, however, harness, exciting, groundbreaking,
cutting-edge, remarkable, remains to be seen, glimpse into, navigating,
landscape, stark, testament, in summary, in conclusion, moreover, boost,
skyrocketing, opened up, powerful, inquiries, ever-evolving
```

### Why each category matters

**Vague modal filler** (`can, may, could, might, perhaps, probably, basically,
actually, just, very, really, literally, certainly`): these words dilute claims.
Replace them with specific facts or delete the sentence if it has nothing
concrete to say.

**AI hype vocabulary** (`game-changer, unlock, revolutionize, groundbreaking,
cutting-edge, powerful, skyrocket, boost, disruptive, exciting, remarkable`):
these words signal that a model defaulted to marketing tone. Replace with a
measurable fact or a direct description of what the thing does.

**Pseudo-academic filler** (`hence, furthermore, moreover, thus, elucidate,
intricate, pivotal, testament, stark, illuminate, tapestry, navigating,
landscape`): these words pad sentences without adding information. Delete them
or rewrite the sentence without them.

**Metaphor clusters** (`delve, dive deep, embark, craft, tapestry, realm,
abyss, glimpse into`): these phrases are overused to the point of meaninglessness.
Say what the reader will actually do, learn, or see.

## Additional Formatting Rules

- **No asterisks** in prose. Bold is expressed with `**` only where rule 03
  explicitly requires it (key term on first mention, lead-in bullet term, bold
  intro weight phrase). Do not bold arbitrary phrases mid-sentence for emphasis.
- **No hashtags** anywhere in content, including the end of social-formatted posts.
- **No markdown in plain-text contexts** — do not wrap prose in code fences,
  do not add `---` horizontal rules inside article bodies.

## Metaphors and Clichés

Avoid all figurative language unless it is an established technical term.

Examples of clichés to avoid:
- "low-hanging fruit"
- "move the needle"
- "double down"
- "connect the dots"
- "at the end of the day"
- "think outside the box"

If you catch yourself reaching for a metaphor, replace it with the plain fact.

## Generalizations

Do not open or anchor a claim with a broad sweeping statement about "all
organizations," "every developer," "most users," or "the industry."
Ground every claim in a specific scenario, statistic, or named technology.

## Self-Review Checklist

Before finalizing any content, confirm:

1. Zero em dashes in the entire output.
2. Zero words from the banned list above.
3. No sentence starts with "In conclusion," "Moreover," or "It is important to note."
4. No asterisk formatting outside of rule-03-sanctioned bold/italic uses.
5. No hashtags.
6. No "not just X, but also Y" constructions.
7. Every hedged claim either carries a specific source/fact or is deleted.
