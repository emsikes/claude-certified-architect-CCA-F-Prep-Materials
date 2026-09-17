Enforecement Spectrum
1. Prompt-based guidance
    - probablistic, 90-95% reliable
    - few shot examples
2. Programmatic Enforcement
    - deterministic
    - fixed regardless of model output variation
  
- Decsion rule: financial loss, security breach, or compliance violation - always use programatic enforcement  
- Routing is not enforcement:
  - routing classifier decides which agent handles a request, nothing more
  - routing does NOT fix a compliance failure that happens within an agent's execution sequence
  - the fix is per-agent workflow ordering, verify before refund, check before acting, enforce by gates and hooks

Hook Identifiers
1. PreToolUse
   - runs before a tool executes
   - can block, modify, pause for approval, or redirect on the outgoing call so the tool never runs
   - compliance gate
2. PostToolUse
   - runs after a tool executes but before the model processes the result
   - transforms and normalizes data
   - not effective for policy enforcement
   - use for things like common date formatting and other data normalization
3. Subagent Lifecycle Hooks
   - SubagentStart
     - Fires when a subagent is spawned via the Agent tool, log, validate, rate-limit, check context
   - SubagentStop
     - Fires when a subagent finishes, validate output against schema, strip sensitive data, record completion
   - Scoped Hooks
     - Subagents can declare their own PreToolUse/PostToolUse hooks scoped only to their execution
   - Auto-Conversion
     - A stop hook in a subagent auto-converts to a SubAgentStop event at runtime

Handoff Fields
1. Handoff summary should be generated to be passed along for human review as needed
   - e.g. customer ID, conversation summary, root cause analysis, refund amount, recommended action 

Decomposition Tradeoffs
1. Fixed pipelines
   - consistent, reliable, easy to debug
   - same input, same path
2. Dynamic decomposition
   - adapts to emerging complexity
   - more thorough on open-ended work
   - less predictable, variable time, harder cost estimates, harder to debug
  
Attention Dilutoin - when an agent processes too many items in one pass, a finite attention budget spreads thing
1. Symptoms: 
   - shallow analysis late in a batch
   - same pattern flagged in one file but approved in another
   - obvious bugs missed while sylistic variances caught early
2. Fix - multi-pass architecture
   - a dedicated per-item local pass (full budget per item)
   - plus a separate cross-item integration pass
   - anti-patter: not a bigger model or larger context