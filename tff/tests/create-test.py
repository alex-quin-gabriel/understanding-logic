#!/usr/bin/env python3

import sys
import argparse
import random



NUM_PHENOMENA=25#0
NUM_FORMALISMS=10#0
NUM_TEMPLATES=30#0 # has to be smaller than number of modelets
NUM_MODELETS=50#0 # has to be bigger than number of templates
NUM_PROPERTIES=30#0
#NUM_REQUIREMENTS=20
NUM_ENGINES=30#0
NUM_TEMPLATE_SETS=30#0

MAX_PROPERTIES = 20 # cannot be greater than NUM_PROPERTIES
MAX_TEMPLATES = 25 # cannot be greater than NUM_TEMPLATES
MAX_NUMBERS = 10

NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


USE_ROS_FORMALISMS = True
MAX_SIZES = 10
SIZES = ["size1", "size2", "size3", "size4", "size5", "size6", "size7", "size8", "size9", "size10"]


def create_phenomenons(n):
    output = "%%%  phenomena  %%% \n"
    for index in range(1, n+1):
        output += f"tff(phenomenon_{index}_decl, type, phenomenon_{index} : phenomenon).\n"
    output += "tff(all_phenomena, axiom,\n  ![P : phenomenon]:\n  (\n    "
    output += "\n    |\n    ".join([f"P = phenomenon_{index}" for index in range(1,n+1)])
    output += "\n  )\n).\n\n"
    return output


def create_formalisms(n):
    output = "%%%  formalisms  %%%\n"
    for index in range(1, n+1):
        output += f"tff(formalism_{index}_decl, type, formalism_{index} : formalism).\n"
    output += "tff(all_formalisms, axiom,\n  ![F : formalism]:\n  (\n    "
    output += "\n    |\n    ".join([f"F = formalism_{index}" for index in range(1,n+1)])
    output += "\n  )\n).\n\n"
    return output

def create_numbers():
    output = ""
    for n in range(MAX_NUMBERS):
        number = NUMBERS[n]
        output += f"tff({number}_decl, type, {number} : real).\n"
    return output

def create_sizes():
    output = ""
    for n in range(MAX_SIZES):
        size = SIZES[n]
        output += f"tff({size}_decl, type, {size} : size).\n"
    return output

def create_properties_and_requirements(n):
    output = "%%%  properties and requirements  %%%\n"
    for index in range(1, n+1):
        formalism = _get_random_formalism()
        v = random.randint(0, MAX_NUMBERS-1)
        output += f"tff(property_{index}_decl, type, prop_{index} : property).\n"
        output += f"tff(property_{index}_uses_formalism_decl, axiom,\n  type_of_p(prop_{index}) = {formalism}\n).\n"
        output += f"tff(property_{index}_has_value_{v}, axiom,\n  has_value(prop_{index}) = {NUMBERS[v]}\n).\n\n"

        output += f"tff(requirement_{index}_decl, type, req_{index} : requirement).\n"
        output += f"tff(requirement_{index}_uses_formalism_decl, axiom,\n  type_of_r(req_{index}) = {formalism}\n).\n"
        output += f"tff(requirement_{index}_has_permissible_value_{v}, axiom,\n  is_permissible(req_{index}, {NUMBERS[v]})\n).\n\n"
    output += "tff(all_props, axiom,\n  ![P : property]:\n  (\n    "
    output += "\n    |\n    ".join([f"P = prop_{index}" for index in range(1,n+1)])
    output += "\n  )\n).\n\n"
    output += "tff(all_reqs, axiom,\n  ![R : requirement]:\n  (\n    "
    output += "\n    |\n    ".join([f"R = req_{index}" for index in range(1,n+1)])
    output += "\n  )\n).\n\n"
    return output


def _get_random_formalism():
    if not USE_ROS_FORMALISMS:
        return f"formalism_{random.randint(1, NUM_FORMALISMS)}"

    assert(len(SIZES) > 0)

    builtins = [
                'Bool',
                'Byte',
                'Char',
                'Float32',
                'Float64',
                'Int8',
                'Uint8',
                'Int16',
                'Uint16',
                'Int32',
                'Uint32',
                'Int64',
                'Uint64',
                'String',
                'Wstring']
    arrays = [
              'BoundedString',
              'UnboundedDynamicArray',
              'BoundedDynamicArray',
              'StaticArray']
    namespace = 'ROS2.msg.'

    i = random.randint(0, len(builtins) + len(arrays) - 1)
    # i = random.randint(0, len(builtins) - 1) # only include the builtins
    if i >= len(builtins): # arrays
        a = i - len(builtins)
        b = random.randint(0, len(builtins) - 1)

        if a == 1: # UnboundedDynamicArray
            return f"'{namespace}{arrays[a]}'('{namespace}{builtins[b]}')"

        s = random.randint(0, len(SIZES) - 1)
        if a == 0: # BoundedString
            return f"'{namespace}{arrays[a]}'({SIZES[s]})"

        return f"'{namespace}{arrays[a]}'('{namespace}{builtins[b]}', {SIZES[s]})"

    return f"'{namespace}{builtins[i]}'"



