1. Reliability Hierarchy
   1. tool_use + JSON Schema
      1. Removes JSON syntax errors - no missing brackets, trailing commas, or unquoted keys
   2. Prompt-based JSON "works often"
      1. "Return only valid JSON" - gives no structural guarantee and will periodically produce unparseable output


2. tool_choice has three modes 
      1. Use "any" when you expose several schemas and the document type is unkown
      2. This guarantees a structured call while letting Claude pick the right schema
         1. tool_choice={"type: "auto"}                     - may reply in text
         2. tool_choice={"type": "any"}                     - must call a tool
         3. tool_choice={"type: "tool", "name":, "my_tool"} - must call this specific tool
   
3. Semantic Errors
   1. A valid schema fixes shape, but not meaning.  These failures classes survive it
      1. Sum descrepencies
         1. Line items that don't add up to the stated total
      2. Field placement errors
         1. A value dropped into the wrong same-typed field
      3. Fabrication
         1. Inventing a required field when source data is absent - defend this with output/nullable fields