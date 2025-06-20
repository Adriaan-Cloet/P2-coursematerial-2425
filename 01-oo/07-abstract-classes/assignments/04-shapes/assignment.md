# Task

Copy the code from `startercode.py` to `student.py`.
The code defines two classes `Rectangle` and `Circle`.
Define a class `Shape` that acts as their parent class.

Look at what members `Rectangle` and `Circle` have in common.
Add those as abstract members to `Shape`.

You might wonder what use this might be: `Shape` only contains abstract members, so there's no shared code to speak of.
You can see `Shape` as a sort of "contract": it provides a guarantee that all of its child classes must contain certain members.
Say you were to define a new shape, say `Triangle`. In case you forget to implement a member, Python will point this out to you.