#def create_requirement(n=20, formalism_count):
#    output = ""
#    for index in range(1, n+1):
#        m = randint(1,formalism_count)


def create_templates_and_modelets(num_templates, num_modelets, max_properties, property_count):
    output = "%%%  templates and modelets  %%%\n"

    for index in range(1, num_templates+1):
        template = ""
        modelet = ""
        phenomenon = random.randint(1, NUM_PHENOMENA)
        formalism = _get_random_formalism()
        modelet += f"tff(modelet_{index}_decl, type, modelet_{index} : modelet).\n"
        template += f"tff(template_{index}_decl, type, template_{index} : template).\n"
        properties = random.sample(range(1, property_count+1), random.randint(1, max_properties))
        for m in properties:
            modelet += f"tff(modelet_{index}_has_property_{m}, axiom,\n  is_property_of_m(prop_{m}, modelet_{index})\n).\n"
            template += f"tff(template_{index}_has_requirement_{m}, axiom,\n  is_part_of(req_{m}, template_{index})\n).\n"
        modelet += f"tff(modelet_{index}_of_phenomenon_{phenomenon}, axiom,\n  referent_of_m(modelet_{index}) = phenomenon_{phenomenon}\n).\n"
        modelet += f"tff(formalism_of_modelet_{index}, axiom,\n  formalism_of_m(modelet_{index}) = {formalism}\n).\n\n"
        #for m in random.sample(range(1, property_count+1), random.randint(1, max_requirements)):
        template += f"tff(template_{index}_of_phenomenon_{phenomenon}, axiom,\n  referent_of_t(template_{index}) = phenomenon_{phenomenon}\n).\n"
        template += f"tff(formalism_of_template_{index}, axiom,\n  formalism_of_t(template_{index}) = {formalism}\n).\n"
        template += f"tff(template_{index}_requirements, axiom,\n  ![R : requirement]:\n  (\n"
        template += f"    is_part_of(R, template_{index})\n    =>\n    (\n      "
        template += "\n      |\n      ".join([f"R = req_{m}" for m in properties])
        template += "\n    )\n  )\n).\n\n"
        output += modelet
        output += template
    for index in range(num_templates+1, num_modelets+1):
        phenomenon = random.randint(1, NUM_PHENOMENA)
        formalism = _get_random_formalism()
        output += f"tff(modelet_{index}_decl, type, modelet_{index} : modelet).\n"
        for m in random.sample(range(1, property_count+1), random.randint(1, max_properties)):
            output += f"tff(modelet_{index}_has_property_{m}, axiom,\n  is_property_of_m(prop_{m}, modelet_{index})\n).\n"
        output += f"tff(modelet_{index}_has_phenomenon_{phenomenon}, axiom,\n  referent_of_m(modelet_{index}) = phenomenon_{phenomenon}\n).\n"
        output += f"tff(formalism_of_modelet_{index}, axiom,\n  formalism_of_m(modelet_{index}) = {formalism}\n).\n\n"
    output += "tff(all_modelets, axiom,\n  ![M : modelet]:\n  (\n    "
    output += "\n    |\n    ".join([f"M = modelet_{index}" for index in range(1,num_modelets+1)])
    output += "\n  )\n).\n"
    output += "tff(all_templates, axiom,\n  ![T : template]:\n  (\n    "
    output += "\n    |\n    ".join([f"T = template_{index}" for index in range(1,num_templates+1)])
    output += "\n  )\n).\n\n"
    return output

    
def create_template_sets(n, max_templates, template_count):
    output = "%%%  template sets  %%%\n"
    for index in range(1, n+1):
        output += f"tff(template_set_{index}_decl, type, template_set_{index} : template_set).\n"
        
        templates = random.sample(range(1, template_count+1), random.randint(1, max_templates))
        for m in templates:
            output += f"tff(template_{m}_in_template_set_{index}, axiom,\n  in_set_t(template_{m}, template_set_{index})\n).\n\n"
        output += f"tff(template_set_{index}_templates, axiom,\n  ![T : template]:\n  (\n"
        output += f"    in_set_t(T, template_set_{index})\n    =>\n    (\n      "
        output += "\n      |\n      ".join([f"T = template_{t}" for t in templates])
        output += "\n    )\n  )\n).\n\n"
    output += "tff(all_template_sets, axiom,\n  ![TS : template_set]:\n  (\n    "
    output += "\n    |\n    ".join([f"TS = template_set_{index}" for index in range(1,n+1)])
    output += "\n  )\n).\n\n"
    return output


