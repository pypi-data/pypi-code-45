import itertools
import tableprint as tp
from .molecular import *
import matplotlib.pyplot as plt
def calc (elements,depth,max=-1) :
	elements=elements.elements
	combinaisons=[]
	for i in list(range(1,depth+1)) :
		combinaisons+=list(itertools.combinations_with_replacement(elements,i))
	results=mol_container()
	impurities=mol_container()
	for combinaison in combinaisons :
		name=[]
		mass=0
		probability=1
		impurity=0.
		for element in combinaison :
			name.append(element.name)
			mass+=element.mass
			if element.score>=1 :
				element.score=1.
				impurity+=1.
			probability=probability*element.rate*element.score
		name.sort()
		_name=''
		for item in name :
			_name+=item
		if impurity == 0. :
			mol=molecular(_name,{'mass':mass,'probability':probability,'elements':name})
			if mol.probability > max :
				results.add_molecule(mol)
			else:
				pass
		else :
			mol = molecular(_name, {'mass': mass, 'probability': probability, 'elements': name})
			if mol.probability > max :
				impurities.add_molecule(mol)
			else:
				pass

	results.sort()
	impurities.sort()
	return (results,impurities)

def charge_calculation(results,charge_range) :
	results, impurities = results[0], results[1]
	charged_results=ion_container()
	charged_impurities = ion_container()
	for ion in results.molecules :
		charges=ion.get_charge(charge_range[0],charge_range[1])
		for charge in charges :
			mol=molecular(ion.name,{'mass':ion.mass/charge,'probability':ion.probability,'elements':[]},charge=charge)
			charged_results.add_molecule(mol)
	for ion in impurities.molecules :
		charges=ion.get_charge(charge_range[0],charge_range[1])
		for charge in charges :
			mol=molecular(ion.name,{'mass':ion.mass/charge,'probability':ion.probability,'elements':[]},charge=charge)
			charged_impurities.add_molecule(mol)
	charged_results.sort()
	charged_impurities.sort()
	return (charged_results,charged_impurities)

def disp_results(results,imp=False) :
	results, impurities = results[0], results[1]
	yx=[]
	for molecule in results.molecules :
		yx.append((molecule.name,molecule.mass,molecule.charge,molecule.probability))
	tp.banner('Combinaison results')
	tp.table(yx,['Combinaison','DA','Charge','Probability'], style='fancy_grid', width=25)

	if imp!=False :
		yx = []
		for molecule in impurities.molecules:
			yx.append((molecule.name, molecule.mass, molecule.charge, molecule.probability))
		tp.banner('Impurities')
		tp.table(yx, ['Combinaison', 'DA', 'Charge', 'Relative Probability'], style='fancy_grid', width=25)
	
def plot_sim (results) :
	results, impurities = results[0], results[1]
	X=[molecule.mass for molecule in results.molecules]
	Y=[molecule.probability for molecule in results.molecules]
	plt.plot(X,Y)
	plt.xlabel('DA')
	plt.ylabel('Relative Intensity')
	plt.show()

def save_results(results,file) :
	results, impurities = results[0], results[1]
	yx=[]
	file=open(file,'w')
	for molecule in results.molecules :
		yx.append([molecule.name,molecule.mass,molecule.charge,molecule.probability])
	for molecule in impurities.molecules:
		yx.append([molecule.name, molecule.mass, molecule.charge, molecule.probability])
	for item in yx :
		file.write('%s\t%s\t%s\t%s\n' % (item[0],item[1],item[2],item[3]))
	file.close()
	
def disp_select(results,DA) :
	results, impurities = results[0], results[1]
	yx=[]
	total=0
	for molecule in results.molecules :
		if molecule.mass == DA :
			yx.append([molecule.name,molecule.charge,molecule.probability])
			total+=molecule.probability
	for molecule in yx :
		molecule.append(molecule[-1]/total*100)
	tp.banner('DA Probability Results for %s' % DA)
	tp.table(yx,['Combinaison','Charge','Overall Probability','DA Probability (%)'], style='fancy_grid', width=25)
	yx=[]
	for molecule in impurities.molecules :
		if molecule.mass == DA :
			yx.append([molecule.name,molecule.charge,molecule.probability])
			total+=molecule.probability
	for molecule in yx :
		molecule.append(molecule[-1]/total*100)
	tp.banner('Impurities at %s' % DA)
	tp.table(yx,['Combinaison','Charge','Relative Probability','DA Probability (%)'], style='fancy_grid', width=25)
			
def plot_results (results,mass_range=(0,1E3)) :
	results, impurities = results[0], results[1]
	for molecule in results.molecules :
		if mass_range[0]<=molecule.mass<=mass_range[1] :
			plt.plot(molecule.mass,molecule.probability,marker='+',color='red',ms=10)
			plt.text(molecule.mass,molecule.probability,molecule.name,fontsize=12)
	for molecule in impurities.molecules :
		if mass_range[0]<=molecule.mass<=mass_range[1] :
			plt.plot(molecule.mass,molecule.probability,marker='+',color='blue',ms=10)
			plt.text(molecule.mass,molecule.probability,molecule.name,fontsize=12)
	plt.xlabel('DA')
	plt.ylabel('Probability')
	plt.yscale('log')
	plt.show()
