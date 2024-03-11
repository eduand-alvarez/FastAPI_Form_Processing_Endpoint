from pydantic import BaseModel

class SubmissionPayload(BaseModel):
    affiliation: str
    training_infrastructure: str
    weight_type: str
    precision: str
    hw_type: str
    model_type: str
    revision_name: str
    model_name: str
    base_model: str
    terms: bool
