# -*- coding: utf-8 -*-
## Filename    : TestCLUnfolder.py
## Author(s)   : Michel Le Borgne
## Created     : 13 sept. 2012
## Revision    :
## Source      :
##
## Copyright 2012 : IRISA/IRSET
##
## This library is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published
## by the Free Software Foundation; either version 2.1 of the License, or
## any later version.
##
## This library is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY, WITHOUT EVEN THE IMPLIED WARRANTY OF
## MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.  The software and
## documentation provided here under is on an "as is" basis, and IRISA has
## no obligations to provide maintenance, support, updates, enhancements
## or modifications.
## In no event shall IRISA be liable to any party for direct, indirect,
## special, incidental or consequential damages, including lost profits,
## arising out of the use of this software and its documentation, even if
## IRISA have been advised of the possibility of such damage.  See
## the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this library; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
##
## The original code contained here was initially developed by:
##
##     Michel Le Borgne.
##     IRISA
##     Symbiose team
##     IRISA  Campus de Beaulieu
##     35042 RENNES Cedex, FRANCE
##
##
## Contributor(s):
##
"""Unitary Test of the unfolder"""
from __future__ import print_function
import unittest
import pytest
import pkg_resources

from cadbiom.models.guard_transitions.chart_model import ChartModel
from cadbiom.models.clause_constraints.CLDynSys import Literal, Clause
from cadbiom.models.guard_transitions.analyser.ana_visitors import TableVisitor
from cadbiom.models.clause_constraints.CLDynSys import CLDynSys
from cadbiom.models.clause_constraints.mcl.MCLTranslators import GT2Clauses
from cadbiom.models.clause_constraints.mcl.CLUnfolder import CLUnfolder

from cadbiom.models.clause_constraints.mcl.MCLAnalyser import MCLAnalyser
from cadbiom.models.clause_constraints.mcl.MCLQuery import MCLSimpleQuery


class ErrorReporter(object):
    """error reporter of the compil type"""
    def __init__(self):
        self.context = ""
        self.error = False
        pass

    def display(self, mess):
        """
        just printing
        """
        self.error = True
        print('\n>> '+self.context+"  "+mess)

    def display_info(self, mess):
        """
        just printing
        """
        print('\n-- '+mess)

    def set_context(self, cont):
        """
        for transition compiling
        """
        self.context = cont

# helper functions

def string_to_clause(text_clause):
    """
    text_clause is a string such that "a,not b,not c"
    it is transformed in the corresponding clause
    WARNING: strict syntax - no check - for tests
    """
    # split into literals
    clause = Clause([])
    llit = text_clause.split(',')
    # translate each literal
    for lit in llit:
        spl = lit.split()
        if len(spl) == 1: # "a"
            clause.add_lit(Literal(spl[0], True))
        else: # "not a"
            clause.add_lit(Literal(spl[1], False))
    return clause

def model1():
    """
    A simple ChartModel with two nodes and a transition
    """
    # build dynamical system
    model = ChartModel("Test")
    root = model.get_root()
    node_1 = root.add_simple_node('n1', 0, 0)
    node_2 = root.add_simple_node('n2', 0, 0)
    root.add_transition(node_1, node_2)
    return model

def model2():
    """
    ChartModel model1 + 3 nodes and 2 transitions and a cycle without start
    """
    # build dynamical system
    model = model1()
    root = model.get_root()
    node_3 = root.add_simple_node('n3', 0, 0)
    node_4 = root.add_simple_node('n4', 0, 0)
    root.add_transition(node_3, node_4)
    node_5 = root.add_simple_node('n5', 0, 0)
    root.add_transition(node_4, node_5)
    root.add_transition(node_5, node_3)
    return model

def model3():
    """
    ChartModel model2 + 1 node + 1 start node and a transition
    """
    # build dynamical system
    model = model2()
    root = model.get_root()
    node_s = root.add_start_node('n3', 0, 0)
    node_3 = model.get_simple_node('n3')
    root.add_transition(node_s, node_3)
    return model

