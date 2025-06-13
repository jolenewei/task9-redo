% Robot access rules in a smart facility

robot(bolt).
robot(iris).
robot(zen).

zone(lab).
zone(vault).
zone(storage).

can_access(bolt, lab).
can_access(iris, storage).
can_access(zen, vault).
restricted(vault).

verify(Query) :- call(Query), write('true'), nl.
verify(_) :- write('false'), nl.
