
from nose.tools import *
import NAME


def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')


if __name__ == "__main__":
    print("This was run directly")
else:
    print("This was run as a module")
