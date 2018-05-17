#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import os

# Expand path to module
mainDir = os.path.dirname(__file__)
sys.path.insert(0,
        os.path.abspath(
            os.path.join(mainDir,'..')))
del mainDir

# Import module
import template

def test_add():
    assert template.mod1.add(1,2) == 3 

def test_mult():
    assert template.mod2.mult(2,2) == 4

