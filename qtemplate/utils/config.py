import inspect
import os
import re
import sys
from urllib.parse import urlparse

import yaml

SELF = sys.modules[__name__]
SCHEMES = [
    'file',
    'http',
    'https'
]


def default_config():
    """Returns a default config as dict"""
    return {
        "template_stores": [
            "file:///etc/qtemplate/templates/*",
            "file:///~/.qtemplate/templates/*",
        ],
        "prompt": {
            "enabled": False
        },
    }


def merge(default, config):
    """Merge two configs and returns as dict"""
    new = default.copy()
    new.update(config)
    return new


# --------------------------------------------------------------
# Config Loading
# --------------------------------------------------------------
def load(uri):
    """Load an external document from a store"""
    pass


def resolve_loader(uri):
    """Resolve the appropriate loader function"""
    pass


def resolve_scheme(uri):
    """Ensures valid scheme and required URI fields per scheme"""
    parsed = urlparse(uri)
    if parsed.scheme is None:
        raise ValueError("URI {0} is missing scheme".format(uri))
    elif parsed.scheme not in SCHEMES:
        raise ValueError("URI scheme not supported. Must be one of {0}".format(",".join(SCHEMES)))
    return parsed.scheme


def load_file_yaml():
    """Load a document from yaml"""
    pass


def load_file_ini():
    """Load a document from ini config"""
    pass


def load_file_json():
    """Load a document from a json file"""
    pass


def load_https():
    """Load a document from an https respource"""
    pass
