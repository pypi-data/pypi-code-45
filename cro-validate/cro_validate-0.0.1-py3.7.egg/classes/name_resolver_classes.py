

class NameResolver:
	def resolve(self, namespace, name):
		raise NotImplementedError()

	def is_nullable(self, namespace, name):
		if name.startswith('nullable_'):
			return True
		return False


class DefaultDefinitionNameResolver(NameResolver):
	def resolve(self, namespace, name):
		if name in namespace:
			return namespace[name]
		if name.startswith('nullable_'):
			normalized_name = name[9:]
			if normalized_name in namespace:
				return namespace[normalized_name]


class DefaultParameterNameResolver(NameResolver):
	def resolve(self, namespace, name):
		if name in namespace:
			return namespace[name]
		if name.startswith('nullable_'):
			normalized_name = name[9:]
			if normalized_name in namespace:
				return namespace[normalized_name]
		else:
			normalized_name = 'nullable_' + str(name)
			if normalized_name in namespace:
				return namespace[normalized_name]
