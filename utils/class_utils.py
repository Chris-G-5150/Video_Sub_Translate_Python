from dataclasses import asdict
from typing import Any, TypeVar

T = TypeVar("T")


def check_class_property_exists(class_self, class_property: str) -> bool:
	exists = hasattr(class_self, class_property)
	status = "exists" if exists else "does not exist"
	print(f"property: {class_property} {status} on {class_self.__class__.__name__}")
	return exists


def dict_to_obj(data: dict, cls: type[T]) -> T:
	"""Turn a dict into a dataclass object."""
	return cls(**data)


def obj_to_dict(obj: Any) -> dict:
	"""Turn a dataclass object into a dict."""
	return asdict(obj)


ClassUtils = {
	"check_class_prop_exists": check_class_property_exists,
	"dict_to_type": dict_to_obj,
	"obj_to_dict": obj_to_dict,
}