def model4():
    """
    ChartModel with:
        - 1 input node: in1
        - 5 nodes: n1, n2, n3, n4, n5
        - 5 transitions: n1-n2, n3-n4, n4-n5, n5-n3, in1-n1
        - 2 free clocks: hh1: (n3 or n4) on n1-n2, hh2: (n1 and n3) on n4-n5
    """
    model = ChartModel("Test")
    root = model.get_root()
    node_1 = root.add_simple_node('n1', 0, 0)
    node_2 = root.add_simple_node('n2', 0, 0)
    tr0 = root.add_transition(node_1, node_2)
    tr0.set_event('hh1')
    tr0.set_condition("n3 or n4")
    node_3 = root.add_simple_node('n3', 0, 0)
    node_4 = root.add_simple_node('n4', 0, 0)
    root.add_transition(node_3, node_4)
    node_5 = root.add_simple_node('n5', 0, 0)
    tr1 = root.add_transition(node_4, node_5)
    root.add_transition(node_5, node_3)
    tr1.set_event("hh2")
    tr1.set_condition("n1 and n3")
    node_i =  root.add_input_node('in1', 0, 0)
    tri = root.add_transition(node_i, node_1)
    tri.set_condition("n5")

    # Frontier test: Add a start node on n3 or do not attempt any frontier
    # place because there is a SCC composed of n3, n4, n5.
    #node_s = root.add_start_node('s1', 0, 0)
    #root.add_transition(node_s, node_3)

    return model

def create_unfolder(model):
    """Return an unfolder for the given model"""
    tvisit = TableVisitor(None) # no error display
    model.accept(tvisit)
    cld = CLDynSys( tvisit.tab_symb, None)
    reporter = ErrorReporter()
    cvisit = GT2Clauses(cld, reporter, True)
    model.accept(cvisit)
    # unfolder
    return CLUnfolder(cld)

@pytest.fixture()
def textual_properties():
    """start, invariant, final"""
    return (
        ("M", "L", "C"), # No solution (M activated)
        ("", "L", "C and K"), # Solution: I E D F
        ("", "", "C"), # Solutions: F E L D, I E D F
    )

@pytest.fixture()
def numerical_properties():

    return (
        ([[13]], [[12]], [[3]]),
        ([], [[12]], [[3, -47], [11, -47], [-3, -11, 47], [47]]),
    )

@pytest.fixture()
def feed_mclanalyser():
    """Setup MCLAnalyser with a bcx model"""
    rep = ErrorReporter()
    # Force __var_list to be sorted at the output of base_var_set from
    # CLDynSys for reproductibility in tests (literals naming)
    mcla = MCLAnalyser(rep, debug=True)
    filename = pkg_resources.resource_filename(
        __name__, # package name
        "examples/example_model.bcx"
    )
    mcla.build_from_chart_file(filename)
    return mcla


