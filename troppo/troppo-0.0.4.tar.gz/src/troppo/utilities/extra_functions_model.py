import numpy as np


class ExtraFunctionsModel():

	def reverse_irreversible_reactions_in_reverse_direction(self, S, lb, ub):
		'''
		Identifies the irreversible reactions in the reverse direction and returns the S matrix with the signals for the
		metabolites reversed, a vector with the upper bounds as reversed form the lower bounds and a vector with the lower
		bounds as the reverse of the upper ones.
		Returns: S, lb, ub after modifications

		'''
		irrev_reverse_idx = np.where(ub <= 0)[0]
		if irrev_reverse_idx.size > 0:  # if they exist
			S[:, irrev_reverse_idx] = -S[:, irrev_reverse_idx]
			temp = ub[irrev_reverse_idx]
			ub[irrev_reverse_idx] = -lb[irrev_reverse_idx]
			lb[irrev_reverse_idx] = -temp
		return S, lb, ub

	def find_irreversible_reactions(self, lb):
		return np.where(lb >= 0)[0]
