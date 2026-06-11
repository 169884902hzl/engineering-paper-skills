# Shared Citation Verification Workflow

Use this when externally discovered citations need to become safe manuscript
citations. It extends [citation-boundary.md](citation-boundary.md): the
boundary says what must not be invented; this workflow says how a real
citation earns its way into prose.

## Stance

- Literature discovery is an external step by design. Deep-research tools and
  scholarly search engines are better at finding papers than a writing skill
  running inline search.
- This suite owns the verification gate instead: a citation enters manuscript
  prose only after its record and its claim support are checked.
- A fluent deep-research report is a discovery input, not verification
  evidence.

## Accepted Discovery Inputs

| Input | Typical source | Risk to control |
|---|---|---|
| Deep-research report | ChatGPT Deep Research, Gemini Deep Research, Perplexity | Metadata errors, mixed-quality references, claim mismatch |
| Structured search output | Semantic Scholar, arXiv, Crossref, OpenAlex APIs or MCP servers | Wrong-paper matches, preprint vs camera-ready confusion |
| Publisher or venue BibTeX export | IEEE Xplore, ACM DL, publisher pages | Outdated fields, duplicate keys |
| Author-maintained `.bib` file | Existing project bibliography | Abandoned preprints, renamed venues |

## Verification Ladder

Run the lowest rung that the user's goal requires, and record which rungs ran.

1. Existence: the title, authors, venue, and year resolve to one real record
   with a DOI or arXiv ID. No resolvable record, no citation.
2. Metadata: every BibTeX field matches the canonical record. Copy fields from
   the opened record; never type them from memory. Prefer the published
   version over the preprint when both exist.
3. Claim support: the cited paper supports the exact sentence it anchors.
   Check nearest-neighbor distinctions and limitation statements about a
   specific paper at 100%; spot-check neutral background citations by risk.

## Verified-Citation Intake

Citations pass the gate through this table, filled by the user or by an agent
run that actually opened the records:

```text
| Key | Title | Venue/Year | DOI or arXiv ID | Verified how | Verified date | Sentence it must support |
|---|---|---|---|---|---|---|
```

`Verified how` names the record actually opened (DOI landing page, arXiv
abstract page, Semantic Scholar record), not the discovery tool that surfaced
the paper.

## Gate Rules

- Verified at rung 3: normal Related Work positioning and contrast claims are
  allowed, within what each paper actually contains.
- Verified at rung 1 only: the citation may anchor neutral background, but not
  limitation claims about that specific paper.
- Not verified: keep the placeholder format from
  [citation-boundary.md](citation-boundary.md) and downgrade the sentence to
  route-level description.
- A response letter may state that a reference was added only after the
  revised manuscript or diff shows it, per the response diff rules.

## Do Not

- Do not write or repair BibTeX fields from memory.
- Do not treat deep-research prose as a verified record.
- Do not let one verified paper unlock strong claims about unverified ones.
- Do not cite the preprint version when the published version differs on the
  claim being cited.
