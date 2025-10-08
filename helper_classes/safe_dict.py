from typing import Any

"""
SafeDict is a wrapper that uses included python functionality so that dictionaries 
can be frozen and unfrozen to have properties able to be removed, added or changed. 

This is just to replace the readonly attribute from other languages like typescript. 

If a dataclass won't be changed, still handy to use this and set it frozen to be true guarantee no mutation 

"""


class SafeDict:
	# initializes the class
	def __init__(self, initial: dict[str, Any] | None = None):
		self._data = dict(initial or {})
		self._frozen = False

	# reads values without having to unfreeze
	def get(self, key: str, default: Any = None) -> Any:
		return self._data.get(key, default)

	# updates the value if isn't frozen
	def set(self, key: str, value: Any):
		if self._frozen:
			raise RuntimeError(f"Cannot modify '{key}' — dictionary is frozen.")
		self._data[key] = value

	# freezes the class back after actions have been performed on ir
	def freeze(self):
		self._frozen = True

	# unfreezes the class to perform work on it.
	def unfreeze(self):
		self._frozen = False

	# Returns a shallow copy but unsafe to mutate
	def as_dict(self) -> dict[str, Any]:
		return dict(self._data)
