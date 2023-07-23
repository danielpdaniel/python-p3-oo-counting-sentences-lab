#!/usr/bin/env python3

class MyString:

  def __init__(self=str, val=''):
    self.value = val
      # self.set_value(val)

  def get_value(self):
    return(self._value)

  def set_value(self, val):
    if type(val) == str:
      self._value = val
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)
    
  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    # sentences = "hey"
    sentences = self.value.replace("!", ".").replace("?", ".").split(".")
    # print(sentences)
    while sentences.__contains__(''):
      sentences.pop(sentences.index(''))
      
    print(sentences)
    return(len(sentences))