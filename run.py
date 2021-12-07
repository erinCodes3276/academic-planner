
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
B_102 = BasicPropositions("B_102")
B_103 = BasicPropositions("B_103")
B_112 = BasicPropositions("B_112")
B_218 = BasicPropositions("B_218")
B_205 = BasicPropositions("B_205")
B_331 = BasicPropositions("B_331")
B_334 = BasicPropositions("B_334")

C_121 = BasicPropositions("C_121")
C_124 = BasicPropositions("C_124") 
C_203 = BasicPropositions("C_203")
C_204 = BasicPropositions("C_204") 
C_221 = BasicPropositions("C_221")
C_223 = BasicPropositions("C_223") 
C_235 = BasicPropositions("C_235")
C_271 = BasicPropositions("C_271") 
C_320 = BasicPropositions("C_320") 
C_330 = BasicPropositions("C_330")
C_332 = BasicPropositions("C_332") 
C_352 = BasicPropositions("C_352") 
C_360 = BasicPropositions("C_360")
C_365 = BasicPropositions("C_365") 
C_471 = BasicPropositions("C_471") 
C_472 = BasicPropositions("C_472") 
C_497 = BasicPropositions("C_497")
C_499 = BasicPropositions("C_499") 

T_111 = BasicPropositions("M_111")
T_120 = BasicPropositions("M_120")

S_263 = BasicPropositions("S_263")

A = BasicPropositions("A")
D = BasicPropositions("D")

B_1 = BasicPropositions("B_1")
B_2 = BasicPropositions("B_2")
B_3 = BasicPropositions("B_3")
B_4 = BasicPropositions("B_4")

C_1 = BasicPropositions("C_1")
C_2 = BasicPropositions("C_2")
C_3 = BasicPropositions("C_3")
C_4 = BasicPropositions("C_4")

T_1 = BasicPropositions("B_1")

FIRST = BasicPropositions("FIRST")
SECOND = BasicPropositions("SECOND")
THIRD = BasicPropositions("THIRD")
FOURTH = BasicPropositions("FOURTH")


# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint(C_320 >> C_235)
    E.add_constraint(C_330 >> (C_121 & C_271))
    E.add_constraint(C_332 >> (C_124 & M_111))
    E.add_constraint(C_352 >> C_235)
    E.add_constraint(C_360 >> (C_124 & C_204))
    E.add_constraint(C_365 >> (C_204 & C_235))
    E.add_constraint(C_471 >> (C_271 & C_352 & C_365))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
