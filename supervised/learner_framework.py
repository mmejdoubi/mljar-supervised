import logging

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.DEBUG)
import uuid
import os

log = logging.getLogger(__name__)

from supervised.validation.validation_step import ValidationStep


from supervised.callbacks.early_stopping import EarlyStopping
from supervised.callbacks.time_constraint import TimeConstraint


from supervised.callbacks.callback_list import CallbackList


class LearnerFrameworkParametersException(Exception):
    pass


class LearnerFramework:
    def __init__(self, params, callbacks=[]):
        log.debug("LearnerFramework __init__")
        self.uid = str(uuid.uuid4())

        self.framework_file = self.uid + ".framework"
        self.framework_file_path = os.path.join("/tmp/", self.framework_file)

        for i in ["learner", "validation"]:  # mandatory parameters
            if i not in params:
                msg = "Missing {0} parameter in LearnerFramework params".format(i)
                log.error(msg)
                raise ValueError(msg)

        self.params = params
        self.callbacks = CallbackList(callbacks)

        self.preprocessing_params = params.get("preprocessing")
        self.validation_params = params.get("validation")
        self.learner_params = params.get("learner")

        self.validation = None
        self.preprocessings = []
        self.learners = []

    def train(self, data):
        pass

    def predict(self, X):
        pass

    def save(self):
        pass

    def load(self, json_desc):
        pass
