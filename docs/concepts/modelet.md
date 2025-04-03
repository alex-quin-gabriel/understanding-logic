## Types
### **modelet** `$tType` { #modelet data-toc-label='modelet' }
Models a [phenomenon](phenomenon.md) as the *thought* in the triangle of meaning.
All modelets describe a [topic](topic.md), have an [origin](origin.md), and are
modeled in a specific [format](format.md).

- [**Topic**](topic.md): the *referent* of the [modelet](#modelet)
- [**Origin**](origin.md): the agent's perspective on the *referent*
- [**Format**](format.md): the representation of the *referent*
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
### **referent_of_m** `(`[**`modelet`**](#modelet)` > `[**`phenomenon`**](phenomenon.md)`)` { #referent_of_m data-toc-label='referent_of_m' }
The [phenomenon](phenomenon.md) naming the *referent* of a [modelet](modelet.md).
###### Source: `engines-and-modelets.tff`

### **formalism_of_m** `(`[**`modelet`**](#modelet)` > `[**`formalism`**](formalism.md)`)` { #formalism_of_m data-toc-label='formalism_of_m' }
The [formalism](formalism.md) used by a [modelet](#modelet) to describe the *referent*.
###### Source: `engines-and-modelets.tff`

### **in_set_m** `((`[**`modelet`**](#modelet)` * `[**`modelet_set`**](#modelet_set)`) > `**`$o`**`)` { #in_set_m data-toc-label='in_set_m' }
Check if a [modelet](#modelet) is a member of a [modelet_set](modelet.md#modelet_set).
###### Source: `engines-and-modelets.tff`
