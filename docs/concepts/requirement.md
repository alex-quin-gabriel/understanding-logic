## Types
### **requirement** `$tType` { #requirement data-toc-label='requirement' }
A restriction on the [property](property.md) values that a [template](template.md) may enforce on a [modelet](modelet.md).
###### Source: `properties.tff`

## Relations
### **datatype_of_requirement** `(`[**`requirement`**](#requirement)` > `[**`datatype`**](datatype.md)`)` { #datatype_of_p data-toc-label='datatype_of_p' }
The [datatype](datatype.md) of a certain [requirement](#requirement).
###### Source: `properties.tff`

### **is_permissible** `((`[**`requirement`**](#requirement)` * `**`$real`**`) > `**`$o`**`)` { #is_permissible data-toc-label='is_permissible' }
Check if a value is *permissible* under a certain [requirement](#requirement).
###### Source: `properties.tff`

### **is_part_of** `((`[**`requirement`**](#requirement)` * `[**`template`**](template.md)`) > `**`$o`**`)` { $is_part_of data-toc-label='is_part_of' }
Check if a [requirement](#requirement) is part of a [template](template.md).
###### Source: `properties.tff`
