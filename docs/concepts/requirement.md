## Types
### **requirement** `$tType` { #requirement data-toc-label='requirement' }
A restriction on the [property](property.md) values that a [template](template.md) may enforce on a [modelet](modelet.md).
###### Source: `properties.tff`

## Relations
### **type_of_r** `(`[**`requirement`**](#requirement)` > `[**`formalism`**](formalism.md)`)` { #type_of_r data-toc-label='type_of_r' }
The [formalism](formalism.md) of a certain [requirement](#requirement).
###### Source: `properties.tff`

### **is_permissible** `((`[**`requirement`**](#requirement)` * `[**`real`**](real.md)`) > `**`$o`**`)` { #is_permissible data-toc-label='is_permissible' }
Check if a value is *permissible* under a certain [requirement](#requirement).
###### Source: `properties.tff`

### **is_part_of** `((`[**`requirement`**](#requirement)` * `[**`template`**](template.md)`) > `**`$o`**`)` { $is_part_of data-toc-label='is_part_of' }
Check if a [requirement](#requirement) is part of a [template](template.md).
###### Source: `properties.tff`
