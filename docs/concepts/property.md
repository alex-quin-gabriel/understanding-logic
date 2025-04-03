## Types
### **property** `$tType` { #phenomenon data-toc-label='phenomenon' }
A specific characteristic of a [modelet](modelet.md) or [engine](engine.md).
Multiple things can exhibit the same [property](#property).

!!! example
    - color: red
    - age: 14 years
###### Source: `properties.tff`

## Relations
### **has_value** `(`[**`property`**](#property)` > `[**`real`**](real.md)`)` { #has_value data-toc-label='has_value' }
The value of a certain [property](#property).
###### Source: `properties.tff`

### **type_of_p** `(`[**`property`**](#property)` > `[**`formalism`**](formalism.md)`)` { #type_of_p data-toc-label='type_of_p' }
The [formalism](formalism.md) of a certain [property](#property).
###### Source: `properties.tff`

### **is_property_of_m** `((`[**`property`**](#property)` * `[**`modelet`**](modelet.md)`) > `**`$o`**`)` { #is_property_of_m data-toc-label='is_property_of_m' }
Check if a [modelet](modelet.md) is described by a certain [property](#property).
###### Source: `properties.tff`

### **is_property_of_e** `((`[**`property`**](#property)` * `[**`engine`**](engine.md)`) > `**`$o`**`)` { #is_property_of_e data-toc-label='is_property_of_e' }
Check if an [engine](engine.md) is described by a certain [property](#property).
###### Source: `properties.tff`
