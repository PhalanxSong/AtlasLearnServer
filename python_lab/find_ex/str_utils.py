import os
import os.path
import codecs
import random


def CleanStr(var):
    var = var.replace('\r', '')
    var = var.replace('\n', '')
    var = var.replace('\t', '')
    var = var.replace(' ', '')
    return var
