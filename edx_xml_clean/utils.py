"""
utils.py

Contains utility functions used in various parts of the library
"""
import os
from os.path import isfile
import re

def traverse(edxobj):
    """
    Returns a generator that traverses a given object and all its children recursively

    This allows routines to traverse an entire course by using:
    for obj in traverse(course):
        (do something with every obj in the course)

    :param edxobj: EdxObject to traverse
    :return: Generator of EdxObjects
    """
    # Generate this object
    yield edxobj

    # Generate every object generated by the children of this object
    for child in edxobj.children:
        for entry in traverse(child):
            yield entry

def check_static_file_exists(course, filename):
    """
    Checks that a given file exists in the static directory.

    :param course: Course object, needed to extract directory
    :param filename: Filename to look for
    :return: True/False
    """
    fullpath = os.path.join(course.directory, "static", filename)
    return isfile(fullpath)


# Copied from the edx-platform xmodule.fields library
TIMEDELTA_REGEX = re.compile(r'^((?P<days>\d+?) day(?:s?))?(\s)?((?P<hours>\d+?) hour(?:s?))?(\s)?((?P<minutes>\d+?) minute(?:s)?)?(\s)?((?P<seconds>\d+?) second(?:s)?)?$')

def validate_graceperiod(entry):
    """Returns True if entry is a valid grace period"""
    if entry is None:
        return True
    parts = TIMEDELTA_REGEX.match(entry)
    if not parts:
        return False
    return True