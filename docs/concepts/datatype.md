## Types
### **datatype** `$tType` { #datatype data-toc-label='datatype' }
A precise information encoding that is taken as granted.
As the name suggests, the fundamental types of data considered.

!!! example
    - real number
    - uint8
    - pixel
###### Source: `fundamental-concepts.tff`

## ROS 2 Interface builtins
ROS 2 interfaces (messages, services, and actions) are
[formalisms](formalism.md) constructed from semantically named builtin
[datatypes](#datatype) and arrays of these builtins. See the ROS 2 
[documentation](https://docs.ros.org/en/rolling/Concepts/Basic/About-Interfaces.html)
for more details.

!!! important
    These individuals are not associated with a particular semantic label. The
    intention (WIP) is to match a particular [datatype](#datatype) (the
    `fieldtype`) and a [topic](topic.md) (the `fieldname`) in some
    [formalism](formalism.md) representing the ROS 2 interface.

### **'ROS2.msg.Bool'** [**`datatype`**](#datatype) { #ros2-msg-bool data-toc-label="'ROS2.msg.Bool'" }
The builtin `bool` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Byte'** [**`datatype`**](#datatype) { #ros2-msg-byte data-toc-label="'ROS2.msg.Byte'" }
The builtin `byte` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Char'** [**`datatype`**](#datatype) { #ros2-msg-char data-toc-label="'ROS2.msg.Char'" }
The builtin `char` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Float32'** [**`datatype`**](#datatype) { #ros2-msg-float32 data-toc-label="'ROS2.msg.Float32'" }
The builtin `float32` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Float64'** [**`datatype`**](#datatype) { #ros2-msg-float64 data-toc-label="'ROS2.msg.Float64'" }
The builtin `float64` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Int8'** [**`datatype`**](#datatype) { #ros2-msg-int8 data-toc-label="'ROS2.msg.Int8'" }
The builtin `int8` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Uint8'** [**`datatype`**](#datatype) { #ros2-msg-uint8 data-toc-label="'ROS2.msg.Uint8'" }
The builtin `uint8` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Int16'** [**`datatype`**](#datatype) { #ros2-msg-int16 data-toc-label="'ROS2.msg.Int16'" }
The builtin `int16` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Uint16'** [**`datatype`**](#datatype) { #ros2-msg-uint16 data-toc-label="'ROS2.msg.Uint16'" }
The builtin `uin16` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Int32'** [**`datatype`**](#datatype) { #ros2-msg-int32 data-toc-label="'ROS2.msg.Int32'" }
The builtin `int32` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Uint32'** [**`datatype`**](#datatype) { #ros2-msg-uint32 data-toc-label="'ROS2.msg.Uint32'" }
The builtin `uint32` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Int64'** [**`datatype`**](#datatype) { #ros2-msg-int64 data-toc-label="'ROS2.msg.Int64'" }
The builtin `int64` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.Uint64'** [**`datatype`**](#datatype) { #ros2-msg-uint64 data-toc-label="'ROS2.msg.Uint64'" }
The builtin `uint64` field type of a ROS 2 interface.
###### Source: `datatypes.tff`

### **'ROS2.msg.String'** [**`datatype`**](#datatype) { #ros2-msg-string data-toc-label="'ROS2.msg.String'" }
The builtin (unbounded) `string` field type of a ROS 2 interface.
These strings use 8-bit characters.
###### Source: `datatypes.tff`

### **'ROS2.msg.Wstring'** [**`datatype`**](#datatype) { #ros2-msg-wstring data-toc-label="'ROS2.msg.Wstring'" }
The builtin `wstring` field type of a ROS 2 interface.
These strings use 16-bit characters.
###### Source: `datatypes.tff`


## ROS 2 Interface arrays
ROS 2 interfaces support arrays of builtins, optionally with a fixed or bounded
size.
!!! warning
    Sizes of array datatypes are assumed to be natural numbers. This is **NOT**
    enforced by the type checker or logic.

### **'ROS2.msg.BoundedString'** `(`**`$int`**` > `[**`datatype`**](#datatype)`)` { #ros2-msg-bounded-string data-toc-label="'ROS2.msg.BoundedString'" }
A bounded `string<=n` field type of a ROS 2 interface.
`n` is a natural number.
###### Source: `datatypes.tff`

### **'ROS2.msg.UnboundedDynamicArray'** `(`[**`datatype`**](#datatype)` > `[**`datatype`**](#datatype)`)` { #ros2-msg-unbounded-dynamic-array data-toc-label="'ROS2.msg.UnboundedDynamicArray'" }
An array of any builtin with an unbouned size field type in a ROS 2 interface.
!!! example
    - `char[]`
    - `float32[]`
###### Source: `datatypes.tff`

### **'ROS2.msg.BoundedDynamicArray'** `((`[**`datatype`**](#datatype)` * `**`$int`**`) > `[**`datatype`**](#datatype)`)` { #ros2-msg-bounded-dynamic-array data-toc-label="'ROS2.msg.BoundedDynamicArray'" }
A dynamic array of any builtin with a bounded size field type in a ROS 2 interface.
The size must be a natural number.
!!! example
    - `char[<=5]`
    - `float32[<=4]`
###### Source: `datatypes.tff`

### **'ROS2.msg.StaticArray'** `((`[**`datatype`**](#datatype)` * `**`$int`**`) > `[**`datatype`**](#datatype)`)` { #ros2-msg-static-array data-toc-label="'ROS2.msg.StaticArray'" }
A static array of any builtin with a fixed size field type in a ROS 2 interface.
The size must be a natural number.
!!! example
    - `char[5]`
    - `float32[4]`
###### Source: `datatypes.tff`
