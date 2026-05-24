"""
Lab Work #4 - Task 2: Text Analysis with Regular Expressions — Main
Version: 1.0
Developer: Variant 24
Date: 2024
Description:
    Reads text from a file, performs regex-based analysis per variant 24
    requirements, saves results to a file, and archives with zipfile.

Usage:
    python task2.py
"""

#!/usr/bin/env python3
# Lab 4, task 1, var 24. Student records. Simple version.

import re
import zipfile
import os
from pathlib import Path

RESULT_FILE = "result.txt"
ZIP_FILE = "result.zip"
SAMPLE_TEXT_FILE = "sample_text.txt"

VOWELS = set("aeiouAEIOUаеёиоуыьъэюяАЕЁИОУЫЬЪЭЮЯ")
CONSONANTS = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
                  "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")

SAMPLE_TEXT = """Hello world! This is a sample text for Lab Work 4.
There are Words, sentences, and PuncTuaTion marks.
The quick brown fox jumps over the lazy dog. Really?
Look at the MAC addresses: aE:dC:cA:56:76:54 and invalid 01:23:45:67:89:Az.
The book "Python Programming" is great!
She said, "Goodbye!" and left.
Tomorrow will be a better day; let's hope so.
The letter bbbuttered toast fizzled away — totally odd.
I saw it! Really, I did. Did you? Yes, I did!
Contact Anna about it.
:---)))
::)()[
:---)
"""


