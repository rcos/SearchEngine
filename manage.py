#!/usr/bin/env python
import os
import sys

import word_replace

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stupify.settings")
    
    print "Loading words"
    word_replace.load()
    dictionary = word_replace.dictionary

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
