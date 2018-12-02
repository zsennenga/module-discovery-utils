import importlib
import pkgutil
import types
from collections.abc import Iterable
from inspect import isclass


def load_all_modules_in_packages(package_or_set_of_packages):
    """
    Recursively loads all modules from a package object, or set of package objects

    :param package_or_set_of_packages: package object, or iterable of package objects
    :return: list of all unique modules discovered by the function
    """
    if isinstance(package_or_set_of_packages, types.ModuleType):
        packages = [package_or_set_of_packages]
    elif isinstance(package_or_set_of_packages, Iterable) and not isinstance(package_or_set_of_packages, (dict, str)):
        packages = package_or_set_of_packages
    else:
        raise Exception("This function only accepts a module reference, or an iterable of said objects")

    imported = packages.copy()

    for package in packages:
        if not hasattr(package, '__path__'):
            raise Exception(
                'Package object passed in has no __path__ attribute. '
                'Make sure to pass in imported references to the packages in question.'
            )

        for module_finder, name, ispkg in pkgutil.walk_packages(package.__path__):
            module_name = '{}.{}'.format(package.__name__, name)
            current_module = importlib.import_module(module_name)
            imported.append(current_module)
            if ispkg:
                imported += load_all_modules_in_packages(current_module)

    return list(
        {
            module.__name__: module

            for module in imported
        }.values()
    )


def find_subclasses_in_packages(packages, base_classes):
    """
    Find objects in a set of packages that are class definitions that are subclasses of a set of base classes.

    :param packages: List of package references to the packages you're interested in.
    :param base_classes: List of classes that you want to find subclasses for.
    :return: List of objects mapping to the discovered subclasses
    """
    return _discover_objects(packages, base_classes, True)


def find_instances_in_packages(packages, base_classes):
    """
    Find objects in a set of packages that are instances of a set of base classes, or any subclasses.

    :param packages: List of package references to the packages you're interested in.
    :param base_classes: List of classes that you want to find subclasses for.
    :return: List of all discovered instances
    """
    return _discover_objects(packages, base_classes, False)


def _check_item(item, base_classes, class_definitions_only):
    if class_definitions_only:
        return (
                item not in base_classes and
                isclass(item) and
                any([issubclass(item, _class) for _class in base_classes])
        )
    else:
        return (
                isinstance(item, base_classes) and
                item not in base_classes
        )


def _get_name(obj):
    if isclass(obj):
        return obj.__name__
    else:
        return obj.__class__.__name__


def _discover_objects(packages, base_classes, class_definitions_only):
    discovered_objects = []

    modules = load_all_modules_in_packages(packages)

    if not isinstance(base_classes, tuple):
        base_classes = tuple(base_classes)

    for module in modules:
        for name, value in module.__dict__.items():
            if name.startswith("__") and name.endswith("__"):
                continue

            if _check_item(value, base_classes, class_definitions_only):
                discovered_objects.append(value)

    return list(
        {
            _get_name(item): item
            for item in discovered_objects
        }.values()
    )
