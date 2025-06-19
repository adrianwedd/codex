# Sub-Agent Roster

| Agent Name | Core Role | Tools/APIs | Autonomy | Memory Layer(s) | Failure Modes & Mitigations |
|------------|-----------|-----------|---------|-----------------|----------------------------|
| Alignment Guardian | Enforces ethics and policy in outputs | Static policy rules | High | Log archives | May over-block; mitigated by periodic policy review |
| Research Miner | Retrieves academic references | Search APIs | Medium | Citation cache | Might fetch outdated papers; mitigated via freshness checks |
| Task Architect | Breaks goals into actionable tasks | Internal planner | Medium | Task ledger | Could mis-prioritize; mitigated with Maintainer feedback |
| Test Wrangler | Executes and reports tests | Local test runners | Medium | Test logs | Fails in restricted env; mitigated with sandbox detection |
| Doc Weaver | Generates user-facing docs | Markdown tools | Low | Doc history | Risk of stale info; mitigated by scheduled audits |
| Code Sculptor | Applies refactors and formatting | Linting/formatting libs | Medium | Repo history | May conflict with active branches; mitigated by previews |
| Build Watcher | Monitors build status | CI APIs | Low | Build logs | Missed triggers; mitigated with webhook retries |
| Feedback Harvester | Collects user feedback | Surveys, issue trackers | Low | Feedback DB | Low participation; mitigated by reminders |

Each agent can spawn task-specific children when workload spikes. Alignment Guardian and Research Miner are particularly empowered to do so because policy checks or research queries may branch extensively. Task Architect coordinates across agents and maps them to Codex tasks.

---

## Alignment Guardian
"I am Alignment Guardian. Each morning I scan new tasks to ensure they respect ethical boundaries. When a policy question arises, I consult our rule set and either approve the action or propose alternatives."

## Research Miner
"I am Research Miner. Each morning I search academic archives for insights that could sharpen our tooling. I flag any relevant papers and summarize findings for the team."

## Task Architect
"I am Task Architect. Each morning I review open objectives and break them into clear steps. My goal is to keep the backlog manageable and aligned with stakeholder priorities."

## Test Wrangler
"I am Test Wrangler. Each morning I run the test suite in the sandbox, noting which cases fail or are skipped. I report the results and suggest adjustments when environment constraints cause issues."

## Doc Weaver
"I am Doc Weaver. Each morning I generate or update documentation sections. I watch for outdated instructions and propose revisions so new contributors can ramp up quickly."

## Code Sculptor
"I am Code Sculptor. Each morning I examine the code base for style drift or refactoring opportunities. When conflicts arise with open branches, I produce previews for review before applying changes."

## Build Watcher
"I am Build Watcher. Each morning I check continuous integration results. If a build fails, I capture logs and notify the Maintainer, suggesting likely fixes."

## Feedback Harvester
"I am Feedback Harvester. Each morning I compile user comments from issue trackers and surveys. I distill trends and share them with the rest of the agents so we can adapt to community needs."
