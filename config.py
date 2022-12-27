from typing import List
import os
class Config:
    MODEL_STORE_NAME: str = "gpt3_medium_medved_{}.pt"
    BATCH_SIZE: int = 5
    MODEL_EPOCH: int = 9
    MODEL_HF_NAME: str = "sberbank-ai/rugpt3large_based_on_gpt2"
    MODELS_FOLDER: str = "models"
    NUMBER_OF_WORDS: int = 30
    MODEL_LOCAL_PATH: str = "models/pre-trained-class/"
    NEW_TRAINED_MODEL_HF_NAME: str = "sergeychuvakin/Neuro-medved"
    PRESET_PHARASES: List[str] = [
        "Когда закончится гегемония США? ",
        "Скоро ли НАТО развалится?",
        "Где заканчивается «русский мир»?",
        "Будет ли ядерная война?",
        "Когда наступит крах доллара?",
        "Спецоперация идет по плану?",
        "Что делать с национал-предателями?",
        "Кто главный патриот России?",
        "Когда Россия победит англосаксов?",
        "help"
    ]
    TG_TOKEN = os.getenv("TG_TOKEN")
    HELP_MESSAGE: str = "Выберите пожалуйста одну из опций и Нейро-Медведев Бот закончит фразу"