# Super

In the previous exercise we had `AgeRestrictedItem`s that could only be sold to `Customer`s who are at least 18 years old.
Similarly, a `CountryRestrictedItem` could not be sold to `Customer`s residing in `Arstotzka`.

```python
class AgeRestrictedItem(Item):
    def can_be_sold_to(self, customer):
        return customer.age >= 18


class CountryRestrictedItem(Item):
    def can_be_sold_to(self, customer):
        return customer.country != 'Arstotzka'
```

The age (18) and country (Arstotzka) are hardcoded.
That's generally not a good solution: we can so easily generalize these classes, i.e., make them more flexible, by relying on parameters.
We want users of the class to be able to specify the minimum age or forbidden countries.
Let's try this:

```python
class AgeRestrictedItem(Item):
    def __init__(self, minimum_age):
        self.minimum_age = minimum_age

    def can_be_sold_to(self, customer):
        return customer.age >= minimum_age


class CountryRestrictedItem(Item):
    def __init__(self, forbidden_countries):
        self.forbidden_countries = forbidden_countries

    def can_be_sold_to(self, customer):
        return customer.country not in forbidden_countries
```

Can you see a problem with this?
We'll give you a few moments to think.

&vellip;

Okay, that's enough moments.
Let's see what happens when we instantiate an `AgeRestrictedItem`:

```python
>>> item = AgeRestrictedItem(18)
>>> item.name
AttributeError: 'AgeRestrictedItem' object has no attribute 'name'

>>> item.price
AttributeError: 'AgeRestrictedItem' object has no attribute 'price'
```

The error makes perfect sense: we never mentioned the item's name or price.
Can we perhaps... pass them along to the constructor?

```python
>>> item = AgeRestrictedItem('lightsaber', 5, 18)
TypeError: AgeRestrictedItem.__init__() takes 2 positional arguments but 4 were given
```

That was bound to happen: `AgeRestrictedItem` has overridden its parent class's `__init__` method.
The new version only takes one (or two, if you count `self`) parameters.

We clearly want to be able to specify a name and a price, as well as a minimum age.
This means `AgeRestrictedItem.__init__` will have to accept three parameters:

```python
class AgeRestrictedItem(Item):
    def __init__(self, name, price, minimum_age):
        ???
```

We could simply perform the initialization in `AgeRestrictedItem`'s constructor:

```python
class AgeRestrictedItem(Item):
    def __init__(self, name, price, minimum_age):
        self.name = name
        self.price = price
        self.minimum_age = minimum_age
```

This is a rather bad idea, however: most of the code already exists in `Item`.
We would like to delegate the initialization of `name` and `price` call `Item.__init__`.
And that's exactly what we can do:

```python
class AgeRestrictedItem(Item):
    def __init__(self, name, price, minimum_age):
        super().__init__(name, price)
        self.minimum_age = minimum_age
```

`super()` allows you to access the "old" versions of methods.
Here, `super().__init__` refers to the `__init__` method defined in `Item`.

So, what happens is simple:

* You want to make an `AgeRestrictedItem` with a certain `name`, `price`, and `minimum_age`.
  In code, this is written `AgeRestrictedItem(name, price, minimum_age)`.
* `AgeRestrictedItem.__init__` is called with the given arguments.
* `AgeRestrictedItem.__init__` first calls `super().__init__`, which refers to `Item.__init__`.
* `Item.__init__` initializes the `name` and `price` of the object.
* After `Item.__init__` has finished, execution returns to `AgeRestrictedItem.__init__` which initializes the third attribute, `minimum_age`.
