# Language_translator

The project aims to achieve the following goals in sequential order:

1. Creating language translator function using IBM Watson APIs.
2. Writing unit tests to test the functionality of the code written. 
3. Following python coding conventions and verifying the code by running static code analysis. 


<h3>CREATING LANGUAGE TRANSLATOR FUNCTION</h3>
The program translator.py is capable of converting any text from English to any other language or from any other laguage to English.<br>
<br>
<img src="images/language_codes.jpg" height="600">

In translator.py, <code>API_key</code> and <code>URL</code> are to be replaced with the API key and the URL from your instance of Watson Language Translator service.
  
The program takes two inputs: <br>
  (i) A language code pair - which has language codes of the language from which the translation is required and the language to which the translation is required, both separated       by a '-' . <br>
  For example, the input en-ru implies that the user wishes to translate text from English to Russian while the input ru-en means that the translation would happen from Russian to   English.<br>
 (ii) The second input would be the text that the user wishes to translate. 

<h3>EXAMPLE OUTPUT</h3>
(English to Swedish)
<img src="images/example.png" height="270">

<br>
<h3>UNIT TESTING</h3>

The file test_translator.py runs the unit test for the translator function. As an input, it asks for a language code pair and the text to be translated. Along with this it asks for an expected output which the user is supposed to enter from some other source. The unit test compares this expected output entered by the user with the output generated by the translator function to declare if the test was passed or not. 

<img src="images/unit_test_result.png" height="270">
<br>  
<h3>STATIC CODE ANALYSIS</h3>

<img src="images/pylint_scores.png" height="450">

Of course you can further improve your pylint score by adding comments to your classes and functions.
  