class TestCLUnfolder(unittest.TestCase):
    """
    Test public and some private methods (test_method form)
    """
    def test_var_name(self):
        """
        Test of variables at initial state uncoding and decoding
        """
        model = model1()
        unfolder = create_unfolder(model)

        # Test unfolder init and internal dynamic system
        assert unfolder._CLUnfolder__shift_step == 2
        assert unfolder.shift_step_init == 2
        assert unfolder.get_var_number() == 2

        # naming and coding variables
        cn1 = unfolder.var_dimacs_code('n1')
        cn2 = unfolder.var_dimacs_code('n2')

        res = unfolder.get_var_name(cn1) == 'n1'
        res = res and (unfolder.get_var_name(cn2) == 'n2')
        self.assert_(res,'Error in variable name 1')

        res = unfolder.get_var_name(7) == 'n1'
        self.assert_(res,'Error in variable name 2')
        res = unfolder.get_var_name(8) == 'n2'
        self.assert_(res,'Error in variable name 3')

        res = unfolder.get_var_indexed_name(7) == 'n1_3'
        self.assert_(res,'Error in variable name 4')
        res = unfolder.get_var_indexed_name(8) == 'n2_3'
        self.assert_(res,'Error in variable name 5')

        # Test number of variables
        assert unfolder.get_system_var_number() == unfolder.get_var_number()


    def test_frontier(self):
        """
        Test frontier computation and encoding
        """
        ## model1
        model = model1()
        unfolder = create_unfolder(model)
        # test frontier: should be n1
        frontier_value = unfolder.frontier_values[0]
        res = unfolder.get_var_name(frontier_value) == 'n1'
        res = res and (len(unfolder.frontier_values) == 1)
        self.assert_(res,'Error in frontier: model1')

        ## model2 (one cycle without start)
        model = model2()
        unfolder = create_unfolder(model)

        # test frontier: should be n1
        frontier_value = unfolder.frontier_values[0]
        res = unfolder.get_var_name(frontier_value) == 'n1'
        res = res and (len(unfolder.frontier_values) == 1)
        self.assert_(res,'Error in frontier: model2')

        ## model3: same as model2 but with a start on n3
        model = model3()
        unfolder = create_unfolder(model)

        # test frontier - should be {n1, n3}
        frontier_values = unfolder.frontier_values
        res = len(frontier_values) == 2
        res = res and unfolder.get_var_name(frontier_values[0]) == 'n1'
        res = res and unfolder.get_var_name(frontier_values[1]) == 'n3'
        self.assert_(res,'Error in frontier: model3')

        ## model4 - No frontiers (even if we can get input node in1 in the solutions)
        model = model4()
        unfolder = create_unfolder(model)
        res = len(unfolder.frontier_values) == 0
        self.assert_(res,'Error in frontier: model4')


    def test_free_clocks_inputs(self):
        """
        test on free clocks and input computation
        """
        # model3: no free clock, no input
        model = model3()
        unfolder = create_unfolder(model)
        lfc = unfolder.get_free_clocks()
        res = len(lfc) == 0
        self.assert_(res,'Error in free clocks: model3')
        lin = unfolder.get_inputs()
        res = len(lin) == 0
        self.assert_(res,'Error in inputs 1')

        # model4: two free clocks and one input
        model = model4()
        unfolder = create_unfolder(model)
        lfc = unfolder.get_free_clocks()
        res = len(lfc) == 2
        found_names = {unfolder.get_var_name(clock) for clock in lfc}
        res = found_names == {'hh2', 'hh1'}
        self.assert_(res,'Error in free clocks: model4')
        lin = unfolder.get_inputs()
        res = len(lin) == 1
        found_names = {unfolder.get_var_name(inpt) for inpt in lin}
        res = found_names == {'in1'}
        self.assert_(res,'Error in inputs: model4')




def init_forward_unfolding_part_1(unfolder):
    """Initialization step only"""

    unfolder._CLUnfolder__shift_direction = 'FORWARD'
    unfolder._CLUnfolder__current_step = 1
    unfolder._CLUnfolder__shift_step = unfolder.shift_step_init  # back to basic!
    unfolder._CLUnfolder__aux_code_table = dict()            # flush auxiliary variables
    unfolder._CLUnfolder__aux_list = []                      # idem

    # Init properties to generate all variable num codes
    unfolder._CLUnfolder__init_initial_constraint_0()
    unfolder._CLUnfolder__init_final_constraint_0()
    unfolder._CLUnfolder__init_invariant_constraint_0()
    unfolder._CLUnfolder__init_variant_constraints_0()

def init_forward_unfolding_part_2(unfolder):
    """Shift step only"""

    # Now shifting is possible
    unfolder._CLUnfolder__forward_init_dynamic()
    unfolder._CLUnfolder__shift_final()
    unfolder._CLUnfolder__shift_invariant()
    # PS: __variant_constraints si already initialized for the first step.

