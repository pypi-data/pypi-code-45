from numpy import array, setdiff1d, union1d, intersect1d, append
from random import randint

from cobamp.core.linear_systems import SteadyStateLinearSystem
from cobamp.core.optimization import LinearSystemOptimizer
from troppo.reconstruction_properties import FastCCProperties, MBAProperties
from troppo.methods.gapfill.fastcc import FastCC


class MBA():
	def __init__(self, S, lb, ub, method, properties, consistency_properties):
		self.S = S
		self.lb = lb
		self.ub = ub
		self.method = method
		self.consistency_properties = consistency_properties
		self.properties = properties
		self.medium = self.properties['medium_set']
		self.high = self.properties['high_set']
		self.tolerance = self.properties['tolerance']
		self.epsil = 0.5
		self.n_metabolites, self.n_reactions = self.S.shape
		self.reactions = array(range(0, self.n_reactions))
		self.LPproblem, self.lsoLP = None, None
		self.temp, self.original_bounds, self.inactive_reactions, self.tested_reactions, self.removed_reactions = None, array(
			[]), array([]), array([]), array([])
		self.generate_problem()

	def generate_problem(self):
		self.LPproblem = SteadyStateLinearSystem(self.S, self.lb, self.ub,
												 ['V' + str(i) for i in range(self.S.shape[1])],
												 solver=self.properties['solver'])
		self.lsoLP = LinearSystemOptimizer(self.LPproblem)

	def temp_reaction_remove(self, id_reaction):
		self.temp = self.LPproblem.get_stuff('var', [id_reaction])
		self.original_bounds = [self.lb[id_reaction], self.ub[id_reaction]]
		self.LPproblem.set_variable_bounds(self.temp, [0], [0])
		self.lb[id_reaction], self.ub[id_reaction] = 0, 0

	def temp_reaction_activate(self, id_reaction):
		self.LPproblem.set_variable_bounds(self.temp, self.original_bounds[0], self.original_bounds[1])
		self.lb[id_reaction], self.ub[id_reaction] = self.original_bounds[0], self.original_bounds[1]

	def select_method_for_consistency(self):
		possible_methods = ['fastcc']
		if self.method in possible_methods:
			if self.method == 'fastcc':
				return FastCC(self.S, array(self.lb), array(self.ub), self.consistency_properties)

		return None

	def mba(self):
		nc = setdiff1d(self.reactions, union1d(self.medium, self.high))
		while nc.size != 0:
			ri = randint(0, nc.size)
			testing_reaction = nc[ri]
			self.tested_reactions = append(self.tested_reactions,
										   testing_reaction)  # to keep track of the tested reactions for the algorithm

			self.temp_reaction_remove(testing_reaction)  # change the bounds of the current reaction to test to [0,0]
			sol = self.lsoLP.optimize()
			if sol.status() != 'optimal':
				self.inactive_reactions = setdiff1d(self.reactions,
													self.tested_reactions)  # TODO check later when running the algorithm if this is the right way to do this
			else:
				consistent = self.select_method_for_consistency()
				active_reactions, _, _, _, _, = consistent.run()
				self.inactive_reactions = append(setdiff1d(self.reactions, active_reactions), testing_reaction)

			eH = intersect1d(self.inactive_reactions, self.high)
			eM = intersect1d(self.inactive_reactions, self.medium)
			eX = setdiff1d(self.inactive_reactions, union1d(self.high, self.medium))

			if eH.size == 0 and eM.size < self.epsil * eX.size:
				for remove in self.inactive_reactions:
					self.temp_reaction_remove(remove)
				nc = setdiff1d(nc, self.inactive_reactions)
				self.removed_reactions = union1d(self.removed_reactions, self.inactive_reactions)
			else:
				nc = setdiff1d(nc, testing_reaction)

		return setdiff1d(self.reactions, self.removed_reactions)

	def run(self):
		return self.mba()
