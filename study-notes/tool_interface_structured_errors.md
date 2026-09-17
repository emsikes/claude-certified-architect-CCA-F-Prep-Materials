Five element description checklist
    1. What the tool does
       - Be as desscriptive as possible
    2. Inputs
       - Data types, formats, constraints, required vs optional
    3. Example queries it handles well
    4. Edge cases and limitations
        - What it does not do, out of range behavior
    5. Explicit boundaries against sibling tools

Ranking fixes for misrouting (best options are simple and high leveraged)
    1. First expand descriptions
        - Low effort, high leverage, addresses root cause
    2. Few shot examples
        - Use with caution, adds token overhead, treats symptoms
    4. Routing classifier
        - Typically over-engineered, bypasses model's language understanding
    6. Tool consolidation
        - Valid long-term, but too much effort as a first step

Renaming system prompt conflicts
    1. Renaming
        - Renaming a tool (e.g. analyze_content --> extract_web_results) with a web-specific
          description removes functional overlap without touching the implementation
    2. System prompt keyword conflicts
        - Instructions like 'always check customer details before proceeding' 
          can pull every customer related query toward get_customer, overriding
          even good descriptions.  After updating descriptions, re-review the system
          prompt for keyword conflicts.

MCP isError flag, retryable nuances, access failure vs empty result, error propogation
    - Structured errors are grounded in the MCP protocol's isError boolean.  Setting isError: true
      tells the model that execution failed, so it reasons about recovery instad of treating
      error text as normal results.
      1. errorCategory - Classifies the type of failure
      2. isRetryable - Signals whether any retry path exists (e.g. fix validation errors, transient errors)
      3. description - human readable explanation

Error propogation in multi-agent systems
    1. Subagents retry transient failures locally
    2. Only resolvable errors propogate upward
    3. Propogated reports include partial rules and what was attempted
    
    * anti-patters that will blind the coordinator
    - silently returning empty as success
    - terminating an entire workflow on one failure