# affix-count
simple counter of  prefixes, suffixes, and infixes in a text file, with some allomorphy

use from command line as:

<code> python affcount.py filename sequence of affixes </code>

where <code> filename</code> is the name of the text file, and

<code> sequence of affixes</code> is space-separated prefix, suffix or infix.

Affcount2.py is for Python 2, Affcount3.py is for Python 3, whatever that mess is.

Use the one you need in the examples below.

examples:

<code>python affcount.py README.md -xes -er file- -fix- </code>

<code> python affcount.py fn -ler -lar </code>  in a Turkish text file <code>fn</code>, will print allomorphic count of the plural.

Caveat: These aren't *really* allomorphic counts because we don't do anything with semantics. We just look at the position of
the "affixal form" in a word. For example, the word `kiler' (cellar) in Turkish has no plural, although -ler looks like a "suffix" and counts as such by the program.
