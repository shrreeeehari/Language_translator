import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('API_key')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

def translator(text_input,pair_code):

    language_translator.set_service_url('URL')

    translation = language_translator.translate(
        text=text_input,
        model_id=pair_code).get_result()
    output = (json.dumps(translation, ensure_ascii=False))
    res = (output[output.find(START)+len(START):output.rfind(END)])
    res1 = (output[output.find(END)+len(END):output.rfind(END1)])
    print("\nTranslation: ",res)
    print("\n",res1)


code_pair = input("\nEnter the language code pair (eg. de-en) : ")
input_text = input("Enter text to be translated: ")
START = 'n": '
END = '}], '
END1 = '}'

translator(input_text, code_pair)
