Build desktop app with electron and react
=========================================

Setup
-----

Create a project folder
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    npx crate-react-app --template typescript PROJECT_APP_NAME

The configuration of the project directory created is the following.

::

    PROJECT_APP_NAME
    |- node_modules
    |- public
    |- src
    |- .gitignore
    |- package-lock.json
    |- package.json
    |- tsconfig.json
    `- README.md


Install Recoil
^^^^^^^^^^^^^^

*Recoil* is a state management library for React.
To install the latest stable version, run the following command.

.. code-block:: shell

    npm install recoil


Install tailwindcss
^^^^^^^^^^^^^^^^^^^

Run the following command in the project folder.

.. code-block:: shell

    npm install -D tailwindcss postcss autoprefixer

After installing tailwindcss modules, execute the following command which creates config files for tailwindcss.

.. code-block:: shell

    npx tailwindcss init -p

Edit *tailwindcss.config.js* as the followings.

.. code-block:: javascript
    :caption: tailwindcss.config.js

    /** @type {import('tailwindcss').Config} */ 
    module.exports = {
    content: [
        "./src/**/*.{js,ts,jsx,tsx}",
        "./pages/**/*.{js,ts,jsx,tsx}",
        "./components/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
    }

Add the followings to *src/index.css*, which activates tailwindcss.

.. code-block:: css
    :caption: src/index.css

    @tailwind base;
    @tailwind components;
    @tailwind utilities;


Install axious
^^^^^^^^^^^^^^

Install axious by the following command.

.. code-block:: shell

    npm install axious


Install electron
^^^^^^^^^^^^^^^^

Run the following command in the PROJECT_APP_NAME directory.

.. code-block:: shell

    npm install -D electron electron-builder

Modify *package.json*.

.. code-block:: json

    {
        "main": "build/electron/core/main.js",
        "homepage": "./",
        "build": {
            "extends": null,
            "files": [
            "build/**/*"
            ]
        },
        "script": {
            "electron:start": "npm run build && tsc -p electron && electron .",
            "electron:build": "npm run build && tsc -p electron && electron-builder"
        }
    }

Crate *electron* directory and files in the project root.
The configuration is the following.

::

    electron
    |- core
    |  `- main.ts
    `- tsconfig.json

.. code-block:: json
    :caption: electron/tsconfig.json

    {
    "compilerOptions": {
        "target": "es5",
        "outDir": "../build",
        "rootDir": "../"
    },
    "include": [
        "src/**/*"
    ]
    }

.. code-block:: typescript
    :caption: main.ts

    import { app, BrowserWindow } from "electron";
    import * as path from "path";

    const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        }
    });

    win.loadFile("./build/index.html");
    };

    app.whenReady().then(() => {
    createWindow();

    app.on("activate", () => {
        if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
        }
    });
    });

    app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
    });
