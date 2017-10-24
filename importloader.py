#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging


def load(name):
    try:
        obj = __import__(name)
        reload(obj)
        return obj
    except Exception as e:
        logging.error(e.message)
        pass

    try:
        import importlib
        obj = importlib.__import__(name)
        importlib.reload(obj)
        return obj
    except Exception as e:
        logging.error(e.message)
        pass


def loads(namelist):
    for name in namelist:
        obj = load(name)
        if obj is not None:
            return obj
