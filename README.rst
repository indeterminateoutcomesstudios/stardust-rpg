Stardust RPG
============

.. image:: https://travis-ci.org/johnthagen/stardust-rpg.svg
    :target: https://travis-ci.org/johnthagen/stardust-rpg

.. image:: https://codeclimate.com/github/johnthagen/stardust-rpg/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/stardust-rpg

.. image:: https://codeclimate.com/github/johnthagen/stardust-rpg/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/stardust-rpg

.. image:: https://img.shields.io/pypi/v/stardust-rpg.svg
    :target: https://pypi.python.org/pypi/stardust-rpg

.. image:: https://img.shields.io/pypi/status/stardust-rpg.svg
    :target: https://pypi.python.org/pypi/stardust-rpg

.. image:: https://img.shields.io/pypi/pyversions/stardust-rpg.svg
    :target: https://pypi.python.org/pypi/stardust-rpg/

.. image:: https://img.shields.io/pypi/dm/stardust-rpg.svg
    :target: https://pypi.python.org/pypi/stardust-rpg/

Stardust RPG is a tactical d20 role-playing game designed to provide a variety of progression
options for players and encourage teamwork.  Baseline content is based off the Stardust book
series by John Hagen, but is adaptable to a variety of fantasy settings.

Features
--------

- Cross platform.  Run the server on any platform that supports Python.  Clients can
  connect and manage their characters using a standard web browser with no install required.
- Roll20 integration. Players can to automatically sync their character stats and
  automatically generated weapon and ability macros right into a Roll20 campaign. Special thanks
  to `@theandrewdavis <https://github.com/theandrewdavis>`_ for his analysis of the roll20.net API.
- Extensible. Easily add new content, such as classes, weapons, or abilities.
- Persistent. Store characters in a persistent database for easy reuse.

Usage
=====

Installation
------------

You can install, upgrade, and uninstall ``stardust-rpg`` with these commands:

.. code:: shell-session

    $ pip3 install stardust-rpg
    $ pip3 install --upgrade stardust-rpg
    $ pip3 uninstall stardust-rpg

Configuration
-------------

Initialize the database:

.. code:: shell-session

    $ stardust-rpg makemigrations
    $ stardust-rpg migrate

Create an admin account:

.. code:: shell-session

    $ python manage.py createsuperuser

Start the server:

.. code:: shell-session

    $ stardust-rpg runserver 0.0.0.0:80

Game Setup
----------

Log into the admin interface by browsing to http://localhost/admin

Add ``Users`` for each player.  Configure the following fields:

======================= ==============================================
Field                   Value
======================= ==============================================
``Email Address``       Player's Roll20 email address.
======================= ==============================================

Add ``Characters`` for each character in the game.  Configure the following fields:

======================= ==============================================
Field                   Value
======================= ==============================================
``User``                Player who has modification rights to the character.
``Name``                Name of the character.  Must match name of character in Roll20.
``Roll20 campaign id``  The 6 digit ID assigned to the campaign (e.g. https://app.roll20.net/campaigns/details/ID/CAMPAIGN_NAME)
``Class``               The class assigned to this ``Character``.
======================= ==============================================

Rules
=====

Combat
------

Combat Round (``RND``)
~~~~~~~~~~~~~~~~~~~~~~

#. At the start of combat, roll a d20 + Maximum Speed (``SPEED``) to determine turn order.

    #. If your character is surprised, take no actions during the first ``RND``.

#. Do the following actions in any order. A Full Action (``FullA``) requires consuming all these
   actions. A Free Action (``FreeA``) does not consume any of these actions.

    #. Move Action (``MovA``)

        #. Move your character up to Maximum Speed (``SPEED``).

            #. You may move through squares occupied by allies, but may not move through grid
               squares occupied by enemies.

        #. After performing a ``StdA`` or ``AbA``, you may consume the remaining ``SPEED`` that has
           not be used during this ``RND``.

    #. Standard Action (``StdA``)

        #. Perform a single melee or ranged weapon attack

            #. Roll a d20 and ``PDAM`` dice.  If d20 + ``PAC`` ≥ target ``PDEF``, apply ``PDAM``.

                #. If d20 ≥ Critical Range (``CRAN``), automatic hit, apply CDAM.
                #. if d20 = 1, automatic miss.

    #. Ability Action (``AbA``)

        #. Cast a single ability that requires ``AbA``

            #. Subtract the MP Cost from your Current ``MP``.  Current ``MP`` cannot drop below 0.
            #. Roll a d20 and ``MDAM`` dice. If d20 + ``MAC`` ≥ target ``MDEF``, apply
               ``MDAM`` and Effect.

                #. If d20 = 20, automatic hit, choose one of the following:
                   2x [``MDAM``, Effect, Area, OR Duration].

                #. If d20 = 1, automatic miss.

#. At the conclusion of your turn, roll a d20 and Regeneration Dice (``RD``)

    #. If d20 ≥ Magic Regeneration (``REG``), restore ``RD`` MP.

        #. If d20 = 20, restore 2x ``RD`` MP.
        #. If d20 = 1, automatic failure.

Incapacitation (``KO``)
~~~~~~~~~~~~~~~~~~~~~~~

- If ``HP`` ≤ 0, unconscious status.
- If ``HP`` ≤ -(50% Maximum ``HP``), death status.

Status Effects
~~~~~~~~~~~~~~

=========== ==========================================================================
Status      Effect
=========== ==========================================================================
Immobilize  Cannot take ``MovA``.
Silence     Cannot take ``AbA`` (i.e. any action that targets with MAC or consumes MP).
Stagger     Cannot perform physical attacks.
Disable     Cannot take ``StdA``.
Stun        Cannot take ``MovA`` or ``StdA``.
Sleep       Cannot take ``MovA`` or ``StdA``.  Woken by physical or magical attack.
Fear        Must expend ``MovA`` to move in opposite direction of the source of fear.
Allure      Must expend ``MovA`` to move towards the source of the allure.
Blind       Maximum range of physical and magic attacks reduced to 1.
Unconscious Cannot take anymore actions until revived.
Death       Creature is dead.
=========== ==========================================================================

Vulnerabilities and Resistances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======================= ==============================================
Status                  Effect
======================= ==============================================
Vulnerability (``VUL``) Take 2x from a particular damage type.
Resistance (``RES``)    Take ½ from a particular damage type.
Immunity (``IMU``)      Take no damage from a particular damage type.
======================= ==============================================

Skills
------

======================= ============================================================
Skill                   Effect
======================= ============================================================
Athletics (``ATH``)     Climb, Jump, Swim, Grapple, Reflex, Balance, Fall
Stealth (``STE``)       Sneak, Hide, Sleight of Hand, Disguise, Escape, Detect Trap
Fortitude (``FOR``)     Endurance, Resist Status Effect, Death Save, Survival
Aptitude (``APT``)      Heal, Operate Device, Pick Lock, Forgery, Scan, Utility
Perception (``PER``)    Spot, Listen, Search, Touch, Smell, Taste
Speech (``SPE``)        Diplomacy, Intimidate, Bluff, Persuasion
======================= ============================================================

Releases
========

1.0.0
-----

- Initial Release

TODO
====

Features
--------

- Handle exceptions in a user-friendly way.
- Show only equipable items.
- Utility macros.
- Set bonuses.
- Vulnerabilities and resistances.
- Inventory
- Shops
- Parties
- Weapon / Ability DPS
- Add equation help for how stats are calculated

Technical Debt
--------------

- Break views into multiple modules.
- Switch to logging module.
- Add unit tests