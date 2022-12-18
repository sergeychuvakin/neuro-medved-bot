
class Config:
    MODEL_STORE_NAME: str = "gpt3_medium_medved_{}.pt"
    BATCH_SIZE: int = 5
    MODEL_EPOCH: int = 5
    MODEL_HF_NAME: str = "sberbank-ai/rugpt3large_based_on_gpt2"
    MODELS_FOLDER: str = "models"