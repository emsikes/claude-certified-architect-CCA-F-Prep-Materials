Why centralization exists
- Observability
  - Each message is logged and monitored in one place
- Consistent error handling
  - One uniform recovery policy applied centrally
- Controlled information flow
  - The coordinator decides what context each subagent recieves
  - Direct subagent communication is an anti-pattern as it undoes all of these benefits

Isolation
- Applied per-invocation, subagents do not share memory between invocations
- Every invocation is fully independant (no shared store for later lookup)
- Coordinator must pass facts explicitly

Coordinator duties
- Dynamic subagent selection, don't always run the full pipeline, a simple query may invoke only one subagent
- Research scope partitioning, assign each subagent a distinct subtopic of source type to minimize overlap
- Iterative refinement loops, evaluate aggregated output for gaps and re-delegate targetted follow-ups 

Narrow decomposition failure
- When output is incomplete in scope - whole categories missing, not merely shallow
- Root cause is almost always the coordinator's decomposition, not downstream subagent failure
  - e.g. splitting "renewable energy" into only solar and wind means geothermal and tidal can never be covered
  - The fix is to broaden the decomposition - never add more subagents, they inherit equally narrow assignments

Spawning tool rename
- Spawning tool is now named Agent as of Claude Agent SDK v2.1.63
- The coordinators allowedTools must include "Agent" or "Task"
- AgentDefinition Description, each subagent's description specifically helps the coordinator decide when to invoke that subagent

Goal-oriented conext
- Goal oriented prompts let subagents adapt to unexpected situations and adjust, don't hard-code instructions
- Procedural micro-instructions will constrain the subagent and prevent adjustments that may be needed - should avoid this

Attribution
- Context-passing job
- E.g. if coordinator passes claims but strips source attribution, a downstream synthesis agent produces unsourced claims this is a context passing bug
- Must pass all soruces needed to the synthsis agent such as a structured finding containing its own attribution:
  - source_url, document_name, page_number, confidence, retrieved_by

Fork_session vs --resume mode
- fork_session
  - creates independant branches from a shared analysis baseline
  - each fork explores a divergent approach and cannot see of affect another
  - use this to compare approaches
- --resume
  - continues one specific named session - the same line of investigation
  - use this to continue work
- Parallel Agent Spwawning
  - concurrency within one line of work, not branching