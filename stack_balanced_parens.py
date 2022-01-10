

from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        retun True

        elif p1 == "{" and p2 == "}":
            retun True

            elif p1 == "[" and p2 == "]":
                retun True

                else:
                    False

def is_paren_balanced (paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
    if paren in "([{" :
        s.push(paren)
    else:
        if s.is_empty():
            is_balanced = false
        else:
            top = s.pop()
            if not is_match(top, paren)
            is_balanced = false
    index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        retun False




        print(is_paren_balanced("()"))