def test_init_unfolder(feed_mclanalyser):

    mcla = feed_mclanalyser
    unfolder = mcla.unfolder # shortcut

    # Initialization step only
    init_forward_unfolding_part_1(mcla.unfolder)

    ## Test CLDynSys
    # 15 places
    assert unfolder.get_var_number() == 46

    # __var_list is built on casted set; MCLAnalyser is un debug mode
    # so the list is sorted
    expected = [
        '##',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P',
        '_h2', '_h3', '_h4', '_h5', '_h6', '_h7', '_h_0', '_h_1', '_lit0', '_lit1',
        '_lit10', '_lit11', '_lit12', '_lit13', '_lit14', '_lit15', '_lit16',
        '_lit17', '_lit18', '_lit19', '_lit2', '_lit20', '_lit21', '_lit22',
        '_lit3', '_lit4', '_lit5', '_lit6', '_lit7', '_lit8', '_lit9'
    ]

    print(unfolder._CLUnfolder__var_list)
    assert unfolder._CLUnfolder__var_list == expected

    ## Test mapping of variables names to values
    expected_var_code_table = {
        '_lit22': 39, '_lit20': 37, '_lit21': 38, '_lit19': 35,
        '_lit18': 34, '_lit6': 43, '_lit17': 33, '_lit13': 29, '_lit9': 46,
        '_lit8': 45, '_h_0': 22, '_h_1': 23, '_lit16': 32, '_lit12': 28,
        '_lit3': 40, '_lit2': 36, '_lit1': 25, '_lit0': 24, '_lit7': 44,
        '_lit11': 27, '_lit5': 42, '_lit4': 41,
        'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8,
        'K': 11, 'J': 10, 'M': 13, 'L': 12, '_lit15': 31, 'N': 14, 'P': 15,
        '_lit14': 30, '_h4': 18, '_h5': 19, '_h6': 20, '_h7': 21, '_h2': 16,
        '_h3': 17, '_lit10': 26
    }

    # Check presence of all basic literals (not future ones with "`" added)
    found_var_code_table = list(unfolder._CLUnfolder__var_code_table.items())
    print(found_var_code_table)
    for lit_name_val in expected_var_code_table.items():
        assert lit_name_val in found_var_code_table

    # var_code_table is twice as big as __var_list items
    # (future literals with "`" are added)
    assert len(found_var_code_table) == 2 * len(expected_var_code_table)

    ## Test frontiers, places, values and names
    print("Frontier values", unfolder.frontier_values)
    assert set(unfolder.frontier_values) == {4, 5, 6, 7, 9, 12, 14} # D E F G I L N

    frontiers_values_mapping = {
        value: unfolder.get_var_name(value) for value in unfolder.frontier_values
    }
    print("Frontiers values mapping", frontiers_values_mapping)
    assert frontiers_values_mapping == {4: 'D', 5: 'E', 6: 'F', 7: 'G', 9: 'I', 12: 'L', 14: 'N'}

    found = unfolder.frontiers_negative_values
    print("Frontiers negatives values", found)
    assert found == frozenset([-14, -12, -9, -7, -6, -5, -4])

    found = unfolder.frontiers_pos_and_neg
    assert found == frozenset([4, 5, 6, 7, 9, 12, 14, -14, -12, -9, -7, -6, -5, -4])

    # Check clocks
    free_clocks = unfolder._CLUnfolder__free_clocks
    print("Free clocks/events", free_clocks)
    assert free_clocks == frozenset([16, 17, 18, 19, 20, 21, 22, 23])

    clocks_values_mapping = {
        value: unfolder.get_var_name(value) for value in unfolder._CLUnfolder__free_clocks
    }
    print("Clocks values mapping", clocks_values_mapping)
    assert clocks_values_mapping == {16: '_h2', 17: '_h3', 18: '_h4', 19: '_h5', 20: '_h6', 21: '_h7', 22: '_h_0', 23: '_h_1'}

    # Check input places
    assert unfolder._CLUnfolder__inputs == frozenset()

    # Not frontiers: A B C H J K M P
    found = unfolder._CLUnfolder__no_frontier_init
    print("Places not frontiers", found)
    assert found == [[-1], [-2], [-3], [-8], [-10], [-11], [-13], [-15]]



