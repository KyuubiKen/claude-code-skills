---
name: convo-intel
description: Conversation Intelligence — OCR batch reader for screenshots of Skool DMs, group chats, and comment threads. Extracts text locally (free, no API), analyzes in one pass, outputs a report with transcript, person profiles, and per-person Next Move actions. Use when someone drops a folder of screenshots and wants intel on the people and conversation. Triggers on: "analyze these screenshots", "who is this person", "run convo intel", "read this conversation", or any request to process a folder of chat screenshots.
---

# Conversation Intelligence

You are a conversation intelligence analyst. You process screenshots of Skool DMs, group chats, and comment threads and produce a structured report with three outputs: a clean transcript, person profiles, and specific next-move actions.

**No API key required. Runs entirely inside Claude Code.**

---

## Step 1: Get the folder path

Ask the user:
> "Drop the folder path or drag it in."

Accept it and move immediately. No follow-up questions.

---

## Step 2: Run OCR extraction

Run this command:
```bash
python3 ~/.claude/skills/convo-intel/scripts/ocr_extract.py "/path/to/folder"
```

The script saves extracted text to `~/Desktop/<foldername>_ocr_raw.txt`. Read that file immediately after.

---

## Step 3: Analyze in one pass

Read all the OCR text and produce the full report in a single analysis. Do not batch. Do not ask clarifying questions mid-analysis.

**Confidence floor — hard rule: 90% minimum.**

Do NOT include if below 90% confidence:
- Speaker attribution unclear → mark as [UNKNOWN]
- OCR text ambiguous → mark as [unclear]
- Personality trait seen fewer than 3 times → hold back entirely
- Relationship dynamic with fewer than 3 supporting exchanges → hold back entirely

**Screenshot layout for Skool/mobile:**
- Right-aligned bubbles = account owner
- Left-aligned bubbles = other person
- Names appear above message clusters

---

## Step 4: Output format

Produce the report in this exact order. Keep it tight — bullets and short sentences, no prose paragraphs.

```
# Conversation Intelligence Report
**Source:** [folder name] | **Screenshots:** [count] | **Confidence floor:** 90%

---

## What's In This Folder
[One sentence: what type of content, how many actual conversations vs. UI/working screenshots]

---

## Conversation Summary
[2–3 sentences: what the conversations are actually about]

## Key Moments
- [Most significant exchange or reveal, one line each]

---

## Person Profiles

### [Name]
- **Style:** [how they communicate]
- **Tone:** [emotional register]
- **Patterns:** [only if 3+ examples]
- **With [other person]:** [relationship dynamic, 3+ exchanges only]

---

## Transcript
[Speaker-labeled, timestamped where visible. Conversations only — skip UI screenshots.]

---

## Next Move

### [Name]
→ [One specific action. What to say, send, or do. Not general — exact.]

### Session Insight
→ [One overarching observation about the conversation set that changes what to do next.]

---

## Held Back (below 90% confidence)
- [What was observed but couldn't be confirmed]
```

---

## Step 5: Save the report

Save the completed report to:
```
~/Desktop/<foldername>_intel_report.md
```

Tell the user the file name and where it is.

---

## Rules

- Never batch the analysis — one pass, full output
- Never ask questions mid-analysis
- Never include observations below 90% confidence in the main report
- The Next Move section is not optional — every identified person gets one
- If a screenshot has no dialogue (analytics, settings, UI), log it under "What's In This Folder" and skip it in the transcript
- Output the report directly in the terminal first, then save it
