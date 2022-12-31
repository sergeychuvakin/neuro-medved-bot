from typing import Dict
import os
class Config:
    MODEL_STORE_NAME: str = "gpt3_medium_medved_{}.pt"
    BATCH_SIZE: int = 5
    MODEL_EPOCH: int = 9
    MODEL_HF_NAME: str = "sberbank-ai/rugpt3large_based_on_gpt2"
    MODELS_FOLDER: str = "models"
    NUMBER_OF_WORDS: int = 150
    MODEL_LOCAL_PATH: str = "models/pre-trained-class/"
    NEW_TRAINED_MODEL_HF_NAME: str = "sergeychuvakin/Neuro-medved"
    PRESET_PHARASES_WITH_CONTEXT: Dict[str, str] = {
        "Когда закончится гегемония США?": "Англосаксы и их прихвостни",
        "Что делать с национал-предателями?": "Русофобы и предатели",
        "Когда закончится война в Украине?": "Кровавый киевский режим",
        "Где заканчивается «русский мир»?": "Традиция, метафизика, Бог и особый путь русской цивилизации",
        "Когда Путин умрет?": "Трагедия русского мира и маховик дезинтеграции",
        "Будет ли ядерная война?": "Ядерное оружие, победа России",
        "Украина вернет Крым?": "Нацисты, предатели",
        "Кто главный патриот России?": None
    }
    TG_TOKEN = os.getenv("TG_TOKEN")
    HELP_MESSAGE: str = "Выберите пожалуйста одну из опций и Нейро-Медведев Бот закончит фразу"
    MODEL_ENDPOINT_URL: str = "http://api:5000/gpt/medved"
    N_OPTIONS: int = 2

