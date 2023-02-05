How to write document with Sphinx
=================================

Create Python virtual environment
---------------------------------

In the beginning, install the Sphinx library in your Python environment.
I recommend you use a virtual environment to avoid library conflict with 
other projects.
You can create a virtual environment with the following command.

.. code-block:: shell

    python -m venv YOUR_VIRTUAL_ENVIRONMENT_PATH

For example, if you create a virtual environment named "py310" in ~/.venv,
you execute the following command.

.. code-block::  shell

    python -m venv ~/.venv/py310

To use the virtual environment, you have to activate it.
You can activate the environment by the following command.

.. code-block:: shell

    source ~/.venv/py310/bin/activate

If you use Windows terminal system, use the following command instead of the one above.

.. code-block:: bat

    ~/.venv/py310/Scripts/activate

When you succeed to activate your virtual environment, the environment name is displayed at before of your terminal line.

.. code-block:: shell-session

    (py310) shun@MacBook-Pro mynote % 


Install Sphinx
--------------

You can install Sphinx to your python environment by using the following command.

.. code-block:: shell

    python -m pip install sphinx

There are many third-party extensions for Sphinx and to use them you have to install library packages.
Extensions include themes that change the look and feel of the document, flowcharting tools, and more.
For example, you can install "sphinx-material" theme which is used for this document by the following command.

.. code-block:: shell

    python -m pip install sphinx-material


Create project directory
------------------------

First, create directories with the following configuration.

::

    PROJECT_ROOT
    `- src

In "src" directory, execute the following command,
and a Sphinx project directory named "docs" is created.

.. code-block:: shell

    sphinx-quickstart -q -p PROJECT_NAME -a AUTHOR_NAME ./docs

Now, your project directory configuration becomes as the following.

::

    PROJECT_ROOT
    `- src
       `- docs
          |- _build
          |- _static
          |- _templates
          |- Makefile
          |- make.bat
          |- conf.py
          `- index.rst


Build the first document
------------------------

In this section, you build the HTML document.
Output the document files to the "docs" directory in directly under the project directory for uploading to Github Pages.

Edit Makefile to add a copy process that copies document files to “docs” in the project root.

.. code-block:: diff

    + html: Makefile
    +     @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
    +    if [ -e ../../docs ]; then rm -rf ../../docs; fi
    +    cp -r ./_build/html ../../docs
    +    touch ../../docs/.nojekyll

    %: Makefile
        @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

Let's execute the following command in "src/docs",
the HTML document files are outputted to "src/docs/_build/html" directory and "docs" directory.

.. code-block:: shell

    make html

After outputting the document files, open the "index.html" in the output directory with your web browser such as Google Chrome.


Publish the document on GitHub Pages
------------------------------------

You can publish your document easily by using GitHub Pages.
To publish your documents on GitHub Pages, conduct the next 5 steps.

1. Create a project repository on GitHub.
2. Build the document files on "docs".
3. Stage "docs" to changes, and commit.
4. Push to the remote GitHub repository.
5. Configure your GitHub Pages setting.


Configure GitHub Pages setting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following, I wrote the detail of the 5th step.

1. Access your project repository on GitHub, and open "settings".
2. From the sidebar menu, you select "Pages" in the "Code and automation" section.
3. In the "Branch" part on the "Build and deployment" section, set the branch to "main" and the folder to "/docs".
4. After setting the branch and folder, push the save button.
5. After setting up, your GitHub Pages site is built
   and the URL and the "Visit site" button are displayed on the top of the setting page.
   Access your site and check it!


Document Internationalization
-----------------------------

Internationalize the document according to the official Sphinx method.

At first, install "sphinx-intl" package with pip command.

.. code-block:: shell

    python -m pip install sphinx-intl

Second, edit conf.py to add settings.

.. code-block:: diff

    + locale_dirs = ['locale/']
    + gettext_compact = False

And then, by the following command in "src/docs" generate POT files.
POT files are outputted to the "src/docs/_build" directory.

.. code-block:: shell

    make gettext

Generate PO files with the following command,
and files are outputted to the "src/docs/locale" directory.

.. code-block:: shell

    sphinx-intl update -p _build/gettext -l ja

Translate manually PO files. Open the PO file and add translated message after each "msgstr".

After manually translation, execute the following command.

.. code-block:: shell

    make -e SPHINXOPTS="-D language='ja'" html

If you update the document, you can update PO files with *sphinx-intl update* command.

.. code-block:: shell

    sphinx-intl update -p _build/gettext