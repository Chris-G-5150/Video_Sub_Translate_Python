from data_classes.global_config import DataInitializationStatus
from data_classes.global_state import ClassInitializationStatus

#Could have made this generic to update but felt as if it was clearer to make a small function for each field,
# that way I can be sure that they can only be changed through this class and nowhere else

class InitializationStatusUpdaters:
    def __init__(self, class_initialization_staus: ClassInitializationStatus, data_initialization_status: DataInitializationStatus):
        self.class_initialization_staus = class_initialization_staus
        self.data_initialization_status = data_initialization_status


    #need to predict the value at the point it you are changing it, this can catch errors early as it means something is changing it where it shouldn't.
    def check_class_initialization_status(self, field_to_update: str):
        class_status_attr = self.class_initialization_staus.__getattribute__(f"{field_to_update}")
        if not class_status_attr:
            self.change_class_initializer_value(field_to_update)
        else:
            Exception("Class initialization status has been changed elsewhere, please check GlobalStateManager.")


    def change_class_initializer_value(self, field_to_update: str):
        class_status_field = self.class_initialization_staus.__getattribute__(f"{field_to_update}")

        # [f"{value}"] = True


    def update_data_initialization_status(self, field_to_update: str):



        # TODO - This needs a rework











