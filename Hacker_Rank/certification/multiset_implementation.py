#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    
    def __init__(self) -> None:
        self.m = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.m.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.m:
            self.m.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.m:
            return True
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.m)

if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)
    for res in result:
        print(res)