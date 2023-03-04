Build Python packages with Rust
===============================

You can build Python packages with Rust by the following steps.

1. Create Rust project directory by cargo.
2. Create files for setuptools-rust.
3. Create Rust source files which include functions called by Python.
4. Run setuptools and build package files.

On this page, we create the *string-sum* package.
The *string-sum* package is used in your code as follows.

.. code-block:: python

    import string_sum

    result = string_sum.sum_as_string(2, 3)
    print(result)

The output is the follows.

::

    '5'


Create Rust project directory
-----------------------------

Create a Rust project directory by the following comand.

.. code-block::

    cargo new --lib YOUR_LIBRARY

And edit Cargo.toml as follows.

.. code-block:: toml

    [package]
    name = "string_sum"
    version = "0.1.0"
    edition = "2018"

    [lib]
    # The name of the native library. This is the name which will be used in Python to import the
    # library (i.e. `import string_sum`). If you change this, you must also change the name of the
    # `#[pymodule]` in `src/lib.rs`.
    name = "string_sum"
    # "cdylib" is necessary to produce a shared library for Python to import from.
    #
    # Downstream Rust code (including code in `bin/`, `examples/`, and `tests/`) will not be able
    # to `use string_sum;` unless the "rlib" or "lib" crate type is also included, e.g.:
    # crate-type = ["cdylib", "rlib"]
    crate-type = ["cdylib"]

    [dependencies]
    pyo3 = { version = "0.18.1", features = ["extension-module"] }


Create files for setuptools-rust
--------------------------------

setup.py
^^^^^^^^

.. code-block:: python

    from setuptools import setup
    from setuptools import find_packages
    from setuptools_rust import Binding
    from setuptools_rust import RustExtension

    setup(
        name="string-sum",
        version="1.0",
        rust_extensions=[RustExtension("string_sum", binding=Binding.PyO3)],
        packages=find_packages(),
        # rust extensions are not zip safe, just like C-extensions.
        zip_safe=False,
    )

pyproject.toml
^^^^^^^^^^^^^^

.. code-block:: toml

    [build-system]
    requires = ["setuptools", "wheel", "setuptools-rust"]


MANIFEST.in
^^^^^^^^^^^

.. code-block:: 

    include Cargo.toml
    recursive-include src *


Rust source for python modules
------------------------------

.. code-block:: rust

    use pyo3::prelude::*;

    /// Formats the sum of two numbers as string.
    #[pyfunction]
    fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
        Ok((a + b).to_string())
    }

    /// A Python module implemented in Rust. The name of this function must match
    /// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
    /// import the module.
    #[pymodule]
    fn string_sum(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
        m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
        Ok(())
    }

Build Python package with the python build module
-------------------------------------------------

So far, the directory configurations will be as follows.

::

    YOUR_LIBRARY
    |- src
    |  `- lib.rs  
    |- .gitignore
    |- MANIFEST.in
    |- setup.py
    |- Cargo.lock
    |- Cargo.toml
    `- pyproject.toml

All that remain to build a python package is to execute the following command.

.. code-block:: shell

    python -m build
