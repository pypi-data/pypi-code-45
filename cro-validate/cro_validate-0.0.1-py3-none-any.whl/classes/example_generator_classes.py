import cro_validate.api.definition_api as DefinitionApi
import cro_validate.api.configuration_api as ConfigApi
from cro_validate.enum import DataType
from crolib.enum import DataFormat


class ExampleGenerator:
	def next(self):
		raise NotImplementedError()


class ExampleGeneratorFactory:
	def create(self, definition, **kw):
		raise NotImplementedError()


class DefaultExamplesProvider:
	def get_examples(self, definition, **kw):
		return [1]
		#if definition.data_type == DataType.Boolean:
		#	return [True]
		#if definition.data_format == DataFormat.Email:
		#	return ['test@crosoftware.net']
		#if definition.data_format == DataFormat.PhoneNumber:
		#	return ['+1 (360) 123-6543']
		#if definition.data_format == DataFormat.IntResourceId:
		#	return [1]
		#if definition.data_format == DataFormat.UuidResourceId:
		#	return ['ddf936ae-f5a3-4210-977c-0ac8583040f9']
		#if definition.data_format == DataFormat.Url:
		#	return ['https://test.url']
		#if definition.data_format == DataFormat.DateTime:
		#	return ['2049-10-31T11:32:38.390000']
		#if definition.data_format == DataFormat.Uuid:
		#	return ['9f34f340-54d2-4403-a53b-d8017a64734f']
		#return None


class DefaultGenerator(ExampleGenerator):
	def _select_next(self):
		for k in self.values:
			if k in self.processed:
				continue
			self.processed.add(k)
			return k
		return None

	def __init__(self, definition, **kw):
		super().__init__(definition, **kw)
		self.composite_types = {DataType.Object, DataType.Array}
		if isinstance(definition, str):
			self.definition = DefinitionApi.get(definition)
		else:
			self.definition = definition
		if self.definition.data_type == DataType.Object:
			validator = self.definition.validator
			field_names = validator.list_field_names()
			self.values = {
					k:DefinitionApi.get(validator.get_definition_name(k)).examples
					for k in field_names
					if not DefinitionApi.get(validator.get_definition_name(k)).data_type in self.composite_types
				}
			self.values.update({
					k:DefaultGenerator(validator.get_definition_name(k))
					for k in field_names
					if DefinitionApi.get(validator.get_definition_name(k)).data_type == DataType.Object
				})
			self.values.update({
					k:DefaultGenerator(DefinitionApi.get(validator.get_definition_name(k)).data_format)
					for k in field_names
					if DefinitionApi.get(validator.get_definition_name(k)).data_type == DataType.Array
				})
			self.child_values = {
					k:None
					for k in field_names
					if DefinitionApi.get(validator.get_definition_name(k)).data_type in self.composite_types
				}
			self.indexes = {
					k:[len(self.values[k]),0]
					for k in self.values
					if not DefinitionApi.get(validator.get_definition_name(k)).data_type in self.composite_types
				}
		elif self.definition.data_type == DataType.Array:
			self.values = {self.definition.name:DefaultGenerator(self.definition.data_format)}
			self.child_values = {self.definition.name:None}
		else:
			self.values = {self.definition.name: self.definition.examples}
		self.indexes = {k:[len(self.values[k]),0] for k in self.values if not isinstance(self.values[k], DefaultGenerator)}
		self.processed = set()
		self.visited = set()
		self.selected = self._select_next()
		missing = []
		for k in self.values:
			if isinstance(self.values[k], DefaultGenerator):
				continue
			if not self.values[k]:
				missing.append(k)
		if len(missing) > 0:
			raise Exceptions.InputError('DefaultGenerator', 'Missing examples for fields: {0}'.format(missing))

	def next(self):
		if self.selected is None:
			return None
		result = {}
		visit = {}
		for k in self.values:
			visit[k] = 0
			value = self.values[k]
			if isinstance(value, DefaultGenerator):
				# Composit Value
				################
				next_val = None
				if self.child_values[k] is None:
					self.child_values[k] = self.values[k].next()
					result[k] = self.child_values[k]
				else:
					if k == self.selected:
						next_val = self.values[k].next()
						if next_val is None:
							self.selected = self._select_next()
							result[k] = self.child_values[k]
						else:
							visit[k] = visit[k] + 1
							result[k] = next_val
					else:
						result[k] = self.child_values[k]
				if self.definition.data_type == DataType.Object:
					validator = self.definition.validator
					field_definition = DefinitionApi.get(validator.get_definition_name(k))
					if field_definition.data_type == DataType.Array:
						result[k] = [result[k]]
				elif self.definition.data_type == DataType.Array:
					result[k] = [result[k]]
			else:
				# Simple Value
				##############
				index = self.indexes[k][1]
				if k == self.selected:
					if index >= self.indexes[k][0]:
						index = 0
						self.indexes[k][1] = 0
						self.selected = self._select_next()
						if self.selected is None:
							return None
					else:
						self.indexes[k][1] = index + 1
				visit[k] = index
				result[k] = self.values[k][index]
		# Early Return on No Entries
		############################
		if len(visit) == 1:
			for k in visit:
				if visit[k] == 0:
					self.selected = None
					return result
		# Update Visit
		##############
		parts = [k + '.' + str(visit[k]) for k in visit]
		parts.sort()
		perm = ':'.join(parts)
		if perm in self.visited:
			return self.next()
		self.visited.add(perm)
		# Return
		########
		if not self.definition.data_type == DataType.Object:
			for entry in result:
				return result[entry]
		return result


class DefaultGeneratorFactory(ExampleGeneratorFactory):
	def create(self, definition, **kw):
		g = DefaultGenerator(definition, **kw)
		return g