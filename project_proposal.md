# Image Based Language Translator: IBLT

### Group 9: Chris Drury and Matthew Pinsent 

#### The Problem

The problem we would like to propose is that of language barriers. As a tourist/traveller or a student learning a new language, it can be difficult to translate or understand signs and other written work that may be necessary to understanding the situation the person(s) is in. Furthermore, there can be a time rush to interpreting other languages depending on the situation. 

#### The Solution

The proposed project will aim to create a small application that can process images to find and highlight any written text using image enhancement, filtering and edge detection [1]. Once located, the user will select the language that was captured from a list of predetermined languages and the text will then go through translation for the specified language. Finally, the project aims to place this newly translated text on top of the original text in the image. The project will be implemented using python, and will take advantage of OCR libraries, image enhancement modules such as Pillow [2], and language translator modules like googletrans [3].


#### References

[1] Course textbook <br>
[2] https://pillow.readthedocs.io/en/3.0.x/reference/ImageEnhance.html  <br>
[3] https://pypi.org/project/googletrans/ <br>