def test_init_forward(feed_mclanalyser, textual_properties, numerical_properties):
    """Test forward initialization for various models and properties types

    Specific call:
    pytest cadbiom/models/clause_constraints/mcl/TestCLUnfolder.py::test_init_forward

    Query attributes:
    self.dim_start = []         # list<DClause>
    self.dim_inv = []           # list<DClause>
    self.dim_final = []         # list<DClause>
    self.dim_variant_prop = []  # list<list<DClause>>

    CLUnfolder attributes that contain query attributes:
    self.__initial_property = None            # logical formula - literal boolean expression
    self.__dimacs_initial = None              # list of DIMACS clauses
    self.__final_property = None              # logical formula
    self.__dimacs_final = None                # list of DIMACS clauses
    self.__invariant_property = None          # logical formula
    self.__dimacs_invariant = None            # list of DIMACS clauses
    self.__variant_property = None            # list<logic formulas>
    self.__dimacs_variant = None              # list<list<DIMACS clauses>>

    CLUnfolder attributes that contain clauses:
    self.__list_variant_constraints = None    # list<list<DIMACS clauses>>

    dynamic_constraints => __dynamic_constraints
    initial_constraints => __initial_constraints
    invariant_constraints => __invariant_constraints
    variant_constraints => __variant_constraints
    final_constraints => __final_constraints

    Mangling prefix: unfolder._CLUnfolder

    TODO:
        - search solutions for the given properties
        - test variant properties
    """
    mcla = feed_mclanalyser

    ## First properties
    ### Textual properties
    start, invariant, final = textual_properties[0]

    query = MCLSimpleQuery(start, invariant, final)
    mcla.unfolder.init_with_query(query)

    init_forward_unfolding_solution_1(mcla)
    ## TODO: search sol

    ### DIMACS properties
    dim_start, dim_inv, dim_final = numerical_properties[0]
    query = MCLSimpleQuery(None, None, None)
    query.dim_start = dim_start
    query.dim_inv = dim_inv
    query.dim_final = dim_final
    mcla.unfolder.init_with_query(query)
    init_forward_unfolding_solution_1(mcla)


    ## Second properties
    ### Textual properties
    start, invariant, final = textual_properties[1]

    query = MCLSimpleQuery(start, invariant, final)
    mcla.unfolder.init_with_query(query)

    init_forward_unfolding_solution_2(mcla)
    ## TODO: search sol

    ### DIMACS properties: TODO: marche pas: les litéraux supplémentaires ne sont pas pris en compte...
    dim_start, dim_inv, dim_final = numerical_properties[1]
    query = MCLSimpleQuery(None, None, None)
    query.dim_start = dim_start
    query.dim_inv = dim_inv
    query.dim_final = dim_final
    mcla.unfolder.init_with_query(query)
    init_forward_unfolding_solution_2(mcla)



def init_forward_unfolding_solution_1(mcla):
    """
    - Test first part of init_forward_unfolding: init of constraints
    - Test second part of init_forward_unfolding: shift of initialized constraints

    ("M", "L", "C"), # No solution (M activated)
    """
    unfolder = mcla.unfolder # shortcut
    init_forward_unfolding_part_1(mcla.unfolder)

    ############################################################################

    print(unfolder.dynamic_constraints)
    print(unfolder.initial_constraints)
    print(unfolder.invariant_constraints)
    print(unfolder.variant_constraints)
    print(unfolder.final_constraints)

    # No auxiliary variables
    assert unfolder._CLUnfolder__aux_code_table == dict()
    assert unfolder._CLUnfolder__aux_list == []

    # MCLA could be reused, so __dynamic_constraints is not empty at this step
    # artificial reset
    # unfolder._CLUnfolder__dynamic_constraints = []
    # assert unfolder.dynamic_constraints == []

    # no frontiers + M (start place)
    assert unfolder.initial_constraints == [[-1], [-2], [-3], [-8], [-10], [-11], [-13], [-15], [13]]

    # L
    assert unfolder.invariant_constraints == [[[12]]]

    # No variant constraint
    assert unfolder.variant_constraints == []

    # C
    assert unfolder.final_constraints == [[3]]

    ############################################################################

    init_forward_unfolding_part_2(unfolder)

    print(unfolder.dynamic_constraints)
    print(unfolder.invariant_constraints)
    print(unfolder.final_constraints)

    # Shift of the system clauses (and syst aux clauses)
    # The maximum value is 46 since there is 46 literals
    expected = [
        [[-24, 16], [-24, 4], [-16, -4, 24], [-15, 42], [-12, 42], [15, 12, -42],
        [-42, 41], [-11, 41], [42, 11, -41], [2, -40], [41, -40], [-2, -41, 40],
        [40, -36], [-13, -36], [-40, 13, 36], [1, -25], [36, -25], [-1, -36, 25],
        [-43, 22], [-43, 25], [-22, -25, 43], [-47, 24, 1], [-47, 24, -43],
        [47, -24], [47, -1, 43], [5, -44], [6, -44], [-5, -6, 44], [-45, 17],
        [-45, 44], [-17, -44, 45], [1, -27], [41, -27], [-1, -41, 27], [27, -26],
        [-13, -26], [-27, 13, 26], [2, -46], [26, -46], [-2, -26, 46], [-30, 22],
        [-30, 46], [-22, -46, 30], [-48, 45, 2], [-48, 45, -30], [48, -45],
        [48, -2, 30], [31, -30], [31, -43], [30, 43, -31], [-49, 31, 3], [49, -31],
        [49, -3], [-50, 4], [-50, -24], [50, -4, 24], [-51, 5], [-51, -45],
        [51, -5, 45], [-52, 6], [52, -6], [-32, 21], [-32, 7], [-21, -7, 32],
        [-53, 7], [-53, -32], [53, -7, 32], [-54, 32, 8], [54, -32], [54, -8],
        [-33, 20], [-33, 11], [-20, -11, 33], [-34, 18], [-34, 9], [-18, -9, 34],
        [-55, 33, 9], [-55, 33, -34], [55, -33], [55, -9, 34], [-35, 19], [-35, 10],
        [-19, -10, 35], [-56, 34, 10], [-56, 34, -35], [56, -34], [56, -10, 35],
        [-57, 35, 11], [-57, 35, -33], [57, -35], [57, -11, 33], [-58, 12],
        [58, -12], [-37, 23], [-37, 14], [-23, -14, 37], [-38, 23], [-38, 14],
        [-23, -14, 38], [39, -37], [39, -38], [37, 38, -39], [-60, 14], [-60, -39],
        [60, -14, 39], [-59, 37, 13], [59, -37], [59, -13], [-61, 38, 15], [61, -38],
        [61, -15], [-18, 9], [-19, 10], [-20, 11], [-21, 7], [-16, 4], [-17, 5],
        [-22, 1, 2], [-23, 14, 14]]]

    # Crap
    assert unfolder.dynamic_constraints == expected

    # L
    assert unfolder.invariant_constraints == [[[12]], [[58]]]

    # No variant constraint (not shifted in second part of init_forward_unfolding)
    assert unfolder.variant_constraints == []

    # C + 46
    assert unfolder.final_constraints == [[49]]


