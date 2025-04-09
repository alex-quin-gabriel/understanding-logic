## Types
### **modelet** `$tType` { #modelet data-toc-label='modelet' }
Models a [phenomenon](phenomenon.md) as the *thought* in the triangle of meaning.
All modelets describe a [topic](topic.md), have an [origin](origin.md), and are
modeled in a specific [formalism](formalism.md).

- [**Topic**](topic.md): the *referent* of the [modelet](#modelet)
- [**Origin**](origin.md): the agent's perspective on the *referent*
- [**Formalism**](formalism.md): the representation of the *referent*
###### Source: `engines-and-modelets.tff`

### **modelet_set** `$tType` { #modelet_set data-toc-label='modelet_set' }
Some particular set of [modelets](#modelet) which the has reasoner assembled.
Used to collect the inputs to an [engine](engine.md).
!!! example
    - {m1, m2, m3}
    - {m2}
    - {}
###### Source: `engines-and-modelets.tff`


## Relations
### **topic_of_modelet** `(`[**`modelet`**](#modelet)` > `[**`phenomenon`**](phenomenon.md)`)` { #topic_of_modelet data-toc-label='topic_of_modelet' }
The [phenomenon](phenomenon.md) symbolizing the *referent* of a [modelet](modelet.md).
!!! question "TODO"
    rename from 'topic' to something else.
!!! question "TODO"
    Should we call this the intrinsic purpose? (as opposed to the [`role`](role.md)).
###### Source: `engines-and-modelets.tff`

### **formalism_of_modelet** `(`[**`modelet`**](#modelet)` > `[**`formalism`**](formalism.md)`)` { #formalism_of_modelet data-toc-label='formalism_of_modelet' }
The [formalism](formalism.md) used by a [modelet](#modelet) to describe the *referent*.
###### Source: `engines-and-modelets.tff`

### **modelet_creation_date** `(`[**`modelet`**](#modelet)` > `**`$real`**`)` { #modelet_creation_date data-toc-label='modelet_creation_date' }
The date a [modelet](#modelet) was created.
!!! question "TODO"
    The date is represented as a `$real` but we don't make any assumptions about
    what that number represents. Unix time? time since last restart? seconds?
    This may be solved by integration with `spacetime_point`.
###### Source: `engines-and-modelets.tff`

### **modelet_location** `(`[**`modelet`**](#modelet)` > `[**`spacetime_point`**](spacetime_point.md)`)` { #modelet_location data-toc-label='modelet_location' }
The time and spatial location a [modelet](#modelet) refers to.
[Modelets](modelet.md) may have a specific temporal scope or make an observation
at a specific [`spacetime_point`](spacetime_point.md).
###### Source: `engines-and-modelets.tff`

### **modelet_extent** `(`[**`modelet`**](#modelet)` > `[**`extent`**](extent.md)`)` { #modelet_extent data-toc-label='modelet_extent' }
The time and spatial [extent](extent.md) a [modelet](#modelet) refers to.
[Modelets](#modelet) may have an area/volume/duration of reference.
###### Source: `engines-and-modelets.tff`

### **role_of_modelet** `(`[**`modelet`**](#modelet)` > `[**`role`**](role.md)`)` { #role_of_modelet data-toc-label='role_of_modelet' }
The [role](role.md) a [modelet](#modelet) plays when used by an [engine](engine.md).
!!! question "TODO"
    This looks like it will turn out to be HOL.
###### Source: `engines-and-modelets.tff`


### **is_in_modelet_set** `((`[**`modelet`**](#modelet)` * `[**`modelet_set`**](#modelet_set)`) > `**`$o`**`)` { #is_in_modelet_set data-toc-label='is_in_modelet_set' }
Check if a [modelet](#modelet) is a member of a [modelet_set](#modelet_set).
###### Source: `engines-and-modelets.tff`
