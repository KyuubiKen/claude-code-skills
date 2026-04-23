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

---

## How to Install Any Skill

```bash
# Clone this repo
git clone https://github.com/KyuubiKen/claude-code-skills.git

# Copy the skill you want into your Claude skills directory
mkdir -p ~/.claude/skills/youtube-channel-audit
cp claude-code-skills/youtube-channel-audit/SKILL.md ~/.claude/skills/youtube-channel-audit/SKILL.md
```

Then inside Claude Code, type `/youtube-channel-audit` to invoke it.

---

## About

Built by [Ken Khamphiphone](https://github.com/KyuubiKen) — educator and content creator focused on making Claude Code accessible to non-technical creators. I teach Claude Code workflows through tutorials, community, and open-source tools.

More skills coming. Star the repo if you find it useful.
