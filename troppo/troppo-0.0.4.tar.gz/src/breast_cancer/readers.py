import pandas as pd
from pandas import Series, IndexSlice
from numpy import array, unique, where, append


# base data from breast cancer
# TODO THIS IS IMPORTANT -> MAKE THIS TO DOWNLOAD THE INFORMATION (SINCE MOST OF THE DATASETS ARE GOING TO TAKE A LOT
# todo ON THE GIT

class BreastCancerOmicsAndInformation:
	def __init__(self, load_all_information=False):
		self.load_breast_cancer_info()
		self.load_all = load_all_information
		if load_all_information:
			self.__load_all_information()
		self.final_cell_lines, self.final_origin = None, None

	def __load_all_information(self):
		self.load_gdsc_breast_cancer()
		self.load_nci60_breast_cancer()
		self.load_normal_hpa()
		self.load_pathology_hpa()
		# self.load_protein_hpa_breast() # for now, I won't use this, since this may be relevant to analyze after the generation of the models, so I'll wait
		self.load_rna_hpa_breast()
		self.load_hpa_tissue()
		self.transcript_hpa_rna_cell_line()

	def __simplify_names(self, cell_line):
		return str(cell_line).replace('-', '').replace(' ', '').upper()

	def __join_gene_names(self, data, ind, by_col=True):
		if isinstance(ind, (list, array, Series)):
			if by_col:
				return data[ind].apply(lambda x: '/'.join(x), axis=1)
			else:
				return data.loc[ind].apply(lambda x: '/'.join(x), axis=0)
		else:
			raise Exception('ind should be either a list, array or panda Series')

	def __identify_cell_lines(self, data, identification):
		'''
		This should be a multi_index, fix this shit. EDIT: fixed\n
		:param data: pd.DataFrame with the data and a single index value
		:param identification: source of the data
		:return: a pd.DataFrame with a MultiIndex containing both the cell line and source
		'''
		return pd.MultiIndex.from_tuples(list(map(lambda x: (x, str(identification)), data.index.values)),
										 names=['cell_line', 'origin'])

	def load_breast_cancer_info(self):
		self.breast_cancer_information = pd.read_csv('./data/breast_cancer_cell_lines.tsv', sep='\t')
		self.breast_cancer_information['Cell lines'].apply(lambda x: self.__simplify_names(x))
		self.breast_cancer_information = self.breast_cancer_information.set_index('Cell lines')

	def load_gdsc_breast_cancer(self):
		# TODO here should be the ability to check if the file is present; if not, download from the website
		gdsc_preprocessed = pd.read_csv('./data/sanger1018_brainarray_ensemblgene_rma.txt',
										sep='\t')
		mapping = pd.read_excel('./data/Cell_Lines_Details.xlsx', dtype={'COSMIC identifier': str}, sheet_name=None)
		mapping_dict = dict(
			zip(mapping['Cell line details']['COSMIC identifier'], mapping['Cell line details']['Sample Name']))
		gdsc_preprocessed_mapped = gdsc_preprocessed.rename(
			columns={k: self.__simplify_names(v) for k, v in mapping_dict.items()})

		# select only the breast cancer data
		cell_lines_to_keep = [c for c in gdsc_preprocessed_mapped.columns if
							  c in self.breast_cancer_information.index.values.tolist()]
		cell_lines_to_keep.append('ensembl_gene')  # to keep the genes for later conversion

		self.gdsc_data = gdsc_preprocessed_mapped[cell_lines_to_keep]
		self.gdsc_data = self.gdsc_data.T.rename(
			columns=dict(zip(self.gdsc_data.index.values, self.gdsc_data['ensembl_gene']))).drop('ensembl_gene')
		self.gdsc_data = self.gdsc_data.set_index(self.__identify_cell_lines(self.gdsc_data, 'gdsc'))

	def load_nci60_breast_cancer(self):
		nci_60 = pd.read_excel('./data/RNA__Affy_HG_U133_Plus_2.0_RMA.xls')
		breast_cancer_columns = [c for c in nci_60.columns if 'BR:' in c]
		breast_cancer_columns.append('Probe id c')
		breast_cancer_columns.append('Gene name d')
		self.nci_60_data = nci_60[breast_cancer_columns]
		self.nci_60_data = self.nci_60_data.rename(
			columns={c: self.__simplify_names(c.strip('BR:')) if 'BR:' in c else c for c in breast_cancer_columns})
		self.nci_60_data['Probe and gene names'] = self.__join_gene_names(self.nci_60_data,
																		  ['Probe id c', 'Gene name d'])
		self.nci_60_data = self.nci_60_data.drop(['Probe id c', 'Gene name d'], axis=1)
		self.nci_60_data = self.nci_60_data.T.rename(
			columns=dict(zip(self.nci_60_data.index.values, self.nci_60_data['Probe and gene names']))).drop(
			'Probe and gene names')
		self.nci_60_data = self.nci_60_data.set_index(self.__identify_cell_lines(self.nci_60_data, 'nci_60'))

	def load_normal_hpa(self):
		normal_hpa = pd.read_csv('./data/HPA/normal_tissue.tsv', sep='\t')
		normal_hpa_breast = normal_hpa[normal_hpa.Tissue == 'breast']

		self.normal_hpa_breast_glandular = normal_hpa_breast[normal_hpa_breast['Cell type'] == 'glandular cells']
		self.normal_hpa_breast_glandular = self.normal_hpa_breast_glandular.T.rename(
			columns=self.__join_gene_names(self.normal_hpa_breast_glandular, ['Gene', 'Gene name'])).drop(
			['Gene', 'Gene name', 'Tissue', 'Cell type'], axis=0)
		self.normal_hpa_breast_glandular = self.normal_hpa_breast_glandular.set_index(
			self.__identify_cell_lines(self.normal_hpa_breast_glandular, 'hpa_normal_glandular'))

		self.normal_hpa_breast_adipocytes = normal_hpa_breast[normal_hpa_breast['Cell type'] == 'adipocytes']
		self.normal_hpa_breast_adipocytes = self.normal_hpa_breast_adipocytes.T.rename(
			columns=self.__join_gene_names(self.normal_hpa_breast_adipocytes, ['Gene', 'Gene name'])).drop(
			['Gene', 'Gene name', 'Tissue', 'Cell type'],
			axis=0)
		self.normal_hpa_breast_adipocytes = self.normal_hpa_breast_adipocytes.set_index(
			self.__identify_cell_lines(self.normal_hpa_breast_adipocytes, 'hpa_normal_adipocytes'))

		self.normal_hpa_breast_myoepithelial = normal_hpa_breast[
			normal_hpa_breast['Cell type'] == 'myoepithelial cells']
		self.normal_hpa_breast_myoepithelial = self.normal_hpa_breast_myoepithelial.T.rename(
			columns=self.__join_gene_names(self.normal_hpa_breast_myoepithelial, ['Gene', 'Gene name'])).drop(
			['Gene', 'Gene name', 'Tissue', 'Cell type'],
			axis=0)
		self.normal_hpa_breast_myoepithelial = self.normal_hpa_breast_myoepithelial.set_index(
			self.__identify_cell_lines(self.normal_hpa_breast_myoepithelial, 'hpa_normal_myoepithelial'))

	def load_pathology_hpa(self):
		pathology_hpa = pd.read_csv('./data/HPA/pathology.tsv', sep='\t')
		self.pathology_hpa_breast_cancer = pathology_hpa[pathology_hpa['Cancer'] == 'breast cancer']
		self.pathology_hpa_breast_cancer['Expression'] = self.pathology_hpa_breast_cancer[
			['High', 'Medium', 'Low', 'Not detected']].idxmax(
			axis=1).fillna('Not Detected')
		self.pathology_hpa_breast_cancer = self.pathology_hpa_breast_cancer.T.rename(
			columns=self.__join_gene_names(self.pathology_hpa_breast_cancer,
										   ['Gene', 'Gene name'])).drop(
			['Gene', 'Gene name', 'High', 'Medium', 'Low', 'Not detected', 'prognostic - favourable',
			 'unprognostic - favourable', 'prognostic - unfavourable',
			 'unprognostic - unfavourable', 'Cancer'])
		self.pathology_hpa_breast_cancer = self.pathology_hpa_breast_cancer.set_index(
			self.__identify_cell_lines(self.pathology_hpa_breast_cancer, 'hpa_pathology_breast'))

	def load_protein_hpa_breast(self):
		'''
		This function/data will not be used in the meantime; only if necessary\n
		:return: pd.DataFrame with protein atlas HPA data
		'''
		protein_atlas_hpa = pd.read_csv('./data/HPA/proteinatlas.tsv', sep='\t')
		self.proteins_atlas_hpa_breast = protein_atlas_hpa.loc[
			where(protein_atlas_hpa['TPM max in non-specific'].str.contains('breast') == True)[0]]

	def load_rna_hpa_breast(self):
		cell_lines_hpa = pd.read_csv('./data/HPA/rna_celline.tsv', sep='\t')
		# cell_info_hpa = array([str(c).upper().replace('-', '') for c in cell_lines_hpa['Sample'].unique()])
		cell_info_hpa = array([self.__simplify_names(c) for c in cell_lines_hpa['Sample'].unique()])
		breast_cancer_cell_lines_hpa = unique(
			array([c for c in cell_info_hpa if c in self.breast_cancer_information.index.values.tolist()]))
		cell_lines_hpa['Sample'] = cell_lines_hpa['Sample'].apply(lambda x: self.__simplify_names(x))
		self.cell_lines_hpa_rna_breast = cell_lines_hpa[cell_lines_hpa['Sample'].isin(breast_cancer_cell_lines_hpa)]
		self.cell_lines_hpa_rna_breast = self.cell_lines_hpa_rna_breast.T
		self.cell_lines_hpa_rna_breast = self.cell_lines_hpa_rna_breast.rename(
			columns=self.__join_gene_names(self.cell_lines_hpa_rna_breast, ['Gene', 'Gene name'], False)).drop(
			['Gene', 'Gene name', 'Unit'], axis=0)
		self.cell_lines_hpa_rna_breast = pd.DataFrame(
			{sample: self.cell_lines_hpa_rna_breast.iloc[
				1, where(self.cell_lines_hpa_rna_breast.loc['Sample'] == sample)[0]] for sample in
			 self.cell_lines_hpa_rna_breast.loc['Sample'].unique().tolist()}).T
		self.cell_lines_hpa_rna_breast = self.cell_lines_hpa_rna_breast.set_index(
			self.__identify_cell_lines(self.cell_lines_hpa_rna_breast, 'hpa_cell_lines_rna'))

	def load_hpa_tissue(self):
		tissue_rna_hpa = pd.read_csv('./data/HPA/rna_tissue.tsv', sep='\t')
		self.breast_tissue_rna_hpa = tissue_rna_hpa[tissue_rna_hpa['Sample'] == 'breast'].drop(columns='Sample')
		self.breast_tissue_rna_hpa = self.breast_tissue_rna_hpa.T
		self.breast_tissue_rna_hpa = self.breast_tissue_rna_hpa.rename(
			columns=self.__join_gene_names(self.breast_tissue_rna_hpa, ['Gene', 'Gene name'], False)).drop(
			['Gene', 'Gene name', 'Unit'], axis=0)
		self.breast_tissue_rna_hpa = self.breast_tissue_rna_hpa.rename(index={'Value': 'normal'})
		self.breast_tissue_rna_hpa = self.breast_tissue_rna_hpa.set_index(
			self.__identify_cell_lines(self.breast_tissue_rna_hpa, 'hpa_breast_tissue'))

	def transcript_hpa_rna_cell_line(self):
		'''
		TODO: make this to single out transcripts, not only the genes; for every other data obtained, assume that the 'main' transcript is the one being produced

		:return: 
		'''
		trans_rna_hpa_cell_line = pd.read_csv('./data/HPA/transcript_rna_celline.tsv', sep='\t')
		trans_rna_hpa_cell_line['name'] = trans_rna_hpa_cell_line[['ensgid', 'enstid']].apply(lambda x: '/'.join(x),
																							  axis=1)
		trans_rna_hpa_cell_line = trans_rna_hpa_cell_line.drop(['ensgid', 'enstid'], axis=1)
		trans_rna_hpa_cell_line_names = {c: self.__simplify_names(c).split('.')[0] for c in
										 trans_rna_hpa_cell_line.columns}
		trans_rna_hpa_cell_line = trans_rna_hpa_cell_line.rename(columns=trans_rna_hpa_cell_line_names)
		self.trans_rna_hpa_cell_line_breast = trans_rna_hpa_cell_line.loc[:, append(unique(
			array([c for c in list(trans_rna_hpa_cell_line_names.values()) if
				   c in self.breast_cancer_information.index.values.tolist()])), 'NAME')]
		self.trans_rna_hpa_cell_line_breast = self.trans_rna_hpa_cell_line_breast.T
		self.trans_rna_hpa_cell_line_breast = self.trans_rna_hpa_cell_line_breast.rename(
			columns=self.trans_rna_hpa_cell_line_breast.loc['NAME']).drop('NAME', axis=0)
		self.trans_rna_hpa_cell_line_breast = self.trans_rna_hpa_cell_line_breast.set_index(
			self.__identify_cell_lines(self.trans_rna_hpa_cell_line_breast, 'hpa_breast_cell_line_rna'))

	def merge_data(self):
		'''
		This function is to merge all the information available. If it was load_all_information was False, it'll load
		all the information regardless.
		TODO: make this generic as possible to only load certain data. For this to be easier, all information should be in a dict or something similar to be easier to access the information
		:return: a DataFrame present in the class object
		'''
		if not self.load_all:
			self.__load_all_information()
		keys = list(self.__dict__.keys())
		keys.remove('breast_cancer_information'), keys.remove('load_all'), keys.remove('nci_60_data')
		self.merged = pd.concat([self.__dict__[k] for k in keys])

	def get_cell_line_and_origin(self, cell_line=None, origin=None):
		if isinstance(cell_line, (str, list, type(array))):
			if isinstance(origin, (str, list, type(array))):
				return self.merged.loc[IndexSlice[cell_line, origin], :]
			elif origin == None:
				return self.merged.loc[IndexSlice[cell_line, :], :]
			else:
				raise Exception(
					'Both \'cell_line\' and/or \'origin\' must be either a string, list or numpy array, or one of them is None')
		elif isinstance(origin, (str, list, type(array))):
			return self.merged.loc[IndexSlice[:, origin], :]
		else:
			raise Exception(
				'Both \'cell_line\' and/or \'origin\' must be either a string, list or numpy array, or one of them is None')


if __name__ == '__main__':
	# tests
	b = BreastCancerOmicsAndInformation(True)
	b.merge_data()
	b.get_cell_line_and_origin('mcf7')
	

	keys = list(b.__dict__.keys())
	keys.remove('breast_cancer_information'), keys.remove('load_all'), keys.remove('nci_60_data')
	b.merged = pd.concat([b.__dict__[k] for k in keys], sort=False)

	d = b.__dict__
	d.pop('breast_cancer_information'), d.pop('load_all')
	x = pd.concat(d)
	for k in d.keys():
		print(d[k].duplicated)

# TODO make sure that I extract all the cell lines if they are repeated, because they're replicates
# TODO also, think about if we keep both of them separated from each other or do we apply a statistical method for it
