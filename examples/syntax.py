## A small Python snippet with syntax highlighting ##
from encolor import sub

code = """def foo(bar):
    return bar

print(foo("baz"))
"""

rules_str = "{def|return: red, \(|\): gray, \".*\": green, \w+(?=\(.*\)): yellow}"
rules = sub.parse_rules(rules_str)

print(sub.substitute(code, rules))
