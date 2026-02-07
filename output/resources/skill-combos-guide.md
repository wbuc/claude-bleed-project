# How to Combine Claude Code Skills

Chain skills together to go from idea to finished output. Each workflow below shows the skill order, what it does at each step, and the prompt pattern to use.

---

## 1. Pitch Deck Creation

**Goal**: Research-backed, persuasive investor deck

| Step | Skill | What it does |
|------|-------|-------------|
| 1 | `/last30days` | Research what people are saying about your market, pain points, competitors |
| 2 | `/marketing-psychology` | Pick the right persuasion framework for your audience (loss aversion, social proof, anchoring) |
| 3 | `/copywriting` | Write slide-by-slide copy: headline, problem, solution, traction, ask |
| 4 | `/copy-editing` | Tighten every slide to be punchy and clear |
| 5 | `/humanizer` | Remove any AI-sounding language before presenting |
| 6 | `/frontend-design` | Build the visual slide as a polished HTML page |

**Example prompt flow**:
```
/last30days "blood testing consumer pain points"
→ then: "Using the marketing-psychology skill, what mental models work best
   for health-tech investor pitches?"
→ then: /copywriting "Write pitch deck copy for a blood diagnostics startup.
   Use the research and psychology insights from above."
→ then: /copy-editing "Edit the deck copy for clarity and punch"
→ then: /humanizer "Clean up the final copy"
→ then: /frontend-design "Create a visual slide for [specific slide]"
```

---

## 2. Research to Blog Post

**Goal**: Turn market research into a published article

| Step | Skill | What it does |
|------|-------|-------------|
| 1 | `/last30days` | Gather real conversations, pain points, trending topics from Reddit/X |
| 2 | `/content-researcher-writer` | Structure findings into an outline, add citations, write each section with feedback |
| 3 | `/copy-editing` | Edit for flow, clarity, and readability |
| 4 | `/humanizer` | Strip AI patterns so it reads naturally |

**Example prompt flow**:
```
/last30days "what developers are saying about AI code review tools"
→ then: /content-researcher-writer "Write a blog post about the rise of AI
   code review. Use the research above as primary source material.
   Target audience: engineering leads."
→ then: /copy-editing "Edit this blog post — tighten the intro,
   check the flow between sections"
→ then: /humanizer "Make this sound natural"
```

---

## 3. Research to Social Media Content

**Goal**: Turn insights into platform-ready posts

| Step | Skill | What it does |
|------|-------|-------------|
| 1 | `/last30days` | Find real quotes, stats, pain points people are discussing |
| 2 | `/marketing-psychology` | Identify which hooks and triggers will resonate (curiosity gap, controversy, specificity) |
| 3 | `/social-content` | Create platform-specific posts (LinkedIn, X, etc.) using the research and psychology |
| 4 | `/humanizer` | Clean up so posts don't sound AI-generated |

**Example prompt flow**:
```
/last30days "remote work burnout discussions"
→ then: "Using marketing-psychology, what hooks work best for LinkedIn
   engagement on workplace topics?"
→ then: /social-content "Create 5 LinkedIn posts and 5 tweets about remote
   work burnout. Use the real quotes and stats from the research.
   Apply the hooks from the psychology analysis."
→ then: /humanizer "Make these sound like a real person wrote them"
```

---

## 4. Competitor Research to Landing Page

**Goal**: Build a comparison or alternatives page

| Step | Skill | What it does |
|------|-------|-------------|
| 1 | `/last30days` | Research what people complain about with competitors |
| 2 | `/competitor-alternatives` | Structure a full comparison/alternatives page with SEO in mind |
| 3 | `/copywriting` | Write the landing page copy with clear positioning |
| 4 | `/copy-editing` | Polish and sharpen |
| 5 | `/frontend-design` | Build the page as a working HTML/CSS prototype |

**Example prompt flow**:
```
/last30days "[Competitor name] complaints and frustrations"
→ then: /competitor-alternatives "Create a [Your Product] vs [Competitor] page.
   Use the pain points from research as ammunition."
→ then: /copywriting "Rewrite the hero section and CTAs to be more compelling"
→ then: /copy-editing "Final pass for clarity"
→ then: /frontend-design "Build this as a responsive landing page"
```

---

## 5. Product Launch Campaign

**Goal**: Full launch plan with content ready to go

| Step | Skill | What it does |
|------|-------|-------------|
| 1 | `/last30days` | Understand current market conversation and timing |
| 2 | `/launch-strategy` | Plan the phased launch (pre-launch, launch day, post-launch) |
| 3 | `/marketing-psychology` | Choose persuasion tactics for each phase (scarcity, social proof, urgency) |
| 4 | `/copywriting` | Write landing page, email, and announcement copy |
| 5 | `/social-content` | Create launch day social posts for all platforms |
| 6 | `/copy-editing` | Final edit pass on all content |
| 7 | `/humanizer` | Clean everything before publishing |

---

## 6. Blog Post to Multi-Channel Content

**Goal**: Repurpose one piece of content across channels

| Step | Skill | What it does |
|------|-------|-------------|
| 1 | `/content-researcher-writer` | Write the original long-form blog post |
| 2 | `/social-content` | Break it into LinkedIn posts, tweet threads, Instagram captions |
| 3 | `/copywriting` | Create an email version or landing page teaser |
| 4 | `/humanizer` | Clean all outputs |

---

## 7. Lead Generation Campaign

**Goal**: Find leads and create outreach content

| Step | Skill | What it does |
|------|-------|-------------|
| 1 | `/lead-research-assistant` | Identify target companies and contact strategies |
| 2 | `/marketing-psychology` | Choose the right approach angle for cold outreach |
| 3 | `/copywriting` | Write outreach emails and landing page copy |
| 4 | `/humanizer` | Make outreach feel personal, not templated |

---

## Tips

- **You don't need every step**. Skip what's not relevant. The power is in knowing the order.
- **Reference previous output**. Say "use the research from above" or "apply the psychology insights" so each skill builds on the last.
- **Save intermediate output**. Ask Claude to save research or drafts to `output/` so you can reference them later.
- **Mix and match**. These are patterns, not rules. Create your own combos based on what you need.

---

## Quick Reference: All Skills

| Skill | Best for |
|-------|----------|
| `/last30days` | Market research from Reddit, X, web |
| `/marketing-psychology` | Mental models, persuasion frameworks |
| `/copywriting` | Landing pages, headlines, CTAs |
| `/copy-editing` | Editing and tightening existing copy |
| `/humanizer` | Removing AI-sounding language |
| `/content-researcher-writer` | Long-form content with citations |
| `/social-content` | Platform-specific social posts |
| `/competitor-alternatives` | Comparison and alternative pages |
| `/launch-strategy` | Product launch planning |
| `/lead-research-assistant` | Finding and researching leads |
| `/marketing-ideas` | Brainstorming marketing tactics |
| `/frontend-design` | Building visual HTML/CSS pages and components |
| `/skill-creator` | Creating new custom skills |
