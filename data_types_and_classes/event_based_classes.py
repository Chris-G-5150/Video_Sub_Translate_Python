from collections.abc import Callable
from typing import Any

from data_types_and_classes.data_constants import CompletionStatus


def build_process_message(process_name, process_status: str, msg: str, error_msg: str):
	return {
		"process_name": process_name,
		"process_status": process_status,
		"msg": msg,
		"error_message": error_msg,
	}


def build_class_event_list_item(
	order: int, event_name: str, class_ref: Any, function_ref: Callable
):
	return {
		"order": order,
		"event_name": event_name,
		"class_ref": class_ref,
		"function_ref": function_ref,
	}


def build_event(order: int, event_name: str, class_ref: Any, function_ref: Callable, status: str):
	return {
		"order": order,
		"event_name": event_name,
		"class_ref": class_ref,
		"function_ref": function_ref,
		"status": status,
		"completed": CompletionStatus.not_started,
		"error_message": None,
	}
