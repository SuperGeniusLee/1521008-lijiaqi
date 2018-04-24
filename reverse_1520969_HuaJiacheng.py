#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 4/24/18.

def reverse(l: list, size: int):
    if not size: return l
    l.insert(size, l.pop(0))
    return reverse(l, size - 1)


if __name__ == '__main__':
    l = reverse([12, 2, 3, 4], 3)
    print(l)
