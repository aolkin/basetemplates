# Base Templates
Base templates for starting a Django project with Bootstrap.

## Inheritable Templates

Each template is designed to be inherited from, and provides a number of
blocks to be used. Additionally, some behavior of these templates can be
controlled by various settings, described below.

For all templates to function properly, a CSS file is included, and requires
that static files are set up properly. The request context processor must also
be enabled for the templates to function.

Additionally, the base template expects static files to be set up, and will
search for static files of the form `{app_name}.js` and
`{app_name}/{url_name}.js`and include them if found.

Lastly, `basetemplates.context_processor` must be enabled.

Each template inherits from the one above it. Blocks provided:

### base.html

- title
- body
- extra_scripts

### default.html

This template consumes the `body` block from above, and provides three new
blocks within it.

- header
- footer
- content

### sidebar.html

This template consumes the `content` block from above, and provides two new
blocks within it.

- sidebar
- main

## Settings

### Settings used by the base template

- `BT_SITE_TITLE`: the part after the last | in page titles
- `BT_CSS_FILES`: paths to static css files for the site
- `BT_JS_FILES`: paths to static js files for the site
- `BT_BOOTSTRAP_VERSION`: the version of Bootstrap to link to [3.3.7].
- `BT_BOOTSTRAP_CSS_INTEGRITY`
- `BT_BOOTSTRAP_JS_INTEGRITY`
- `BT_TETHER_VERSION`: include this to enable Tether for Bootstrap 4
- `BT_TETHER_JS_INTEGRITY`
- `BT_JQUERY_VERSION`: the version of jQuery to link to [3.2.1].
- `BT_JQUERY_JS_INTEGRITY` [set by default]
- `BT_VIEWPORT_SCALE`: enable the viewport meta tag [True]

### Settings used by the default template

Except for the first, these settings will only be used if the respective block
is not overridden.

- `BT_CONTAINER_FLUID`: determines if the root container is fluid or not
  [False].
- `BT_FOOTER_OWNER`: copyright the current year for this text will be shown
- `BT_FOOTER_SITE`: will become a link
- `BT_HEADER_IMAGE`: passed to `static`
- `BT_HEADER_URL`: passed to `url`

## Template Pieces

These are designed to be included in your templates, and many expect
a certain context variable to be provided.

### messages.html

Renders the contents of the `messages` context variable using Bootstrap.

### title.html

An easy way to fill in the title block using the `page_title` context variable.

### user_dropdown.html

This is meant to be extended, then included, but can be included directly.
It renders a dropdown menu based on the current authentication state.
It provides the `user_menu_actions` and `user_authenticated_actions` blocks
for extension (the former will always be shown, the latter only when a user is
logged in).

## Template Tags

### setting

Retrieves a Django setting.

### script

Generates a script tag given a source URL, with optional SRI argument.
If the location does not match the current domain (starts with "https://"),
`crossorigin="anonymous"` is applied as well.

### style

Identical to the above, except for stylesheets.
