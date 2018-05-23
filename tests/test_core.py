#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import os

# Expand path to module
mainDir = os.path.dirname(__file__)
sys.path.insert(0,
                os.path.abspath(
                        os.path.join(mainDir, '..')))
del mainDir
import carSharingBills as cSB


def test():
    assert True
