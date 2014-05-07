#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: tests/lib/test_images.py
#
# This file is part of Dafiti's Image Processing
#
# Copyright (C) 2013 Dafiti TI Team <ti@dafiti.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.

import os
import pytest

from sys import path
from shutil import rmtree
from wand.image import Image

path.append('.')

from lib.images import *


def test_get_resized_image():
    image = 'tests/fixtures/blackdress.jpg' # 1104 x 1600

    resized_image = get_resized_image(image, 200, 300)

    assert 200 == int(resized_image.width)
    assert 300 == int(resized_image.height)


def test_generate_pjpeg():
    image = 'tests/fixtures/blackdress.jpg' # 1104 x 1600
    output_dir = '/tmp/ibp_tests/'
    output_name = 'new_blackdress.jpg'
    output_file = "%s%s" % (output_dir, output_name)

    try:
        rmtree(output_dir)
    except:
        pass

    os.mkdir(output_dir)

    generate_pjpeg(output_dir, image, output_name)

    img = Image(filename=output_file)

    assert img.width == 430
    assert img.height == 620
    assert img.format == 'JPEG'
    assert img.metadata.get('jpeg:colorspace') == '2'