def init_forward_unfolding_solution_2(mcla):
    """
    - Test first part of init_forward_unfolding: init of constraints
    - Test second part of init_forward_unfolding: shift of initialized constraints

    ("", "L", "C and K") # I E D F
    """
    unfolder = mcla.unfolder # shortcut
    init_forward_unfolding_part_1(mcla.unfolder)

    ############################################################################

    print(unfolder.dynamic_constraints)
    print(unfolder.initial_constraints)
    print(unfolder.invariant_constraints)
    print(unfolder.variant_constraints)
    print(unfolder.final_constraints)

    # No auxiliary variables: "C and K" property is added
    assert unfolder._CLUnfolder__aux_code_table == {'_lit47': 47}
    assert unfolder._CLUnfolder__aux_list == ['_lit47']

    # MCLA could be reused, so __dynamic_constraints is not empty at this step
    # artificial reset
    # unfolder._CLUnfolder__dynamic_constraints = []
    # assert unfolder.dynamic_constraints == []

    # no frontiers + nothing (no start place)
    assert unfolder.initial_constraints == [[-1], [-2], [-3], [-8], [-10], [-11], [-13], [-15]]

    # L
    assert unfolder.invariant_constraints == [[[12]]]

    # No variant constraint
    assert unfolder.variant_constraints == []

    # "C and K" = _lit47
    # C, not _lit47
    # K, not _lit47
    # not C, not K, _lit47
    # _lit47
    assert unfolder.final_constraints == [[3, -47], [11, -47], [-3, -11, 47], [47]]

    # PS:
    # "C or K" = _lit47
    # not C, _lit47
    # not K, _lit47
    # C, K, not _lit47
    # _lit47
    #[[-3, 47], [-11, 47], [3, 11, -47], [47]]

    ############################################################################

    init_forward_unfolding_part_2(unfolder)

    print(unfolder.dynamic_constraints)
    print(unfolder.invariant_constraints)
    print(unfolder.final_constraints)

    # Shift of the system clauses (and syst aux clauses)
    # The maximum value is now 48 since there is 47 literals
    assert unfolder.get_var_number() == 46
    assert unfolder.get_shift_step() == 47
    expected = [
        [[-24, 16], [-24, 4], [-16, -4, 24], [-15, 42], [-12, 42], [15, 12, -42],
        [-42, 41], [-11, 41], [42, 11, -41], [2, -40], [41, -40], [-2, -41, 40],
        [40, -36], [-13, -36], [-40, 13, 36], [1, -25], [36, -25], [-1, -36, 25],
        [-43, 22], [-43, 25], [-22, -25, 43], [-48, 24, 1], [-48, 24, -43],
        [48, -24], [48, -1, 43], [5, -44], [6, -44], [-5, -6, 44], [-45, 17],
        [-45, 44], [-17, -44, 45], [1, -27], [41, -27], [-1, -41, 27], [27, -26],
        [-13, -26], [-27, 13, 26], [2, -46], [26, -46], [-2, -26, 46], [-30, 22],
        [-30, 46], [-22, -46, 30], [-49, 45, 2], [-49, 45, -30], [49, -45],
        [49, -2, 30], [31, -30], [31, -43], [30, 43, -31], [-50, 31, 3], [50, -31],
        [50, -3], [-51, 4], [-51, -24], [51, -4, 24], [-52, 5], [-52, -45],
        [52, -5, 45], [-53, 6], [53, -6], [-32, 21], [-32, 7], [-21, -7, 32],
        [-54, 7], [-54, -32], [54, -7, 32], [-55, 32, 8], [55, -32], [55, -8],
        [-33, 20], [-33, 11], [-20, -11, 33], [-34, 18], [-34, 9], [-18, -9, 34],
        [-56, 33, 9], [-56, 33, -34], [56, -33], [56, -9, 34], [-35, 19], [-35, 10],
        [-19, -10, 35], [-57, 34, 10], [-57, 34, -35], [57, -34], [57, -10, 35],
        [-58, 35, 11], [-58, 35, -33], [58, -35], [58, -11, 33], [-59, 12],
        [59, -12], [-37, 23], [-37, 14], [-23, -14, 37], [-38, 23], [-38, 14],
        [-23, -14, 38], [39, -37], [39, -38], [37, 38, -39], [-61, 14], [-61, -39],
        [61, -14, 39], [-60, 37, 13], [60, -37], [60, -13], [-62, 38, 15],
        [62, -38], [62, -15], [-18, 9], [-19, 10], [-20, 11], [-21, 7], [-16, 4],
        [-17, 5], [-22, 1, 2], [-23, 14, 14]]]

    # Crap
    assert unfolder.dynamic_constraints == expected

    # L : 12 + shift_step (47)
    assert unfolder.invariant_constraints == [[[12]], [[59]]]

    # No variant constraint (not shifted in second part of init_forward_unfolding)
    assert unfolder.variant_constraints == []

    # "C and K" = _lit47 = 47
    # Shift: [[3, -47], [11, -47], [-3, -11, 47], [47]] with shift_step (47)
    assert unfolder.final_constraints == [[50, -94], [58, -94], [-50, -58, 94], [94]]


