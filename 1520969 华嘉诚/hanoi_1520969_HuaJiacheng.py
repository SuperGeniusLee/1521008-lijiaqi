#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 4/25/18.

def move(n, left, mid, right):
    if n == 1:
        print(left, ">", right)
        return
    move(n - 1, left, right, mid)
    move(1, left, mid, right)
    move(n - 1, mid, left, right)

if __name__ == '__main__':
    move(3, "a", "b", "c")

