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

Each template inherits from the one above it. Below are listed the blocks
provided by each template.

### base.html

This template will search for static files of the form `{app_name}.js`,
`{app_name}.css`, and `{app_name}/{url_name}.js`, and include them if found.
It will also add `app-{app_name}` and `view-{url_name}` classes to the body
automatically.

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
- `extra_header`
- `extra_footer`

The first two blocks have content, the last three are designed to be extended.
Do not attempt to extend the `extra_` blocks if you overwrite their bases.

### sidebar.html

This template renders using a `fluid-container`, and provides a new `sidebar`
block in addition to the blocks provided by `default.html`

By default, the `sidebar` block will render the contents of the template
variable `sidebar_menus`, and provide the additional block `sidebar_extra`
at the bottom.

The template expects `sidebar_menu` to be an `dict`, mapping menu names to
iterables of menu items. Each item may then optionally have `url` and
`active` attributes, and should have a `name` attribute.

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
- `BT_TYPEAHEAD_VERSION`: the version of bootstrap-3-typeahead to load from
  cdnjs [4.0.2].
- `BT_SCROLLTO_VERSION`: the version of jQuery-scrollTo to load from cdnjs
  [2.1.0].
- `BT_SELECT2_VERSION`: the version of Select2 to load from cdnjs [4.0.3].
- `BT_FONTAWESOME_VERSION`: the version of Font Awesome to load from the
  Bootstrap CDN.
- `BT_FONTAWESOME_CSS_INTEGRITY` [set by default]
- `BT_VIEWPORT_SCALE`: enable the viewport meta tag [True]

Note that if the jQuery of Font Awesome versions are changed, the corresponding
SRI options must be set.

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

This piece works well when placed in the `extra_header` block from
`default.html`.

## Template Tags and Filters

### setting (tag)

Retrieves a Django setting. If a context variable exists with the exact same
name, that will be returned instead, to allow per-view overrides.

### script (tag)

Generates a script tag given a source URL, with optional SRI argument.
If the location does not match the current domain (starts with "https://"),
`crossorigin="anonymous"` is applied as well.

### style (tag)

Identical to the above, except for stylesheets.

### break_punctuation (filter)

Inserts <wbr> tags after all sequences of "non-word characters".

### order_by(args) (filter)

Orders the given queryset by the given args, a comma-separated string.

## Extra CSS Classes

### Responsive Tables

#### `.bt-table-responsive`

Fixes the current Bootstrap 4 issue where responsive tables try to behave
responsively even on larger screens. The 992px breakpoint has been used.

The following three classes must be children of a `.bt-table-responsive`

##### `.table-col-xs

Sets a minimum width of 6rem.

##### `.table-col-sm`

Sets a minimum width of 8rem.

##### `.table-col-md`

Sets a minimum width of 12rem.

##### `.table-col-lg`

Sets a minimum width of 16rem.

##### `.table-col-xl`

Sets a minimum width of 20rem.

##### `.table-col-break`

Allows long columns to be broken even against normal rules.
