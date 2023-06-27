from langdetect import detect
from deep_translator import GoogleTranslator

def detect_and_translate(text, target_lang):
    result_lang = detect(text)
    if result_lang == target_lang:
        return text
    else:
        # translator = google_translator()
        translate_text = GoogleTranslator(source='auto', target='en').translate(text)
        return translate_text


# text = "こんにちは、元気ですか"
text=input("Enter source Language : ")
print("The entered text is ",text)
lang = input("Convert to which language ?: ")
# print("enter short for language For English(en)")
print("The result is : ",detect_and_translate(text, target_lang='lang'))

codes = {
    'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Langauge',
    'sq': 'Albanian', 'bn': 'Bangla', 'bh': 'Bhojpuri',
    'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
    'cze': 'Caech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
    'fre': 'french', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
    'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
    'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
    'mar': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'dut': 'Dutch',
    'te': 'Telugu', 'ta': 'Tamil', 'cy': 'Welsh'}
