from pytest import raises

from module_discovery_utils.module_discovery_utils import load_all_modules_in_packages
from test.test_cases.plugin_discovery_instance import main


def test_module_instead_of_package():
    with raises(Exception) as e:
        load_all_modules_in_packages(main)

    assert str(e.value) == (
        'Package object passed in has no __path__ attribute. '
        'Make sure to pass in imported references to the packages in question.'
    )


def test_bad_package_type():
    with raises(Exception) as e:
        load_all_modules_in_packages({'test': main})

    assert str(e.value) == (
        'This function only accepts a module reference, or an iterable of said objects'
    )

    with raises(Exception) as e:
        load_all_modules_in_packages('test')

    assert str(e.value) == (
        'This function only accepts a module reference, or an iterable of said objects'
    )

    with raises(Exception) as e:
        load_all_modules_in_packages(object())

    assert str(e.value) == (
        'This function only accepts a module reference, or an iterable of said objects'
    )
