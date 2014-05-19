# Consider me solving this for you your birthday present ;)
# Erika x

# Initial variables
jakew = 'Jake Whiteman'
supermysteriouscode = '^>>>>>>.>>>>>.]]]<..[<<<<<-.[[<.^]<<<.[!>>>>.[[<.]].>>.<<<[.<<].!>>>>]]-.\,[[<./.>.>.>.\!\!\!'


class Parser(object):

        def __init__(self, code, phrase):
                self.code = code
                self.phrase = phrase
                self.position = 0
                self.char_push = 0
                self.result = ''
                self.escape = False
                self.upper = False
                self.lower = False
                self.instructions = {
                        '>': self.right,
                        '<': self.left,
                        ']': self.push_right,
                        '[': self.push_left,
                        '/': self.reset,
                        '\\': self._escape,
                        '-': self._lower,
                        '^': self._upper,
                        '.': self.select,
                        '!': self.reverse,
                }

        def run(self):
                for ch in self.code:
                        if self.escape:
                                self.result += ch
                                self.escape = False
                        else:
                                self.instructions[ch]()
                return self.result

        def right(self):
                self.position += 1

        def left(self):
                self.position -= 1

        def push_left(self):
                self.char_push -= 1

        def push_right(self):
                self.char_push += 1

        def reset(self):
                self.position = 0

        def _escape(self):
                self.escape = True

        def _upper(self):
                self.upper = True
                self.lower = False

        def _lower(self):
                self.lower = True
                self.upper = False

        def reverse(self):
                self.phrase = self.phrase[::-1]

        def select(self):
                curchar = chr(ord(self.phrase[self.position]) + self.char_push)
                if self.upper:
                        self.result += curchar.upper()
                elif self.lower:
                        self.result += curchar.lower()
                else:
                        self.result += curchar
                self.upper = False
                self.lower = False


if __name__ == '__main__':
        print(Parser(supermysteriouscode, jakew).run())
