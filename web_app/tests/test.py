import pytest

from web_app.app import *
from web_app.app import app


class Tests:

    def test_sanity_check(self):

        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_sanity_check2(self):

        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"