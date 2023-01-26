# -*- coding: utf-8 -*-
"""."""

import re


def get_just_the_numbers(data: str) -> str:
    return re.sub('[^0-9]', '', data)


if __name__ == '__main__':
    pass
