# Concepts
!!! danger
    These concepts are still in development and high susceptible to change.
    Use the provided terms, definitions, and types with caution.

The **Understanding System** (a.k.a Understanding Core) is a CoreSense module
for generating understanding within a *CoreSense* agent.
The main idea is to:
!!! quote "Intuition"
    Find *sequences* of **Engine** *exertions* to **create** required **Modelets**
    Source: Alex' presentation

!!! question "TODO"
    Add a map of the conepts or something more elegant here...
    We should also include the triangle of meaning.

## Types
### [**agent**](agent.md)
--8<-- "docs/concepts/agent.md:3:3"

### [**engine**](engine.md)
--8<-- "docs/concepts/engine.md:3:3"

### [**formalism**](formalism.md)
--8<-- "docs/concepts/formalism.md:3:3"

### [**format**](format.md)
--8<-- "docs/concepts/format.md:3:3"

### [**modelet**](modelet.md)
--8<-- "docs/concepts/engine.md:3:3"

### [**modelet_set**](modelet_set.md)
--8<-- "docs/concepts/modelet.md:13:13"

### [**origin**](origin.md)
--8<-- "docs/concepts/origin.md:3:3"

### [**phenomenon**](phenomenon.md)
--8<-- "docs/concepts/phenomenon.md:3:3"

### [**property**](property.md)
--8<-- "docs/concepts/property.md:3:3"

### [**real**](real.md)
--8<-- "docs/concepts/real.md:3:3"

### [**requirement**](requirement.md)
--8<-- "docs/concepts/requirement.md:3:3"

### [**sequence**](sequence.md)
--8<-- "docs/concepts/sequence.md:3:3"

### [**template**](template.md)
--8<-- "docs/concepts/template.md:3:3"

### [**template_set**](template_set.md)
--8<-- "docs/concepts/template.md:10:10"

### [**topic**](topic.md)
--8<-- "docs/concepts/topic.md:3:3"


## Relations
### **inputs_match** `((`[**`modelet`**](modelet.md)` * `[**`template`**](template.md)`) > `**`$o`*`)` { #inputs_match data-toc-label='inputs_match' }
Check if a [modelet](modelet.md) matches a [template](template.md).

- Check if they are [formally equivalent](#formally_equivalent)
- Check if the [modelet](modelet.md) contains *permissible* values for each of
  the [properties](property.md) of [requirements](requirement.md) of the [template](template.md).
###### Source: `engines-and-modelets.tff`, `properties.tff`

### **formally_equivalent** `((`[**`template`**](template.md)` * `[**`modelet`**](modelet.md)`) > `**`$o`**`)` { #formally_equivalent data-toc-label='formally_equivalent' }
A [template](template.md) and a [modelet](modelet.md) share the same *referent* and [formalism](formalism.md).
###### Source: `properties.tff`


### **exert** `((`[**`engine`**](engine.md)` * `[**`modelet_set`**](modelet.md#modelet_set)` * `[**`modelet`**](modelet.md)`) > `**`$o`**`)` { #exert data-toc-label='exert' }
Exert an [engine](engine) on a [modelet_set](modelet.md#modelet_set) to produce and output [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`

### **interfaces_match** `((`[**`modelet_set`**](modelet.md#modelet_set)` * `[**`template_set`**](template.md#template_set)`) > `**`$o`**`)` { #interfaces_match data-toc-label='interfaces_match' }
Check if all of the [templates](template.md) in the [template_set](template.md#template_set) have a corresponding [modelet](modelet.md) in the [modelet_set](modelet.md#modelet_set) with matching profile.

- Check if they are [formally equivalent](#formally_equivalent)
- Check if their [inputs match](#inputs_match)
###### Source: `engines-and-modelets.tff`, `properties.tff`

### **exertable** `((`[**`modelet_set`**](modelet.md#modelet_set)` * `[**`engine`**](engine.md)`) > `**`$o`**`)` { #exertable data-toc-label='exertable' }
A [modelet_set](modelet.md#modelet_set) can be exerted by an [engine](engine.md) iff their [interfaces match](#interfaces_match).
###### Source: `engines-and-modelets.tff`

