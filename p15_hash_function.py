#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = Allen

import hashlib


if __name__ == '__main__':
    h1 = hashlib.md5("Hello, World!".encode()).hexdigest()
    h2 = hashlib.sha1("Hello, World!".encode()).hexdigest()

    print(h1)
    print(h2)

    h3 = hashlib.md5()
    h3.update("Hello, World!".encode())
    h3.update("This is part #2".encode())
    h3.update("This is part #3".encode())

    print(h3.hexdigest())
