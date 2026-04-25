# Claude Code Skills

A collection of custom skills for [Claude Code](https://claude.ai/code) — free and open source.

Claude Code skills are markdown-based instruction files that extend what Claude can do inside your terminal. Drop one in `~/.claude/skills/<skill-name>/SKILL.md` and invoke it with `/skill-name`.

---

## Skills Included

### `/youtube-channel-audit`
Analyze any YouTube channel using `yt-dlp` (free, no API costs). Pulls real video data — views, titles, likes, duration — and delivers a structured content strategy report.

**What it does:**
- Scrapes up to 30+ videos from any public YouTube channel
- Breaks down hook patterns, topic clusters, and format performance
- Identifies your top 3 highest-probability next videos — backed by data
- Works on any channel, not just your own

**Requires:** `yt-dlp` installed (`brew install yt-dlp`)

### `/lyra`
Transform any rough idea or weak prompt into a precision-crafted AI instruction — and save it to your Desktop as both a `.md` and `.docx` file automatically.

**What it does:**
- Diagnoses what's missing from your prompt (clarity, context, structure, constraints)
- Applies the right technique based on request type (creative, technical, educational, image gen, system prompts)
- Delivers a fully optimized prompt — no explanation, just the finished product
- Auto-saves output to Desktop as `.md` + `.docx` via bundled Python script

**Requires:** `python-docx` (`pip3 install python-docx`)

### `/convo-intel`
Drop a folder of screenshots — Skool DMs, group chats, comment threads — and get back a full conversation intelligence report. Transcript, person profiles, and a specific next action for every person identified. No API key required.

**What it does:**
- OCRs all screenshots locally using Apple's built-in Vision framework (free, no internet needed)
- Identifies every person in the conversation and builds a profile
- Applies a 90% confidence floor — nothing below it appears in the output
- Ends every report with a Next Move section: one specific action per person
- Saves a `.md` report to your Desktop automatically

**Requires:** macOS only — `pip3 install pyobjc-framework-Vision pyobjc-framework-Quartz`

---

## How to Install Any Skill

```bash
# Clone this repo
git clone https://github.com/KyuubiKen/claude-code-skills.git

# Copy the skill you want into your Claude skills directory
# Example: convo-intel (includes a scripts folder)
mkdir -p ~/.claude/skills/convo-intel/scripts
cp claude-code-skills/convo-intel/SKILL.md ~/.claude/skills/convo-intel/SKILL.md
cp claude-code-skills/convo-intel/scripts/ocr_extract.py ~/.claude/skills/convo-intel/scripts/ocr_extract.py
```

Then inside Claude Code, type `/convo-intel` to invoke it.

---

## About

Built by [Ken Khamphiphone](https://github.com/KyuubiKen) — educator and content creator focused on making Claude Code accessible to non-technical creators. I teach Claude Code workflows through tutorials, community, and open-source tools.

More skills coming. Star the repo if you find it useful.
