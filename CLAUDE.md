# Project Notes

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
