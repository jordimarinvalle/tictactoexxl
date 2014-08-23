TicTacToeXXL
============

.. image:: https://api.travis-ci.org/jordimarinvalle/tictactoexxl.png
        :target: https://secure.travis-ci.org/jordimarinvalle/tictactoexxl


TicTacToeXXL is a tic-tac-toe game with xxl fun. The rules are the same, but there are not fixed elements -- you can create a tic-tac-toe game with **multiple players** on a **n*m grid** and the first player who **strikes 'x' movements in a row** (vertical/horizontal/diagonal) wins the game. Simple as playing a tic-tac-toe game but with xxl fun.


Installation
------------

Manual
~~~~~~
For a manual installation, do as usual and execute the following -- unpack it, go to unpacked directory and run setup.py install

.. code:: bash

    tar zxf tictactoexxl-{VERSION}.tar.gz
    cd tictactoexxl-{VERSION}/
    python setup.py install


PIP
~~~
For a pip installation, just ``pip install tictactoexxl``

.. code:: bash

    $ pip install tictactoexxl


Play
----
Once installed, just type ``tictactoexxl-play.py`` but it will no provide you xxl fun. Check tictactoexxl help ``tictactoexxl-play.py --help`` to customice your tic-tac-toc game, e.g.:

.. code:: bash

    tictactoexxl-play.py -p3 -x5 -y5 -w4


If a game constraint is not provided, the corresponding one of standard tic-tac-toe game will be set. ``tictactoexxl-play.py -x5 -y5 -w4`` will set a default param `-p2` that represents that the game will be set for two players.


Support
-------
Python 2.7 and 3.4 versions have been tested with success.


License
-------
MIT License, so you can sell tictactoexxl package and no one will charge you for your action. ;)


Testing
-------

.. code:: bash

    pip install pytest coverage pytest-cov tox


Please install ``tox`` and ``pytest`` to test tictactoexxl package -- ``coverage`` and ``pytest-cov`` are not required to run the tests. Just simply run ``tox`` on the tictactoexxl root directory and it will run the tests, ``python setup.py test`` will also provide the same feedback.


Skills Proof / Cheat Style
--------------------------

TicTacToeXXL has been created to be applied as a proof of my personal Python development practices/knowledge and prove myself to create/distribute a Python package from scratch.

If you need to create a tic-tac-toe game to submit it on a job appliance, bachelor course, university master, however, please do not cheat, and leave any temptation to read / copy tictactoexxl code. It will not be the way. Be honest, do not cheat yourself and the code reviewer who might face your truth.
