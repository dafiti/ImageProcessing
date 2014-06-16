#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: lib/images.py
#
# This file is part of Dafiti's Image Processing
#
# Copyright (C) 2013 Dafiti TI Team <ti@dafiti.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.

from os import makedirs
from os.path import isdir

from wand.image import Image
from wand.color import Color


def get_resized_image(image, width=None, height=None):
    """ (str, int, int) -> Image

    Resizes an image

    Returns a wand.image.Image object
    """
    image_handler = Image(filename=image)

    if image_handler.height == image_handler.width:
        image_handler.resize(width=width, height=width)
    elif width and height:
        image_handler.resize(width=width, height=height)

    return image_handler


def generate_sprite(image_dir, images):
    """ (str, list of Image) -> str

    Generate sprites with 4 images

    Returns the name of the generated sprite
    """
    image_width = 160
    image_height = 232
    sprite = None
    left_position = 0
    for image in images:
        i = get_resized_image(image=image, width=image_width, height=image_height)
        if sprite is None:
            if i.height == i.width:
                sprite = Image(width=image_width*4, height=image_width, background=Color("#fff"))
            else:
                sprite = Image(width=image_width*4, height=image_height, background=Color("#fff"))
        sprite.composite(image=i, left=left_position, top=0)
        left_position += image_width
        i.destroy()
    sprite_file = "%s/sprite.jpg" % (image_dir)

    if not isdir(image_dir):
        makedirs(image_dir)

    sprite.save(filename=sprite_file)
    sprite.destroy()

    return sprite_file


def generate_pjpeg(output_dir, image, output_name):
    """ (str, Image, str) -> None

    Creates a Progressive JPEG
    """
    img = get_resized_image(image, 430, 620)
    new_image = "PJPEG:%s%s" % (output_dir, output_name)
    pjpeg = img.convert('JPEG')
    pjpeg.save(filename=new_image)
    pjpeg.destroy()
