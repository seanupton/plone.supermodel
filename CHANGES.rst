Changelog
=========

1.2.5 (unreleased)
------------------

- Support Choice fields with terms containing distinct title from value
  as option, while preserving backward-compatible round-trip for all
  Choice fields where title is not distinct from value.
  [seanupton]

- Fix parsing of empty Choice term to u'', not None, which addresses a
  cause of https://github.com/plone/plone.app.dexterity/issues/49
  [seanupton]

- Explicitly construct SimpleTerm instances for each Choice field
  element, instead of relying on zope.schema constructors to do so.
  This ensures that all terms have non-None title attributes.
  [seanupton]

- Tests for ChoiceHandler serialization and parsing.
  [seanupton]


1.2.4 (2014-01-27)
------------------

- Replace deprecated test assert statements.
  [timo]


1.2.3 (2013-08-14)
------------------

- Add defaultFactory tag for Dexterity XML. Define an interface
  IDefaultFactory. defaultFactories specified via XML must implement it or
  IContextAwareDefaultFactory.


1.2.2 (2013-05-23)
------------------

- Avoid trying to process XML comments within field values.
  [davisagli]


1.2.1 (2013-01-01)
------------------

- Allow XML comments in field definitions.
  [gweis]

1.2.0 (2012-10-17)
------------------

- Nothing changed yet.


1.1.2 (2012-08-29)
------------------

- Use lxml instead of elementtree.
  [davisagli]

- Avoid a test dependency on zope.app.testing.
  [davisagli]


1.1.1 (2012-04-15)
------------------

- Fix a packaging error.
  [esteele]

1.1 (2012-04-15)
----------------

- Support i18n:domain and i18n:translate for internationalization.
  [davisagli]

- When an error is encountered while parsing a supermodel, the exception
  now provides the filename, line number, and source of the part of the
  model that was being processed. Inclusion of the line number and source
  requires lxml.
  [davisagli]

- Add model.Schema and directives to avoid grok dependency.
  [elro]

1.0.4 - 2012-02-20
------------------

- When syncing to a schema that inherits fields from a base, include fields
  with the same names as the inherited fields even when overwrite is False.
  This fixes http://code.google.com/p/dexterity/issues/detail?id=253
  [davisagli]

1.0.3 - 2011-05-20
------------------

- Relicense under BSD license.
  See http://plone.org/foundation/materials/foundation-resolutions/plone-framework-components-relicensing-policy
  [davisagli]

1.0.2 - 2011-05-02
------------------

- Only convert Choice field ``values`` attribute into a vocabulary when it is
  necessary to handle unicode values. This fixes a regression in compatibility
  with plone.registry.
  [davisagli]

1.0.1 - 2011-04-30
------------------

- Adjust manifest to exclude .pyc files.
  [davisagli]

1.0 - 2011-04-30
----------------

- Handle serializing tokenized vocabularies with unicode values as long as the
  terms' tokens are equal to the utf8-encoded values.
  [davisagli]


1.0b8 - 2011-03-18
------------------

- Add MANIFEST.in.
  [WouterVH]

- Field names should be strings, not unicode.
  [elro]


1.0b7 - 2011-03-03
------------------

- Support serialization of nested dicts/lists.
  [elro]


1.0b6 - 2011-01-04
------------------

- Declare zope.app.testing as a test dependency for Zope 2.13 compatibility.
  [esteele]

- Fix namespace bug which could prevent loading Dict and Collection elements.
  [davisagli]


1.0b5 - 2010-04-19
------------------

- Added support for zope.schema.Decimal fields.
  [optilude]


1.0b4 - 2009-11-17
------------------

- Ignored vocabularyName property when writing Choice fields. The constructor
  still uses they 'vocabulary' key in an overloaded capacity. We only support
  'vocabulary' with a named vocabulary, or 'values' with a list of values.
  This fixes test failures on Zope 2.12 / zope.schema 3.5.4.
  [optilude]


1.0b3 - 2009-09-28
------------------

- Add support for synchronising marker interfaces found on source fields
  to syncSchema().
  [optilude]


1.0b2 - 2009-07-12
------------------

- Changed API methods and arguments to mixedCase to be more consistent with
  the rest of Zope. This is a non-backwards-compatible change. Our profuse
  apologies, but it's now or never. :-/

  If you find that you get import errors or unknown keyword arguments in your
  code, please change names from foo_bar too fooBar, e.g. load_file() becomes
  loadFile().
  [optilude]

- No longer include name kwarg to Field constructor if no name was set
  [MatthewWilkes]


1.0b1 - 2009-04-17
------------------

- Initial release
