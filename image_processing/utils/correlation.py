from itertools import zip_longest

def rowDivider(image, n): #separa as linhas da imagem de acordo com o numero de linhas (m).
    c = []
    imageCopy = image.copy()
    while len(imageCopy) > n-1:
        c.append(imageCopy[:n])
        imageCopy.pop(0)
    return c

def columnDivider(a,m): #separa as colunas da imagem de acordo com o numero de colunas (n).
    return rowDivider([i for i in range(len(a))], m)

def windowMaker(a,b):#Obtem os elementos para aplicação dos filtros sem extensão por zeros.
    c = []
    for elem in b:
        d = []
        for i in elem:
            d.append(a[i])
        e = [list(a) for a in zip(*d)]
        for j in e:
            c.append(j)
    return c

def grouper(iterable, n, fillvalue=None): #https://docs.python.org/3/library/itertools.html#itertools-recipes
    """Collect data into fixed-length chunks or blocks.

    >>> grouper('ABCDEFG', 3, 'x')
    ['ABC', 'DEF', 'Gxx']
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
