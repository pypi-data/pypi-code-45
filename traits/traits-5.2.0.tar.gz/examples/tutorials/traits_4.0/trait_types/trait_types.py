#  Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

# --(New Trait Definition Style)------------------------------------------------
"""
New Trait Definition Style
==========================

The Traits package comes with a number of predefined traits, such as **Str**,
**Int**, **Float**, **Range** and so on. While these core traits suffice for
most common programming situations, quite often the need arises to create a
new *custom* trait.

Traits has always supported creating new traits, but in the past this has
typically involved creating a new **TraitHandler** subclass and invoking the
**Trait** function to define a new trait based on that subclass, as shown in
the following example::

    class OddIntHandler(TraitHandler):

        def validate(self, object, name, value):
            if isinstance(value, int) and ((value % 2) == 1):
                return value

            self.error(object, name, value)

        def info(self):
            return 'an odd integer'

    OddInt = Trait(1, OddIntHandler)

    OddInt = TraitFactory(OddInt)

While not overly complex, nevertheless several developers have complained that
that:

- The process of creating a new trait is not overly intuitive.
- The resulting trait cannot be subclassed to derive a new trait with slightly
  different behavior.

As a result, in Traits 3.0 a new method of defining traits has been added that
hopefully addresses both of these issues. Note that this new style of creating
traits does not replace the old style of creating traits, but is simply a new
technique that can be used instead of the original method. Both old and new
style traits can be defined, used and interoperate in the same program without
any adverse side effects.

OddInt Redux
------------

Using the new style of defining traits, we can rewrite our previous **OddInt**
example as follows::

    class OddInt(Int):

        # Define the default value:
        default_value = 1

        # Describe the trait type:
        info_text = 'an odd integer'

        def validate(self, object, name, value):
            value = super(OddInt, self).validate(object, name, value)
            if (value % 2) == 1:
                return value

            self.error(object, name, value)

This provides the exact same functionality as the previous definition of
**OddInt**. There are several points to make about the new definition however:

- The **OddInt** class derives from **Int** (not **TraitHandler**). This
  has several important side effects:

  * **OddInt** can re-use and change any part of the **Int** class behavior
    that it needs to. Note in this case the re-use of the **Int** class's
    *validate* method via the *super* call in **OddInt's** *validate* method.

  * As a subclass of **Int**, it is related to **Int**, which can be
    important both from a documentation and programming point of view. The
    original definition of **OddInt** was related to **Int** only in that their
    names were similar.

- The default value and trait description information are declared as class
  constants. Although there are more dynamic techniques that allow computing
  these values (which will be described in another tutorials), this provides
  a very simple means of defining these values.

- No use of **TraitHandler**, **Trait** or **TraitFactory** is required, just
  good old OO programming techniques. Hopefully this will make the process of
  creating a new trait type a little more understandable to a wider group of
  developers.
"""
# --<Imports>-------------------------------------------------------------------
from __future__ import print_function
from traits.api import *


# --[OddInt Definition]---------------------------------------------------------
class OddInt(Int):

    # Define the default value:
    default_value = 1

    # Describe the trait type:
    info_text = "an odd integer"

    def validate(self, object, name, value):
        value = super(OddInt, self).validate(object, name, value)
        if (value % 2) == 1:
            return value

        self.error(object, name, value)


# --[Test Class]----------------------------------------------------------------
class Test(HasTraits):

    any_int = Int
    odd_int = OddInt


# --[Example*]------------------------------------------------------------------

# Create a test object:
t = Test()

# Set both traits to an odd integer value:
t.any_int = 1
print("t.any_int:", t.any_int)

t.odd_int = 1
print("t.odd_int:", t.odd_int)

# Now set them both to an even value (and see what happens):
t.any_int = 2
print("t.any_int:", t.any_int)

t.odd_int = 2
print("t.odd_int:", t.odd_int)  # Should never get here!
