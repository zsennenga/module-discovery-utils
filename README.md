# Module Discovery Utils

## Motivation

A simple library to make it easier to dynamically find and discover objects from a predefined set of packages.

There is often a pattern used in python where subclasses of an object are defined, and by virtua of being a subclass, those objects are either directly or indirectly added to a registry.

Examples of this are Flask routes, and Sqlalchemy tables.

This is all well and good, but the problem is, you need to import those modules to register them.  A common solution is to create a registry file of sorts, sometimes in the __init__.py file.

Often, you have a significant number of classes, and are frequently adding new ones, or removing old ones. However, maintaining a single file that imports all of them can be cumbersome, and falls afoul of python style rules and formatting tools, as the imports are technically not used in the registry file.

Thus, using python's importlib, pkgutils, and introspection tools, there are a number of ways to dynamically scan a package, load all submodules, and parse out objects of interest.

I have implemented and reimplemented this sort of code many, many times, and I hope I can prevent others from doing the same in the future.

## Usage


To recursively import all modules in a group of packages:
```python
from module_discovery_utils import load_all_modules_in_packages
from blah import package, package2

load_all_modules_in_packages(package)
load_all_modules_in_packages(package2)
```
OR
```python
from module_discovery_utils import load_all_modules_in_packages
from blah import package, package2

load_all_modules_in_packages([package, package2])

```

To find all subclasses in a package:
```python
from module_discovery_utils import find_subclasses_in_packages
from blah import package, package2, BaseClass1, BaseClass2

find_subclasses_in_packages([package, package2], [BaseClass1, BaseClass2])
```

You can also technically do:
```python
from module_discovery_utils import load_all_modules_in_packages
from blah import package, package2, BaseClass

load_all_modules_in_packages([package, package2])
subclasses = BaseClass.__subclasses__()
```
However, the problem I have with that solution is there are cases (such as testing) where you may not want to retrieve all defined subclasses.

It's pratically impossible to control what gets imported when in a python program, and you don't want to potentially rely on import order, or imports from other parts of the program to determine which subclasses are "visible" at any given time.

To find all instances of a given base class in a given set of packages:
```python
from module_discovery_utils import find_instances_in_packages
from blah import package, package2, BaseClass1, BaseClass2

find_instances_in_packages([package, package2], [BaseClass1, BaseClass2])
```