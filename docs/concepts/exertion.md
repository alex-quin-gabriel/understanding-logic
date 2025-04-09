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

### **interfaces_match** `((`[**`modelet_set`**](modelet.md#modelet_set)` * `[**`template_set`**](template.md#template_set)`) > `**`$o`**`)` { #interfaces_match data-toc-label='interfaces_match' }
Check if all of the [templates](template.md) in the [template_set](template.md#template_set) have a corresponding [modelet](modelet.md) in the [modelet_set](modelet.md#modelet_set) with matching profile.

- Check if they are [formally equivalent](#formally_equivalent)
- Check if their [inputs match](#inputs_match)
###### Source: `engines-and-modelets.tff`, `properties.tff`

### **exert** `((`[**`engine`**](engine.md)` * `[**`modelet_set`**](modelet.md#modelet_set)` * `[**`modelet`**](modelet.md)`) > `**`$o`**`)` { #exert data-toc-label='exert' }
Exert an [engine](engine.md) on a [modelet_set](modelet.md#modelet_set) to produce and output [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`

### **exertable** `((`[**`modelet_set`**](modelet.md#modelet_set)` * `[**`engine`**](engine.md)`) > `**`$o`**`)` { #exertable data-toc-label='exertable' }
A [modelet_set](modelet.md#modelet_set) can be exerted by an [engine](engine.md) iff their [interfaces match](#interfaces_match).
###### Source: `engines-and-modelets.tff`

<!--
### **exertion** `((`[**`engine`**](engine.md)` * `[**`modelet_set`**](modelet.md#modelet_set)` * `[**`modelet`**](modelet.md#modelet)` * `[**`modelet_set`**](modelet.md#modelet_set)`) > `[**`modelet_set`**](modelet.md#modelet_set)`)`
The act of exerting an [engine](engine.md) on a
[modelet_set](modelet.md#modelet_set), resulting in a [modelet](modelet.md), in
defined state of knowledge, resulting in the addition of the output modelet to
that state of
knowledge. 
###### Source: `understanding-calculus.tff`
-->
