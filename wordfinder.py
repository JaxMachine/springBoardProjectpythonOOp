"""Word Finder: finds random words from a dictionary."""

#import random module
import random

class WordFinder:
    """Used to find words in a dictionary file
    
    >>> wf = WordFinder("Simple.txt")
    3 words read
    
    >>> wf.random() in ["cat", "dog", "procupine"]
    True

    >>> wf.random() in ["cat", "dog", "procupine"]
    True

    >>> wf.random() in ["cat", "dog", "procupine"]
    True
    """

    def __init__(self, path):
        """Read The Dictionary File"""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        """Parse words from the dictionary file"""

        return[w.strip() for w in dict_file]
    
    def random(self):
        """Return a random word from the Dictionary file"""

        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Specialized Word Finder skips certin entries
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> Swf.random() in ["pear", "carrot", "kale"]
    True

    >>> Swf.random() in ["pear", "carrot", "kale"]
    True

    >>> Swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse deict file and skip comments"""
        return [w.strip for w in dict_file
            if w.strip() and not w.startswith("#")]

