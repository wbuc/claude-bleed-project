# Project Notes

## General Information
- Your responses should be clear and to the point. Leading with the result followed by an explenation.
- **Single source of truth:** All project memory, lessons learned, output rules, and research sources live in this CLAUDE.md file. Never save to MEMORY.md. This file is the only place for persistent project knowledge.
- **All generated output goes in `output/`** unless the user specifies a different location.
- Do not create new top-level folders without explicit instruction.

## Trust & Honesty — Non-Negotiable
Trust is the foundation of everything we publish. If we lose credibility once, a hundred good posts won't rebuild it.

- **Write from the source, not from summaries.** When given a link or article, fetch and read it before writing. Content must be based on what the source actually says, not paraphrased plans or secondhand descriptions.
- **Every claim needs a receipt.** All research-based content must include a references section at the bottom with direct links to the source material (DOI, PubMed, or the article URL). If someone queries us, we need to point them to exactly where a claim came from.
- **Use exact numbers from the research.** Don't round, don't approximate, don't guess. If the study says 106,973 women, write 106,973. If a gene shifts timing by 5.61 years, write 5.61.
- **Flag what's established vs emerging.** Verified findings get stated confidently with a source link. Emerging evidence gets flagged ("early research suggests..."). Personal observations get owned ("I've noticed a pattern but don't have a study for this yet").
- **Never fabricate or assume details.** If a source doesn't confirm something, don't include it. Gaps in knowledge are fine. Wrong claims are not.
- **Verify author names, institutions, and dates** against PubMed or the original paper before publishing. Getting the basics wrong undermines everything else.

## Reference Rules for Content Output
When generating any content based on research (blog posts, social scripts, health education):
1. **Fetch the source article** before writing. If the direct URL fails (e.g., nature.com 303 redirects), use fallback sources like PubMed, ScienceDaily, or news summaries.
2. **Cross-check claims** against at least two sources where possible.
3. **Include a references section** at the bottom of every output file with:
   - Full citation (Author, Title, Journal, Year)
   - DOI or direct URL
   - Any secondary sources used for verification
4. **Keep references auditable.** If anyone asks "where did you get that?", the answer should be in the file.

## Priority Research Sources
Papers and URLs already verified. Fetch these to cross-check claims when creating related content.

### Ovarian aging, cancer risk & de novo mutations
- **Paper:** Stankovic, S. et al. "Genetic links between ovarian ageing, cancer risk and de novo mutation rates." Nature (Sept 2024)
- **DOI:** https://doi.org/10.1038/s41586-024-07931-x
- **Nature URL:** https://www.nature.com/articles/s41586-024-07931-x (returns 303 on WebFetch — use fallbacks)
- **PubMed:** https://pubmed.ncbi.nlm.nih.gov/39261734/
- **ScienceDaily:** https://www.sciencedaily.com/releases/2024/09/240911112144.htm
- **News-Medical.net:** https://www.news-medical.net/news/20240912/New-gene-variants-linked-to-early-menopause-and-cancer-risk-identified.aspx
- **MRC Epidemiology Unit:** https://www.mrc-epid.cam.ac.uk/blog/2024/09/11/genes-menopause-timing-cancer-risk/
- **Drug Discovery News:** https://www.drugdiscoverynews.com/rare-gene-variants-may-influence-reproductive-age-and-cancer-risk-16109
- **Verified claims:** 5 new genes (ETAA1, ZNF518A, PNPLA8, PALB2, SAMHD1), 4 previously reported (BRCA2, CHEK2, HELB, HROB), ZNF518A = 5.61-year shift, SAMHD1 = 1.35 years later, 106,973 women sample, 7/9 genes in DNA repair, SAMHD1 cancer link in both sexes, 8,089 family trios from 100K Genomes Project, BRCA1 = 2.1 years earlier, BRCA2 = 1.18 years earlier
- **Used in:** `output/content/ovarian-aging-genes/`

## MCP Configuration
- Using Brave Search MCP for web search (configured in `.mcp.json`)
- Brave API key stored in `.env`
- Removed chrome-devtools MCP (not needed)

## /last30days Skill
- Installed at `.claude/skills/last30days/` (project-local, forked from github.com/mvanhorn/last30days-skill)
- **Modified**: Replaced OpenAI API with Brave Search API for Reddit discovery
- API keys loaded from project `.env` only (no global config)
- Reddit search: Brave Search API (`BRAVE_API_KEY` in project `.env`)
- X/Twitter search: xAI API (`XAI_API_KEY` - placeholder in `.env`, needs real key)
- Pipeline preserved: Brave Search finds Reddit threads -> enrich with real Reddit JSON -> score/dedupe -> synthesize
- **Always show source counts in the response footer** (e.g., Reddit: 12 threads | 340 upvotes, X: 8 posts | 120 likes, Web: 5 pages)

## Lessons Learned
- When writing health/science content, always WebFetch the source paper first to verify specific numbers, gene names, and claims — don't rely solely on summaries provided in plans.
- nature.com returns 303 redirects on WebFetch. Use PubMed, ScienceDaily, or news summaries as fallback sources.
- When a plan references a prior session transcript, read it — it likely contains fetched data that the plan summary condensed or lost.
