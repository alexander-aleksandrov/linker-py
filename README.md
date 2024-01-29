# LinkerPy
#### Video Demo:  <URL HERE>
#### Description:
LinkerPy is a Python-based utility designed to enhance note-taking and knowledge management within the Obsidian ecosystem. It automates the process of interlinking files by transforming mentions of potential note titles into Markdown links, thus fostering a more connected and efficient digital notebook.

At the core of LinkerPy is a custom stemmer algorithm tailored for Russian language processing, which I developed after evaluating other solutions. This stemmer is built upon the [Snowball algorithm](http://snowball.tartarus.org/algorithms/russian/stemmer.html), optimized for performance and integration with the Obsidian vault structure.

LinkerPy Files:

stemmer.py - Contains the custom stemmer algorithm that processes text to identify potential stem of the word based on linguistic rulles within the Russian language scope.

test_project.py - A script for testing the functionalities of LinkerPy, ensuring that the stemmer and linking mechanisms are operating correctly.

project.py - The main script that executes the LinkerPy program. It scans markdown files within specified folder, identifies potential note title mentions, and converts them into Markdown links. Make sure that all files that you want to be linked should be in one folder.

helper.py - A utility script that helps to sort and clean exclusion file if needed.

requirements.txt - Lists all the Python libraries and dependencies necessary to run LinkerPy.

exclutions.txt - A custom exclusion list used by the stemmer to ignore certain words during the stemming process.

testVault/ - A directory containing sample files used to test and demonstrate the functionality of LinkerPy without affecting actual notes. But inside a a project you can specify any folder

files/ - This directory currently housing a single file that contains words for the stemmer to exclude.

Key decisions in the development of LinkerPy include the creation of a custom stemmer for performance reasons and choosing a Python-centric approach for its simplicity and efficiency in scripting complex operations. Because such libraries as 
NLTK (Natural Language Toolkit), Pymorphy2, Natasha, SpaCy, Mystem are to heavy for this simple task.

In conclusion, LinkerPy offers a streamlined solution for Obsidian users to weave their notes into a tightly-knit web of knowledge with minimal effort. 

My code is still weak please pay attention that files over 20000 words can cuase strange linking that i'm still trying to figure out. Do a backup of your vaults before using this app. 

