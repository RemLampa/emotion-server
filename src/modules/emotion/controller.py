from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features

from . import credentials
from .model import henry_text

natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=credentials.username,
    password=credentials.password,
    version="2017-02-27"
)

response = natural_language_understanding.analyze(
    text=henry_text,
    features=[
        Features.Entities(
            emotion=True,
            sentiment=True,
            limit=2
        ),
        Features.Keywords(
            emotion=True,
            sentiment=True,
            limit=2
        )
    ]
)

