from enum import Enum
from typing import Type


class AutomationProcessorListItem:
	def __init__(self, order: int, automated_class: Type[any], automated_class_params):
		self.order = order
		self.automated_class = automated_class
		self.automated_class_params = (automated_class_params)


class CompletionStatus(Enum):
	ERROR = "ERROR"
	COMPLETE = "COMPLETE"
	IN_PROGRESS = "IN PROGRESS"
	NOT_STARTED = "NOT_STARTED"


class ProcessMessage:
	def __init__(self, completion_status: CompletionStatus, msg:str, error: str | None = None):
		self.process_status = completion_status
		self.msg = msg
		self.error = error


class AutomationProcess:
	def __init__(self, order, automated_class, automated_class_params, manager_status_callback):
		self.order = order,
		self.automated_class = automated_class,
		self.automated_class_params = automated_class_params
		self.processor = None
		self.process_status = CompletionStatus.NOT_STARTED
		self.message_string = NONE # build something here
		self.process_output = ProcessMessage | None

	def init(self):
		automation_process = self
		worker = automation_process.automated_class
		params = automation_process.automated_class_params
		automation_process.processor = SequentialEventsProcessor(class_being_processed=worker(params), on_complete=self.processor_complete_callback)
		
	def processor_complete_callback(self, process_status: ProcessStatus, msg: str, error_message: str | None = None):
		self.process_status = process_status
		self.message_string = f"" #### get name of class, add error message to it 
		self.process_output = ProcessMessage(process_status=process_status, msg=self.message_string, error_message=error_message)
		self.manager_status_callback(self.process_output, )
	

class AutomationManager:
    def __init__(self, global_state_manager_callback, trigger_function):
		self.global_state_manager_callback = global_state_manager_callback
		self.trigger_function = trigger_function
		self.automation_processor_list: list[AutomationProcessorListItem] | None = None
		self.actionable_process_list = None
		self.current_list_item = None
		self.current_list_item_status = None

	def init():
		#check for a list of automation tasks, if none then just sit not doing anything
		# if so build them, out 	
		

	def build_process_list(self):
		processes = []
		for process in self.automation_processor_list:
			processes.append(
				AutomationProcess(
					order = process.order,
					automated_class = process.automated_class,
					automated_class_params = process.automated_class_params,
					manager_status_callback = self.automation_manager_callback,
					)
				)
                
		return dict(sorted(process.items()))