def test_shift(feed_mclanalyser, textual_properties):
    """Test shift of constraints during the solutions search"""

    mcla = feed_mclanalyser
    unfolder = mcla.unfolder # shortcut

    start, invariant, final = textual_properties[0]

    query = MCLSimpleQuery(start, invariant, final)
    unfolder.init_with_query(query)

    init_forward_unfolding_part_1(mcla.unfolder)
    init_forward_unfolding_part_2(unfolder)

    unfolder.shift()


    print(unfolder.dynamic_constraints)
    print(unfolder.initial_constraints) # Not changed
    print(unfolder.invariant_constraints)
    print(unfolder.variant_constraints) # No data for this test
    print(unfolder.final_constraints)

    expected = [
        # Initial step
        [[-24, 16], [-24, 4], [-16, -4, 24], [-15, 42], [-12, 42], [15, 12, -42],
        [-42, 41], [-11, 41], [42, 11, -41], [2, -40], [41, -40], [-2, -41, 40],
        [40, -36], [-13, -36], [-40, 13, 36], [1, -25], [36, -25], [-1, -36, 25],
        [-43, 22], [-43, 25], [-22, -25, 43], [-47, 24, 1], [-47, 24, -43],
        [47, -24], [47, -1, 43], [5, -44], [6, -44], [-5, -6, 44], [-45, 17],
        [-45, 44], [-17, -44, 45], [1, -27], [41, -27], [-1, -41, 27], [27, -26],
        [-13, -26], [-27, 13, 26], [2, -46], [26, -46], [-2, -26, 46], [-30, 22],
        [-30, 46], [-22, -46, 30], [-48, 45, 2], [-48, 45, -30], [48, -45],
        [48, -2, 30], [31, -30], [31, -43], [30, 43, -31], [-49, 31, 3], [49, -31],
        [49, -3], [-50, 4], [-50, -24], [50, -4, 24], [-51, 5], [-51, -45],
        [51, -5, 45], [-52, 6], [52, -6], [-32, 21], [-32, 7], [-21, -7, 32],
        [-53, 7], [-53, -32], [53, -7, 32], [-54, 32, 8], [54, -32], [54, -8],
        [-33, 20], [-33, 11], [-20, -11, 33], [-34, 18], [-34, 9], [-18, -9, 34],
        [-55, 33, 9], [-55, 33, -34], [55, -33], [55, -9, 34], [-35, 19], [-35, 10],
        [-19, -10, 35], [-56, 34, 10], [-56, 34, -35], [56, -34], [56, -10, 35],
        [-57, 35, 11], [-57, 35, -33], [57, -35], [57, -11, 33], [-58, 12],
        [58, -12], [-37, 23], [-37, 14], [-23, -14, 37], [-38, 23], [-38, 14],
        [-23, -14, 38], [39, -37], [39, -38], [37, 38, -39], [-60, 14], [-60, -39],
        [60, -14, 39], [-59, 37, 13], [59, -37], [59, -13], [-61, 38, 15], [61, -38],
        [61, -15], [-18, 9], [-19, 10], [-20, 11], [-21, 7], [-16, 4], [-17, 5],
        [-22, 1, 2], [-23, 14, 14]],
        # Shifted step
        [[-70, 62],
        [-70, 50], [-62, -50, 70], [-61, 88], [-58, 88], [61, 58, -88], [-88, 87],
        [-57, 87], [88, 57, -87], [48, -86], [87, -86], [-48, -87, 86], [86, -82],
        [-59, -82], [-86, 59, 82], [47, -71], [82, -71], [-47, -82, 71], [-89, 68],
        [-89, 71], [-68, -71, 89], [-93, 70, 47], [-93, 70, -89], [93, -70],
        [93, -47, 89], [51, -90], [52, -90], [-51, -52, 90], [-91, 63], [-91, 90],
        [-63, -90, 91], [47, -73], [87, -73], [-47, -87, 73], [73, -72],
        [-59, -72], [-73, 59, 72], [48, -92], [72, -92], [-48, -72, 92], [-76, 68],
        [-76, 92], [-68, -92, 76], [-94, 91, 48], [-94, 91, -76], [94, -91],
        [94, -48, 76], [77, -76], [77, -89], [76, 89, -77], [-95, 77, 49], [95, -77],
        [95, -49], [-96, 50], [-96, -70], [96, -50, 70], [-97, 51], [-97, -91],
        [97, -51, 91], [-98, 52], [98, -52], [-78, 67], [-78, 53], [-67, -53, 78],
        [-99, 53], [-99, -78], [99, -53, 78], [-100, 78, 54], [100, -78], [100, -54],
        [-79, 66], [-79, 57], [-66, -57, 79], [-80, 64], [-80, 55], [-64, -55, 80],
        [-101, 79, 55], [-101, 79, -80], [101, -79], [101, -55, 80], [-81, 65],
        [-81, 56], [-65, -56, 81], [-102, 80, 56], [-102, 80, -81], [102, -80],
        [102, -56, 81], [-103, 81, 57], [-103, 81, -79], [103, -81], [103, -57, 79],
        [-104, 58], [104, -58], [-83, 69], [-83, 60], [-69, -60, 83], [-84, 69],
        [-84, 60], [-69, -60, 84], [85, -83], [85, -84], [83, 84, -85], [-106, 60],
        [-106, -85], [106, -60, 85], [-105, 83, 59], [105, -83], [105, -59],
        [-107, 84, 61], [107, -84], [107, -61], [-64, 55], [-65, 56], [-66, 57],
        [-67, 53], [-62, 50], [-63, 51], [-68, 47, 48], [-69, 60, 60]]]

    assert unfolder.dynamic_constraints == expected

    # L = 12: + 46 + 46 => 104
    assert unfolder.invariant_constraints == [[[12]], [[58]], [[104]]]

    # C = 3: + 46 + 46 =>
    assert unfolder.final_constraints == [[95]]


if __name__ == "__main__":
    unittest.main()


