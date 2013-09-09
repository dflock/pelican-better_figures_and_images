"""
Better Figures & Images
------------------------

This plugin:

- Adds a style="width: ???px; height: auto;" to each image in the content
- Also adds the width of the contained image to any parent div.figures.
    - If RESPONSIVE_IMAGES == True, also adds style="max-width: 100%;"
- Corrects alt text: if alt == image filename, set alt = ''

TODO: Need to add a test.py for this plugin.

"""

import os

from pelican import signals

from bs4 import BeautifulSoup
from PIL import Image


def content_object_init(instance):

    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content)

        if 'img' in content:
            for img in soup('img'):
                # TODO: Pretty sure this isn't the right way to do this, too hard coded.
                # There must be a setting that I should be using?

                #src = instance.settings['PATH'] + '/images/' + os.path.split(img['src'])[1]

                # The method mentioned above is only working if the images are really in the "images" folder.
                # It's also not working on subdirectories inside the image folder
                # Both issues are fixed:
                # Changed the static "/images/" string to the proper path which is extracted from the 'split' tuple
                # The first 7 letters are cutted ("/static") to get a valid link.
                # Somehow the static folder isn't created in the output folder. It's only on the server after 'make ftp_upload'
                src = instance.settings['PATH'] + os.path.split(img['src'])[0][7:] + '/' + os.path.split(img['src'])[1]

                im = Image.open(src)
                extra_style = 'width: {}px; height: auto;'.format(im.size[0])

                if instance.settings['RESPONSIVE_IMAGES']:
                    extra_style += ' max-width: 100%;'

                if img.get('style'):
                    img['style'] += extra_style
                else:
                    img['style'] = extra_style

                if img['alt'] == img['src']:
                    img['alt'] = ''

                fig = img.find_parent('div', 'figure')
                if fig:
                    if fig.get('style'):
                        fig['style'] += extra_style
                    else:
                        fig['style'] = extra_style

        instance._content = soup.decode()


def register():
    signals.content_object_init.connect(content_object_init)
