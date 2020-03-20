#  API Basics
def one_dict(list_dict):

    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for team in nba_teams:
        for key in keys:
            out_dict[key].append(team[key])
    return out_dict

import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
type(df)

df.head()
df.mean()
from nba_api.stats.static import teams
#https://pypi.org/project/nba-api/
nba_teams = teams.get_teams()
nba_teams[0:3]
nba_teams[0]['city']
dict_nba = one_dict (nba_teams)
df_teams = pd.DataFrame (dict_nba)
df_teams.head()

df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

type (df_warriors [['id']])
id_warriors = df_warriors [['id']].values[0][0]


from nba_api.stats.endpoints import leaguegamefinder

# Since https://stats.nba.com does lot allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
gamefinder.get_json()

games = gamefinder.get_data_frames()[0]
games.head()

games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']

games_home.mean()['PLUS_MINUS']
games_away.mean()['PLUS_MINUS']



fig, ax = plt.subplots()
games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

#= ================================== Rest APIs
# RE = representatioal S = State T = transfer

#translator api key dtS3DlrAl4PZ5_uY_eoMGIcXX5h-Wq3TROC7T0nUqIvO
#translator api url
#spech2text api key
#spech2text api url

#you will need the following library

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/510f3315-0b4d-4f71-8ea5-1c139eb25a3c"
iam_apikey_s2t = "8IWKEoy7OeH1UsDlOlomgjBxGHJZki1XNucFlvJLMBQY"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

filename='PolynomialRegressionandPipelines.mp3'

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
response.result
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)

# ================ language Translator =============================
from ibm_watson import LanguageTranslatorV3

url_lt= 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/870a86fb-b493-4dd1-9343-29c800828510'
apikey_lt= 'dtS3DlrAl4PZ5_uY_eoMGIcXX5h-Wq3TROC7T0nUqIvO'
version_lt='2020-03-20'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

translation=translation_response.get_result()
translation

spanish_translation =translation['translations'][0]['translation']
spanish_translation

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_eng

French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()

French_translation['translations'][0]['translation']
