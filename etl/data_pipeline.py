from abc import ABC, abstractmethod

class DataPipeline(ABC):   

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(data):
        pass

    @abstractmethod
    def load(self, data, worker):
        pass

    def execute(self, worker):
        raw_data = self.extract
        data = self.transform(raw_data)
        self.load(data, worker)
        return

class PipelineManager:
    def __init__(self, pipeline: DataPipeline, worker) -> None:
        self.pipeline = pipeline
        self.worker = worker

    def execute(self):
        # Here we can execute general code for every pipeline
        # Some examples include:
        # - capturing Telemetry events
        # - logs about the amout and type of the data we process/save 
        raw_data = self.pipeline.extract()
        data = self.pipeline.transform(raw_data)
        self.pipeline.load(data, self.worker)