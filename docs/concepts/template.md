## Types
### **template** `$tType` { #template data-toc-label='template' }
Describes the features that a single [modelet](modelet.md) should have for an [engine](engine.md) to accept it as input.

- a semantic function signature
- [properties](property.md) and [requirements](requirement.md) of [modelets](modelet.md)
###### Source: `engines-and-modelets.tff`

### **template_set** `$tType` { #template_set data-toc-label='template_set' }
Some particular set of [templates](#template) which describe the inputs to an [engine](engine.md).
!!! example
    - {t1, t2, t3}
    - {t2}
    - {}
###### Source: `engines-and-modelets.tff`


## Relations
### **referent_of_t** `(`[**`template`**](#template)` > `[**`phenomenon`**](phenomenon.md)`)` { #referent_of_t data-toc-label='referent_of_t' }
The [phenomenon](phenomenon.md) symbolizing the *referent* of a [template](#template).
###### Source: `engines-and-modelets.tff`

### **formalism_of_t** `(`[**`template`**](#template)` > `[**`formalism`**](formalism.md)`)` { #formalism_of_t data-toc-label='formalism_of_t' }
The [formalism](formalism.md) this [template](#template) expects the *referent* to be described by.
###### Source: `engines-and-modelets.tff`

### **in_set_t** `((`[**`template`**](#template)` * `[**`template_set`**](#template_set)`) > `**`$o`**`)` { #in_set_t data-toc-label='in_set_t' }
Check if a [template](#template) is a member of a [template_set](#template_set).
###### Source: `engines-and-modelets.tff`
