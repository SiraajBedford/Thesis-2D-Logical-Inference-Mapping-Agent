from classes.logic_engine import atomic
import itertools
import ttg

Atom=atomic()  
Atom.add_atomic('P', True)
Atom.add_atomic('Q', True)
Atom.print_atomic_dictionary()


table = list(itertools.product([False, True], repeat=2))
print(table)
print(table[3][0] and table[3][1])


print(ttg.Truths(['p', 'q', 'r']))


eval=ttg.Truths(['p', 'q', 'r'], ['p and q and r', 'p or q or r', '(p or (~q)) => r'])
tabl=eval.as_tabulate()
print(tabl)