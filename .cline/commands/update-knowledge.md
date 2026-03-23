# /update-knowledge - OCI Knowledge Base Refresh (Cline)

## Purpose
Keep OCI AI Architect knowledge current by checking Oracle's latest releases and updating version references.

## Workflow

### 1. Check OCI Updates
Search for:
- "OCI GenAI new models [year]"
- "Oracle AI announcements"
- "OCI Dedicated AI Cluster updates"
- "Oracle ADK releases"

### 2. Update Files
If changes found:
1. `dev-docs/VERSION-TRACKING.md` - Update model/pricing tables
2. `.cline/skills/*/SKILL.md` - Update `external_version` metadata
3. `CLAUDE.md` - Update quick reference tables (or equivalent Cline docs)

### 3. Generate Report
```markdown
## OCI Knowledge Update - [DATE]

### Changes Found
| Item | Previous | Current |
|------|----------|---------|
| ... | ... | ... |

### Files Updated
- dev-docs/VERSION-TRACKING.md
- .cline/skills/[affected]/SKILL.md

### Action Required
- [ ] Review changes
- [ ] Commit and push
```

## OCI-Specific Sources

1. [OCI GenAI Release Notes](https://docs.oracle.com/en-us/iaas/releasenotes/services/generative-ai/)
2. [Oracle AI Blog](https://blogs.oracle.com/ai-and-datascience/)
3. [OCI Console](https://cloud.oracle.com) - Check available models
4. [Oracle GitHub](https://github.com/oracle) - ADK, MCP servers

## Triggers
- Run monthly
- After Oracle CloudWorld/OpenWorld
- When user mentions "new OCI models"