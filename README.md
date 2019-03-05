# affix-count
simple counter of  prefixes, suffixes, and infixes in a text or xml file, with some allomorphy

For plain text:

<code> python affcount3.py filename sequence of affixes </code>

For text in xml files:

<code> python affcount3-xml.py filename sequence of affixes </code>

where <code> filename</code> is the name of the text file, and

<code> sequence of affixes</code> is space-separated prefix, suffix or infix.

Prefixes end with dash, suffixes start with it, and infixes start and end with it, for example <code>re-, -ness, -bloody-</code>. We remove the dash before we search the forms.

<code>affcount2.py</code> is for Python 2, and <code>affcount3.py</code> for Python 3, whatever that means in a messy PL.

Examples:

<code>python affcount2.py README.md -xes -er file- -fix- </code>

<code>python3 affcount3.py README.md -xes -er file- -fix- </code>

<code>python3 affcount3-xml.py fn.xml -xes -er file- -fix- </code>

<code>python affcount2.py fn -ler -lar </code>  in a Turkish text file <code>fn</code>, will print allomorphic count of the plural.

Caveat: These aren't *really* allomorphic counts because we don't do anything with semantics. We just look at the position of
the "affixal form" in a word. For example, the word `kiler' (cellar) in Turkish is not plural, although -ler looks like a "suffix" and counts as such by the program.
