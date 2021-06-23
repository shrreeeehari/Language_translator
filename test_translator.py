import unittest
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
    return res


code_pair = input("Enter the language code pair (eg. de-en) : ")
input_text = input("Enter text to be translated: ")
START = 'n": '
END = '}], '


class TestTranslator(unittest.TestCase):
    def test1_translator(self):
        expected = input("Enter expected value\n(within double quotes): ")
        actual = translator(input_text,code_pair)
        self.assertEqual(actual,expected)

unittest.main()
