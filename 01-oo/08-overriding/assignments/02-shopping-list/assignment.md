## Task

Copy the contents of `startercode.py` to `student.py`.
Take a quick look at the code:

* A `Customer` has a name, an age and a country.
* A `ShoppingList` has an owner (a `Customer`) and a list of `Item`s.

The `Item` class still needs to be defined.
That'll be your job.

Start off by defining a class `Item`.
An `Item` should have a `name` and a `price` which are set using the constructor.

As you can see, `shopping_list.add(item)` relies on the `shopping_list.can_be_sold_to(item)` method: it checks if it is legal to sell `item` to the `owner` of the `shopping_list`.
If it's not, `add` refuses to actually add the `item` to the `shopping_list`.
You must therefore equip your `Item` class with a `can_be_sold_to` method.
You can keep it simple: simply have it return `True`.

Next, we want to introduce the concept of an `AgeRestrictedItem`.
It is only allowed to be sold to `Customer`s with `age` at least `18`.
Create a new class `AgeRestrictedItem` which is a child class of `Item`.
Override the `can_be_sold_to` method so that it returns `False` for underage `Customer`s.

Finally, we also want a `CountryRestrictedItem`.
Such `Item`s cannot be sold to people from `Arstotzka`.
