import cro_validate.api.name_resolver_api as NameResolverApi
import cro_validate.api.exception_api as ExceptionApi


class Index(dict):
	def __getattr__(self, name):
		result = NameResolverApi.resolve_parameter(self, name)
		if result is None and not NameResolverApi.is_parameter_name_nullable(self, name):
			raise ExceptionApi.create_input_error(name, 'Cannot be None')
		return result

	def __setattr__(self, name, value):
		self[name] = value

	def ensure(index):
		if index is None:
			return Index()
		return index

