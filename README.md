# affix-count
simple counter of  prefixes, suffixes, and infixes in a text file, with some allomorphy

use from command line as:

<code> python affcount.py filename sequence of affixes </code>

where <code> filename</code> is the name of the text file, and

<code> sequence of affixes</code> is space-separated prefix, suffix or infix.

Prefixes end with dash, suffixes start with it, and infixes start and end with it, for example <code>re-, -ness, -bloody-</code>. We remove the dash before we search the forms.

<code>affcount2.py</code> is for Python 2, <code>affcount3.py</code> is for Python 3, whatever that mess means in a messy PL.

Use the one you need in the examples below.

examples:

<code>python affcount.py README.md -xes -er file- -fix- </code>

<code> python affcount.py fn -ler -lar </code>  in a Turkish text file <code>fn</code>, will print allomorphic count of the plural.

Caveat: These aren't *really* allomorphic counts because we don't do anything with semantics. We just look at the position of
the "affixal form" in a word. For example, the word `kiler' (cellar) in Turkish is not plural, although -ler looks like a "suffix" and counts as such by the program.
