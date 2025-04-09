## Types
### **engine** `$tType` { #engine data-toc-label='engine' }
Does work within a **CoreSense** [agent](agent.md) to consume and/or produce [modelets](modelet.md).

- Takes multiple [modelets](modelet.md) as an input [modelet_set](modelet.md#modelet_set)
- Uses semantic information to identify valid input modelet [formalisms](formalism.md)
    - semantics could be external (part of the type definition) or internal
      (modeled within the [modelet](modelet.md) itself)
- Produces one output [modelet](modelet.md)
	- May or may not impart semantic meaning to the output [modelet](modelet.md)
    - May (re)define the output modelet [origin](origin.md), [topic](topic.md),
      or characteristics
- Has [exertion](exertion.md) characteristics
	- e.g. time delay, resource usage, power consumption

!!! example
    - PersonLocatorNode
    - Planner
    - Min function
###### Source: `engines-and-modelets.tff`

## Relations
### **interface_of** `(`[**`engine`**](#engine)` > `[**`template_set`**](template.md#template_set)`)` { #interface_of data-toc-label='interface_of' }
An [engine](#engine) requires a set of input [modelets](modelet.md) which
matches the [template_set](template.md#template_set).
###### Source: `engines-and-modelets.tff`

### **output_modelet_formalism** `(`[**`engine`**](#engine)` > `[**`formalism`**](formalism.md)`)` { #output_modelet_formalism data-toc-label='output_modelet_formalism' }
The [formalism](formalism.md) of an [engine](#engine) output [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`

### **output_modelet_topic** `(`[**`engine`**](#engine)` > `[**`phenomenon`**](phenomenon.md)`)` { #output_modelet_topic data-toc-label='output_modelet_topic' }
The [topic](topic.md) of an [engine](#engine) output [modelet](modelet.md).
!!! question "TODO"
    `topic` will soon be renamed. Right now this outputs a `phenomenon_class`.
###### Source: `engines-and-modelets.tff`

### **output_property_of_engine** `(`[**`engine`**](#engine)` > `[**`property`**](property.md)`)` { #output_property_of_e data-toc-label='output_property_of_e' }
The [property](property.md) an [engine](#engine) imparts on its output [modelet](modelet.md).
###### Source: `properties.tff`


### **engine_imparts_role** `(`[**`engine`**](#engine)` > `[**`role`**](role.md)`)` { #engine_imparts_role data-toc-label='engine_imparts_role' }
The [role](role.md) an [engine](#engine) imparts on its output [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`