class ValidationMixin():
    def check_filename(filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл {filename} не найден.")
    def check_text(text):
        pass

class FileManager(ValidationMixin):
    def __init__(self):
        pass
        
    # def create_file(filename, str = SAMPLE_TEXT_FILE):
    #     ValidationMixin.check_filename(filename)
    #     ValidationMixin.check_text(str)
    #     """Write the demo sample text to a file for analysis."""
    #     with open(filename, "w", encoding="utf-8") as file:
    #         file.write(SAMPLE_TEXT)
    #     print(f"[IO] Create file: {filename}")
        
    def read_file(filename):
        """
         Read the content of a text file.

        Args:
            filename (str): Path to the source text file.

        Returns:
            str: File contents.
        """
        ValidationMixin.check_filename(filename)
        with open(filename, "r", encoding="utf8") as file:
            text = file.read()
            ValidationMixin.check_text(text)
            print(f"[IO] Read file: {filename}")
            return text    
    
    def save_result(text, filename = RESULT_FILE):
        """
        Save analysis results to a text file.

        Args:
            content (str): Text to write.
            filename (str): Target file path.
        """
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"[IO] Save file: {filename}")
    
    def __str__(self):
        return self.__text
        
        
    def archive_result(filename = RESULT_FILE, zipfilename = ZIP_FILE):
        """
        Compress the result file into a zip archive and print archive info.

        Args:
            source (str): File to compress.
            archive (str): Output zip file name.
        """
        with zipfile.ZipFile(zipfilename, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(filename)
            info = zf.getinfo(filename)
            print(f"\n[ZIP] Archive: {zipfilename}")
            print(f"\n[ZIP] Name list: {zf.namelist()}")
            print(f"  [ZIP] File in zrchive: {info.filename}")
            print(f"  [ZIP] Compress size: {info.compress_size} byte")
            print(f"  [ZIP] File size: {info.file_size} byte")
            print(f"  [ZIP] Date time: {info.date_time}")   
# for extraction: zf.exstractall("foldername") or zf.extract("filename", "foldername")        

class MyParser():
    
    def __init__(self, filename):
        self.__filename = filename
    
    def count_sentences(text: str):
        """
        Count declarative, interrogative, and exclamatory sentences.

        Args:
            text (str): Input text.

        Returns:
            dict: keys 'total', 'declarative', 'interrogative', 'exclamatory'.
        """
        declarative   = len(re.findall(r'\.(?=\s|$)', text))
        interrogative = len(re.findall(r'\?(?=\s|$)', text))
        exclamatory   = len(re.findall(r'!(?=\s|$)', text))
        total = declarative + interrogative + exclamatory
        
        return {
            "total": total,
            "declarative":   declarative,
            "interrogative": interrogative,
            "exclamatory":   exclamatory,
        }
        
    def avg_sentence_length(text: str):
        """
        Calculate average sentence length in characters (letters/digits only).

        Args:
            text (str): Input text.

        Returns:
            float: Average character count per sentence.
        """
        sentences = re.split(r'[.!?](?=\s|$)', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return 0.0
        
        clear = 0
        total = MyParser.count_sentences(text)["total"]
        
        for s in sentences:
            clear += len(re.sub(r"[\W\d]", "", s))
            
        result = clear / total   
        return result 
    
    def avg_word_length(text: str):
        """
        Calculate average word length in characters.

        Args:
            text (str): Input text.

        Returns:
            float: Average word length.
        """
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        if not words:
            return 0.0
        return sum(len(w) for w in words) / len(words)
    
    def count_smileys(text: str) -> int:
        """
        Count smileys defined as: [;:]-*[()\\[\\]]+  (same bracket repeated).

        Args:
            text (str): Input text.

        Returns:
            int: Number of valid smileys found.
        """
        return len(re.findall(r'[;:]-*[\(\)\[\]]+', text))
    
    def words_lowercase_start_and_punctuation(text: str):
        """
        Extract words starting with a lowercase letter and all punctuation marks.

        Args:
            text (str): Input text.

        Returns:
            dict: keys 'words' and 'punctuation'.
        """
        words = re.findall(r'\b[a-z][a-zA-Z]*\b', text)
        punctuation = re.findall(r'[^\w\s]', text)
        return {"words": words, "punctuation": punctuation}
    
    def check_mac_address(text: str) -> bool:
        """
        Validate a MAC-address in the format XX:XX:XX:XX:XX:XX
        where each segment is exactly two hexadecimal digits (0-9, a-f, A-F).

        Args:
            address (str): String to test.

        Returns:
            bool: True if valid MAC address.
        """
        return bool(re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', text))

    def words_starting_with_consonant(text: str):
        """
        Return words starting with a consonant letter.

        Args:
            text (str): Input text.

        Returns:
            list[str]: Words starting with consonant.
        """
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        
        return [w for w in words if w[0] in CONSONANTS]

    def words_with_double_letters(text: str):
        """
        Find words containing two identical consecutive letters, returning
        word and its 1-based position.

        Args:
            text (str): Input text.

        Returns:
            list[tuple]: (position, word) pairs.
        """
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        result = []
        for i, w in enumerate(words, 1):
            if re.search(r'(.)\1', w):
                result.append((i, w))
        return result

    def words_alphabetical(text: str) -> list:
        """
        Extract all words and return them sorted alphabetically.

        Args:
            text (str): Input text.

        Returns:
            list[str]: Sorted words.
        """
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        return sorted(words, key=str.lower)
    
    def print_all(text):
        print(MyParser.count_sentences(text))
        print(MyParser.avg_sentence_length(text))
        print(MyParser.avg_word_length(text))
        print(MyParser.count_smileys(text))
        print(MyParser.words_lowercase_start_and_punctuation(text))
        print(MyParser.check_mac_address(text))
        print(MyParser.words_starting_with_consonant(text))
        print(MyParser.words_with_double_letters(text))
        print(MyParser.words_alphabetical(text))
        
    def save_all(text):
        tosave = []
        tosave.append(str(MyParser.count_sentences(text)))
        tosave.append(str(MyParser.avg_sentence_length(text)))
        tosave.append(str(MyParser.avg_word_length(text)))
        tosave.append(str(MyParser.count_smileys(text)))
        tosave.append(str(MyParser.words_lowercase_start_and_punctuation(text)))
        tosave.append(str(MyParser.check_mac_address(text)))
        tosave.append(str(MyParser.words_starting_with_consonant(text)))
        tosave.append(str(MyParser.words_with_double_letters(text)))
        tosave.append(str(MyParser.words_alphabetical(text)))
        tosave = "\n".join(tosave)
        FileManager.save_result(tosave)


def task2_run(filename):
    text = FileManager.read_file(filename)
    MyParser.print_all(text)
    MyParser.save_all(text)
    FileManager.archive_result()
    
    
    
#task2_run("sometext")