def create_engines(n, template_set_count, max_properties, property_count):
    output = "%%%  engines  %%%\n"
    for index in range(1, n+1):
        output += f"tff(engine_{index}_decl, type, engine_{index} : engine).\n"

        for m in random.sample(range(1, property_count+1), random.randint(1, max_properties)):
            output += f"tff(engine_{index}_has_property_{m}_decl, axiom,\n  is_property_of_e(prop_{m}, engine_{index})\n).\n"

        m = random.randint(1,template_set_count)
        output += f"tff(engine_{index}_uses_template_set_{m}_decl, axiom,\n  interface_of(engine_{index}) = template_set_{m}\n).\n\n"
    output += "tff(all_engines, axiom,\n  ![E : engine]:\n  (\n    "
    output += "\n    |\n    ".join([f"E = engine_{index}" for index in range(1,n+1)])
    output += "\n  )\n).\n\n"
    return output

#def create_modelets(n, max_properties, property_count):
#    output = ""
#    for index in range(1, n+1):
#        m = random.randint(1, NUM_REFERENTS)
#        m = random.randint(1, NUM_FORMALISM)
#    return output

def create_modelet_sets(n):
    output = "%%%  modelet sets  %%%\n"
    for index in range(1, n+1):
        modelets = []
        for index2 in range(1, index+1):
            modelets.append(f"M{index2}")
        output += f"tff(modelet_sets_of_size_{index}_exist, axiom,\n  !["
        output += ", ".join([f"{modelet}: modelet" for modelet in modelets])
        output += "]:\n    ?[MS: modelet_set]:\n    (\n      "
        output += "\n      &\n      ".join([f"in_set_m({modelet}, MS)" for modelet in modelets])
        output += "\n    )  \n).\n\n"
    output += "\n%%%  conjectures   %%%"
    return output


def create_formally_equivalent_test():
    return "\n%tff(conjecture_formally_equivalent, conjecture,\n%  ?[T: template, M: modelet]: formally_equivalent(T, M)).\n"

def create_inputs_match_test():
    return "\n%tff(conjecture_inputs_match, conjecture,\n%  ?[M: modelet, T: template]: inputs_match(M, T)).\n"

def create_interfaces_match_test():
    return "\n%tff(conjecture_interfaces_match, conjecture,\n%  ?[TS: template_set, MS: modelet_set]: interfaces_match(MS, TS)).\n"

def create_interfaces_match_1_test():
    return "\n%tff(conjecture_interfaces_1_match, conjecture,\n%  ?[MS: modelet_set]: interfaces_match(MS, template_set_1)).\n"

def create_is_interface_of_test():
    return "\n%tff(conjecture_is_interface_of, conjecture,\n%  ?[TS: template_set, E: engine]: is_interface_of(TS, E)).\n"

def create_exertable_test():
    return "\ntff(conjecture_exertable, conjecture,\n  ?[E: engine, MS: modelet_set]: exertable(MS, E)).\n"

def create_exertable_1_test():
    return "\n%tff(conjecture_exertable_1, conjecture,\n%  ?[MS: modelet_set]: exertable(MS, engine_1)).\n"


def main() -> int:
    output = "include('understanding-logic/tff/model/properties.tff').\n\n"
    if USE_ROS_FORMALISMS:
        output += "include('understanding-logic/tff/model/ros-message-formalisms.tff').\n\n"
        output += create_sizes()
    output += create_numbers()
    output += create_phenomenons(NUM_PHENOMENA)
    if not USE_ROS_FORMALISMS:
        output += create_formalisms(NUM_FORMALISMS)
    output += create_properties_and_requirements(NUM_PROPERTIES)
    output += create_templates_and_modelets(NUM_TEMPLATES, NUM_MODELETS, MAX_PROPERTIES, NUM_PROPERTIES)
    output += create_template_sets(NUM_TEMPLATE_SETS, MAX_TEMPLATES, NUM_TEMPLATES)
    #output += create_modelets(NUM_MODELETS, MAX_PROPERTIES, NUM_PROPERTIES)
    output += create_engines(NUM_ENGINES, NUM_TEMPLATE_SETS, MAX_PROPERTIES, NUM_PROPERTIES)
    output += create_modelet_sets(MAX_TEMPLATES)

    print(output)
    return 0


if  __name__ == "__main__":
    sys.exit(main())
