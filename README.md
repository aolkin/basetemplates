# Base Templates
Base templates for starting a Django project with Bootstrap.

This project attempts to simultaneously support versions 3 and 4 by using
classes from both where possible. However, where only one usage is possible,
Bootstrap 4 will be preferred.

## Inheritable Templates

Each template is designed to be inherited from, and provides a number of
blocks to be used. Additionally, some behavior of these templates can be
controlled by various settings, described below.

For all templates to function properly, a CSS file is included, and requires
that static files are set up properly. The request context processor must also
be enabled for the templates to function.

Lastly, `basetemplates.context_processor` must be enabled.

> Note: the context processor mainly allows the templates to function properly,
> but also provides a `SETTINGS` context variable that simply refers to the
> Django settings object.

Each template inherits from the one above it. Blocks provided:

### base.html

This template will search for static files of the form `{app_name}.js`,
`{app_name}.css`, and `{app_name}/{url_name}.js`, and include them if found.

- `title`
- `body`
- `extra_scripts`

### default.html

This template consumes the `body` block from above, and provides four new
blocks within it.

To disable the header image link for an individual page, set context variable
`BT_no_header_link` to True.

- `header`
- `footer`
- `content`
- `extra_footer`

The first two blocks have content, the last two are designed to be extended.
Do not attempt to extend `extra_footer` if you overwrite `footer`.

### sidebar.html

*// TODO*

This template consumes the `content` block from above, and provides two new
blocks within it.

- `sidebar`
- `main`

## Settings

### Settings used by the base template

- `BT_SITE_TITLE`: the part after the last | in page titles
- `BT_FAVICON_URL`
- `BT_CSS_FILES`: paths to static css files for the site
- `BT_JS_FILES`: paths to static js files for the site
- `BT_BOOTSTRAP_VERSION`: the version of Bootstrap to link to [3.3.7].
- `BT_BOOTSTRAP_CSS_INTEGRITY`
- `BT_BOOTSTRAP_JS_INTEGRITY`
- `BT_TETHER_VERSION`: include this to enable Tether for Bootstrap 4
- `BT_TETHER_JS_INTEGRITY`
- `BT_JQUERY_VERSION`: the version of jQuery to link to [3.2.1].
- `BT_JQUERY_JS_INTEGRITY` [set by default]
- `BT_TYPEAHEAD_VERSION`: the version of typeahead.js to load from cdnjs
  [0.11.1].
- `BT_VIEWPORT_SCALE`: enable the viewport meta tag [True]

### Settings used by the default template

Except for the first two, these settings will only be used if the respective
block is not overridden.

- `BT_CONTAINER_FLUID`: determines if the root container is fluid or not
  [False].
- `BT_INCLUDE_MESSAGES`: automatically include the `messages.html` piece
  [True].
- `BT_FOOTER_OWNER`: copyright the current year for this text will be shown
- `BT_FOOTER_SITE`: will become a link
- `BT_HEADER_IMAGE`: passed to `static`
- `BT_HEADER_URL`: passed to `url`

This template will also respond to the context variable `BT_hide_messages`,
allowing the message piece to be hidden on a per-page basis if enabled
globally.

## Template Pieces

These are designed to be included in your templates, and many expect
a certain context variable to be provided.

### messages.html

Renders the contents of the `messages` context variable using Bootstrap.
It uses the setting `BT_MESSAGES_COLUMN_SPEC` to control the width of the
displayed alerts, via a bootstrap column class such as `col-md-6`.

### title.html

An easy way to fill in the title block using the `page_title` context variable.

### user_dropdown.html

This is meant to be extended, then included, but can be included directly.
It renders a dropdown menu based on the current authentication state.
It provides the `user_menu_actions` and `user_authenticated_actions` blocks
for extension (the former will always be shown, the latter only when a user is
logged in).

It expects the admin interface to be enabled, and the `LOGOUT_URL` setting
to be defined.

## Template Tags

### setting

Retrieves a Django setting. If a context variable exists with the exact same
name, that will be returned instead, to allow per-view overrides.

### script

Generates a script tag given a source URL, with optional SRI argument.
If the location does not match the current domain (starts with "https://"),
`crossorigin="anonymous"` is applied as well.

### style

Identical to the above, except for stylesheets.
