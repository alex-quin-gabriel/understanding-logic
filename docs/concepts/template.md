## Types
### **template** `$tType` { #template data-toc-label='template' }
Describes the features that a single [modelet](modelet.md) should have for an
[engine](engine.md) to accept it as input.

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
### **topic_of_template** `(`[**`template`**](#template)` > `[**`phenomenon`**](phenomenon.md)`)` { #topic_of_template data-toc-label='topic_of_template' }
The [phenomenon](phenomenon.md) symbolizing the *referent* of a [template](template.md).
!!! question "TODO"
    rename from 'topic' to something else.
!!! question "TODO"
    Should we call this the intrinsic purpose? (as opposed to the [`role`](role.md)).
###### Source: `engines-and-modelets.tff`

### **formalism_of_template** `(`[**`template`**](#template)` > `[**`formalism`**](formalism.md)`)` { #formalism_of_template data-toc-label='formalism_of_template' }
The [formalism](formalism.md) this [template](#template) expects the *referent*
to be described by.
###### Source: `engines-and-templates.tff`

### **template_location** `(`[**`template`**](#template)` > `[**`spacetime_point`**](spacetime_point.md)`)` { #template_location data-toc-label='template_location' }
The time and spatial location a [template](#template) refers to.
A [template](template.md) may have a specific temporal scope or expect an observation
at a specific [`spacetime_point`](spacetime_point.md).
###### Source: `engines-and-modelets.tff`

### **template_extent** `(`[**`template`**](#template)` > `[**`extent`**](extent.md)`)` { #template_extent data-toc-label='template_extent' }
The time and spatial [extent](extent.md) a [template](#template) covers.
A [template](#template) may expect an area/volume/duration of reference.
###### Source: `engines-and-modelets.tff`

### **role_of_template** `(`[**`template`**](#template)` > `[**`role`**](role.md)`)` { #role_of_template data-toc-label='role_of_template' }
The [role](role.md) a [template](#template) requires a [modelet](modelet.md) to
play when used by an [engine](engine.md).
!!! question "TODO"
    This looks like it will turn out to be HOL.
###### Source: `engines-and-modelets.tff`

### **is_in_template_set** `((`[**`template`**](#template)` * `[**`template_set`**](#template_set)`) > `**`$o`**`)` { #is_in_template_set data-toc-label='is_in_template_set' }
Check if a [template](#template) is a member of a [template_set](#template_set).
###### Source: `engines-and-modelets.tff`
