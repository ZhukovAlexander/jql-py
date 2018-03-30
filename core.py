

class Issue:
    pass

EQUALS = '='


class Expression:

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __and__(self, other):
        print(self)
        return Expression(self, 'AND', other)

    def __or__(self, other):
        return Expression(self, 'OR', other)

    def __add__(self, other):
        return Expression(self, 'AND', other)

    def __str__(self):
        return '{} {} {}'.format(self.left, self.op, self.right)

    def ORDER_BY(self, field, direction):
        return '{} ORDER BY {} {}'.format(self, field, direction)



class Field:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return Expression(self.id, EQUALS, other)

    def __ne__(self, other):
        return Expression(self.id, '!=', other)

    def __str__(self):
        return str(self.id)


def IN(f, *items):
    return Expression(f, 'IN', tuple(items))


def NOT_IN(f, *items):
    return Expression(f, 'NOT IN', tuple(items))


def WAS_IN(f, *items):
    return Expression(f, 'WAS IN', tuple(items))


def WAS_NOT_IN(f, *items):
    return Expression(f, 'WAS NOT IN', tuple(items))



if __name__ == '__main__':
    expr = (Field('1') == 1) & (Field('2') == 2) | (Field('bar') != 1) & NOT_IN(Field('d'), 1, 2) | IN(Field('f'), 'f', 'f').ORDER_BY('foo', 'DESC')
    print(expr)
