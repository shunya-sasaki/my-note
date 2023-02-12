Introduction to Rust
====================

Install Rust
------------

Install Rust by the following comand, if you use MacOSX or Linux.

.. code-block:: shell

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

You can update rust by the command *rustup update* .

.. code-block:: shell

    rustup update


Create Project
--------------

.. code-block:: shell

    cargo new YOUR_PROJECT

run program

.. code-block::

    cargo run

Install crates
--------------

In Rust, refer to packages as "crates".
We can get crates from `crates.io <https://crates.io/>`_ .
To install crates to the project, edit "dependencies" section in Cargo.toml.
For example, to install "ferris-says" crate, write Cargo.toml as the following.

.. code-block:: toml

And run **cargo build** .

.. code-block:: shell

    cargo build

Check compile.

.. code-block:: shell

    cargo check

Build release version

.. code-block:: shell

    cargo build --release