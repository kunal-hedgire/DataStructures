_end = '_end_'
class A:
    #Make a trie out of nested HashMap, UnorderedMap, dict structures
    @classmethod
    def MakeTrie(cls,words):
      root = dict()
      for word in words:
        current_dict = root
        for letter in word:
          current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
      return root

    def LongestCompoundWord(self,original_trie, trie, word, level=0):
      first_letter = word[0]
      if not first_letter in trie:
        return False
      if len(word)==1 and _end in trie[first_letter]:
        return level>0
      if _end in trie[first_letter] and self.LongestCompoundWord(original_trie, original_trie, word[1:], level+1):
        return True
      return self.LongestCompoundWord(original_trie, trie[first_letter], word[1:], level)
#Words that were in your question
words = ['test','testing','tester','teste', 'testingtester', 'testingtestm', 'testtest','testingtest']
print('input is :',words)
a=A()
trie = a.MakeTrie(words)
#Sort words in order of decreasing length
words = sorted(words, key=lambda x: len(x), reverse=True)
for word in words:
   if a.LongestCompoundWord(trie,trie,word):
       print("Longest compound word was '{0:}'".format(word))
       break
