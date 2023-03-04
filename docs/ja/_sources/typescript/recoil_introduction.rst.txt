Introduction to Recoil
======================

*Recoil* is a state management library for React.


Install Recoil
--------------

To install the latest stable version, run the following command.

.. code-block:: shell

    npm install recoil

State management with Recoil
----------------------------

The following steps are needed to management states.

1. Put `Recoil Root` to your root component.
2. Create `atom` files.
3. Put 'useRecoilState' to your component files.

Recoil Root
^^^^^^^^^^^

Edit `src/App.tsx`, add `Recoil Root` as the followings.

.. code-block:: jsx
    :caption: src/App.tsx

    import { RecoilRoot } from "recoil";

    function App() {
    return (
        <RecoilRoot>
            ...
        </RecoilRoot>
    );
    };

    export default App;

Atom File
^^^^^^^^^

Create `atom` file.

.. code-block:: typescript
    :caption: src/atoms/atomMode.ts

    import { atom } from "recoil";

    export const atomMode = atom({
    key: "atomMode",
    default: "Data",
    });


State management hooks
^^^^^^^^^^^^^^^^^^^^^^

Use `useRecoilState` as like `useState`. A exmaple is the following.

.. code-block:: jsx

    import {useRecoilState} from 'recoil';
    import {atomMode} from "../atoms/atomMode"

    export const SomeCompoent = () => {

        const [mode, setMode] = useRecoilState<string>(atomMode);

        const onClick = () => {
            setMode("Help");
        }

        return (
            ...
            {mode}
            <button onClick={onClick}>Change Mode</button>
            ...
        )
    }

Read only / Write only hooks
----------------------------

Use `useRecoilValue` if you only read the state value.
On the other hand, use 'useSetRecoilState' if you only write the state value.
