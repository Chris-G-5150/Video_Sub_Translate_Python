from data_types_and_classes.data_types import Injectable


class InjectableFactory:
	def __init_(self, injectable_dicts):
		self.raw_injectable_list: injectable_dicts

	def create_lists(raw_injectable_list):
		for injectable in raw_injectable_list:


	def create_injectables(injectable_dict: dict[str, Any], category: str):
		return Injectable(injectable_dict.name, injectable_dict.category, injectable_dict.payload)


class DIContainer:
	def __init__(self, dependency_set_name: str, injectables: dict[str, Injectable]):
		self.category = dependency_set_name
		self.injectables = injectables

	def get(self, injectable_name: str) -> Injectable | None:
		injectable = self.injectables.get(injectable_name)
		if injectable is None:
			print(f"[DIContainer]: Injectable '{injectable_name}' not found.")
		return injectable

	def inject(self, dependency_name: str):
		def decorator(func):
			def wrapper(*args, **kwargs):
				# first arg is `self` if this is a class method
				injectable = self.get(dependency_name)
				if not injectable:
					raise ValueError(f"Dependency '{dependency_name}' not found.")
				payload = injectable["payload"]
				return func(*args, payload, **kwargs)

			return wrapper

		return decorator
