

'''
Задание 1

Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

Алгоритм:
Дана строка s длины n, в которой мы хотим найти все вхождения строки t длины m.
Найдем хеш строки t (всей строки целиком).
Найдем хеши всех префиксов строки s.
Будем двигаться по строке s окном длины m, сравнивая подстроки s(i...i+m-1).

'''


def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            return i
    return -1

s = 'hello car'
t = 'car'

print (rabin_karp(s, t))


# Задание 2. Закодировать любую строку из трех слов по алгоритму Хаффмана.

string = input('Введите три любвые слова')

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

def huffmanCodeTree(node, left=True, binString=""):
    if type(node) is str:
        return { node: binString }
    l, r = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, binString + "0"))
    d.update(huffmanCodeTree(r, False, binString + "1"))
    return d

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq

while len(nodes) > 1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffmanCodeTree(nodes[0][0])

print("Исходная строка:", string)
print("Закодированная строка: ", end="")
for c in string:
    print(huffmanCode[c], "", end="")
print()
