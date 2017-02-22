#!/usr/bin/python

import os

def spaceToUnderscore():
    for filename in os.listdir("."):
        os.rename(filename, filename.replace(" ", "_"))

    return