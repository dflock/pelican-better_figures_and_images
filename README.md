# Better Figures & Images: A Plugin for Pelican

[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/better_figures_and_images/build)](https://github.com/pelican-plugins/better_figures_and_images/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-better_figures_and_images)](https://pypi.org/project/pelican-better_figures_and_images/)
![License](https://img.shields.io/pypi/l/pelican-better_figures_and_images?color=blue)

Responsive Images & Figure Numbers

## Installation

This plugin can be installed via - this will also install the required dependencies automatically:

    python -m pip install pelican-better_figures_and_images

## Usage

This plug-in:

-   Adds a `style="width: ???px; height: auto;"` attribute to any
    `<img>` tags in the content, by checking the dimensions of the image
    file and adding the appropriate
    `style="width: ???px; height: auto;"` to the `<img>` tag.
-   Also finds any `div class="figures"` tags in the content, that
    contain images and adds the same style to them too.
-   If `RESPONSIVE_IMAGES` setting is true, it adds
    `style="width: ???px; max-width: 100%; height: auto;"` instead.
-   Corrects Alt text: If an image `alt` attribute equals the image
    filename, it sets it to ""

Assuming that the image is 250px wide, it turns this:

```html
<div class="figure">
    <img alt="/static/images/image.jpg" src="/static/images/image.jpg" />
    <p class="caption">This is the caption of the figure.</p>
    <div class="legend">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.
    </div>
</div>
```

into this:

```html
<div class="figure" style="width: 250px; height: auto;">
    <img
        style="width: 250px; height: auto;"
        alt=""
        src="/static/images/image.jpg"
    />
    <p class="caption">This is the caption of the figure.</p>
    <div class="legend">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.
    </div>
</div>
```

or this, if `RESPONSIVE_IMAGES = True`:

```html
<div class="figure" style="width: 250px; max-width: 100%; height: auto;">
    <img
        style="width: 250px; max-width: 100%; height: auto;"
        alt=""
        src="/static/images/image.jpg"
    />
    <p class="caption">This is the caption of the figure.</p>
    <div class="legend">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.
    </div>
</div>
```

or this, if `FIGURE_NUMBERS` is also True:

```html
<div class="figure" style="width: 250px; max-width: 100%; height: auto;">
    <img
        style="width: 250px; max-width: 100%; height: auto;"
        alt=""
        src="/static/images/image.jpg"
    />
    <p class="caption">
        <span class="fig_num" id="fig_1">Figure 1: </span>This is the caption of
        the figure.
    </p>
    <div class="legend">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.
    </div>
</div>
```

## Contributing

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/better_figures_and_images/issues
[contributing to pelican]: https://docs.getpelican.com/en/latest/contribute.html

## License

This project is licensed under the AGPL-3.0 license.
