# leet translator from leet to regular alpha

leet_dict = {
    'a': '@',
    'b': '8',
    'c': '<',
    'e': '3',
    'g': '9',
    'i': '1',
    'j': ';',
    'l': 'L',
    'o': '0',
    's': '$',
    't': '7',
    'A': '@',
    'B': '8',
    'C': '<',
    'E': '3',
    'G': '9',
    'I': '1',
    'J': ';',
    'O': '0',
    'S': '$',
    'T': '7',
}

ascii_dict = {
    'a': ' /\\',
    'b': ' I3',
    'c': ' <',
    'd': ' |)',
    'e': ' 3',
    'f': ' /=',
    'g': ' 9',
    'h': ' |-|',
    'i': ' ][',
    'j': ' ._]',
    'k': ' |<',
    'l': ' |_',
    'm': ' /V\\',
    'n': ' |\|',
    'o': ' ()',
    'p': ' |o',
    'q': ' ()_',
    'r': ' I2',
    's': ' $',
    't': ' +',
    'u': ' (_)',
    'v': ' \/',
    'w': ' \/\/',
    'x': ' }{',
    'y': ' `/',
    'z': ' -/_',
}

ascii_leet = {
    '4': 'a',
    '/\\': 'a',
    '@': 'a',
    '/-\\': 'a',
    '^': 'a',
    '(L': 'a',
    'I3': 'b',
    '8': 'b',
    '13': 'b',
    '|3': 'b',
    '!3': 'b',
    '(3': 'b',
    '/3': 'b',
    ')3': 'b',
    '|-]': 'b',
    'j3': 'b',
    '6': 'b',
    '[': 'c',
    '{': 'c',
    '<': 'c',
    '(': 'c',
    ')': 'd',
    '|)': 'd',
    '(|': 'd',
    '[)': 'd',
    'I>': 'd',
    '?': 'd',
    'T)': 'd',
    'I7': 'd',
    'cl': 'd',
    '|}': 'd',
    '>': 'd',
    '|]': 'd',
    '3': 'e',
    '[-': 'e',
    '|=-': 'e',
    '|=': 'f',
    '|#': 'f',
    'ph': 'f',
    '/=': 'f',
    '&': 'g',
    '(_+': 'g',
    '9': 'g',
    'C-': 'g',
    '(?,': 'g',
    '[,': 'g',
    '{,': 'g',
    '<-': 'g',
    '(.': 'g',
    '#': 'h',
    '/-/': 'h',
    '[-]': 'h',
    ']-[': 'h',
    ')-(': 'h',
    '(-)': 'h',
    ':-:': 'h',
    '|~|': 'h',
    '|-|': 'h',
    ']~[': 'h',
    '!-!': 'h',
    '1-1': 'h',
    '\-/': 'h',
    'I+I': 'h',
    '1': 'i',
    '!': 'i',
    'eye': 'i',
    '3y3': 'i',
    '][': 'i',
    ',_|': 'j',
    '_|': 'j',
    '._|': 'j',
    '._]': 'j',
    '_]': 'j',
    ',_]': 'j',
    ']': 'j',
    ';': 'j',
    '>|': 'k',
    '|<': 'k',
    '/<': 'k',
    '1<': 'k',
    '|c': 'k',
    '|(': 'k',
    '|{': 'k',
    '|_': 'l',
    '|': 'l',
    '/\/\\': 'm',
    '/V\\': 'm',
    'JVI': 'm',
    '[V]': 'm',
    '[]V[]': 'm',
    '|\/|': 'm',
    '^^': 'm',
    '<\/>': 'm',
    '{V}': 'm',
    '(v)': 'm',
    '(V)': 'm',
    '|V|': 'm',
    'nn': 'm',
    'IVI': 'm',
    '|\|\\': 'm',
    ']\/[': 'm',
    '1^1': 'm',
    'ITI': 'm',
    'JTI': 'm',
    '^/': 'n',
    '|\|': 'n',
    '/\/': 'n',
    '[\]': 'n',
    '<\>': 'n',
    '{\}': 'n',
    '|V': 'n',
    '/V': 'n',
    '0': 'o',
    '()': 'o',
    'oh': 'o',
    '[]': 'o',
    '<>': 'o',
    '|*': 'p',
    '|o': 'p',
    '?': 'p',
    '|>': 'p',
    '|"': 'p',
    '[]D': 'p',
    '|7': 'p',
    '(_,)': 'q',
    '()_': 'q',
    '0_': 'q',
    '<|': 'q',
    'I2': 'r',
    '|`': 'r',
    '|~': 'r',
    '|?': 'r',
    '/2': 'r',
    '|^': 'r',
    'lz': 'r',
    '|9': 'r',
    '2': 'r',
    '12': 'r',
    '[z': 'r',
    '.-': 'r',
    '|2': 'r',
    '|-': 'r',
    '5': 's',
    '$': 's',
    'z': 's',
    '7': 't',
    '+': 't',
    '-|-': 't',
    '"|"': 't',
    '~|~': 't',
    '(_)': 'u',
    '|_|': 'u',
    'L|': 'u',
    '\/': 'v',
    '|/': 'v',
    '\|': 'v',
    '\/\/': 'w',
    'VV': 'w',
    "'//": 'w',
    "\\\\'": 'w',
    '\^/': 'w',
    '(n)': 'w',
    '\V/': 'w',
    '\X/': 'w',
    '\|/': 'w',
    '\_|_/': 'w',
    '\_:_/': 'w',
    'uu': 'w',
    '2u': 'w',
    '\\\\//\\\\//': 'w',
    '><': 'x',
    '}{': 'x',
    ')(': 'x',
    '`/': 'y',
    '\//': 'y',
    '7_': 'z',
    '-/_': 'z',
    '%': 'z',
    '>_': 'z',
    '~/_': 'z',
    '-\_': 'z',
    '-|_': 'z'
}
