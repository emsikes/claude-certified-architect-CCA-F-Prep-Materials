Common mistakes that cause the loop to terminate early:
    1. checking response.content[0].type == "text to detect completion
       - Claude can return explanatory text alongside a tool_use block, so having some text at position [0] does not mean the model is finished
       - The authoritative completion signal is always the stop_reason - always check this.  It is never the shape or order of content blocks
    2. forcing the tool_choice to "any" to prevent the model from replying in plain text
       - forcing a tool call even when the agent is genuinely done can potentially create an infinite loop
       - instead let the model signal completion naturally through end_turn
Key terms:
    1. Model-driven decision-making
       - this is the correct name for the agent loop patter
       - different from pre-configured decision trees and fixed tool sequences (what the loop replaces)
       - watch for questions describing hard wired tool order = the decision tree patter, not model-driven flow
       - programatic enforcement overrides the models freedom in cases of financial, security, or compliance scenarios 