from __future__ import print_function
import dill as pickle
import sys
import os
from strace2datawords import DataWord
from register_automaton import RegisterAutomaton
from register_automaton import State
from register_automaton import Transition





def main(name):
  basename = os.path.splitext(os.path.basename(name))[0]
  dirname = os.path.dirname(name)
  datawords_path = os.path.join(dirname, basename + ".dw")
  pickle_path = os.path.join(dirname, basename + ".pickle")
  automaton_path = os.path.join(dirname, basename + ".auto")

  # Load in the dataword list (we might not even use this)
  # dataword list is in the .dw file
  with open(datawords_path, "r") as f:
    datawords = f.readlines()


  # Load in the List of dataword objects (we might just use this)
  with open(pickle_path, "r") as f:
    dataword_objs = pickle.load(f)


  # Load in the automaton
  with open(automaton_path, "r") as f:
    automaton = pickle.load(f)


  # Pass each dataword in the list in series into the automaton

  for i in dataword_objs:
    automaton.match(i)


  # At the end of everything we have a transformed set of datawords.
  # We either use them if we ended in an accepting state or drop ignore
  # them if we haven't ended in an accepting state
  # Some print goes here
  print("Automaton ended in state: " + str(automaton.current_state))
  print("With registers: " + str(automaton.registers))

  for i in dataword_objs:
    print(i.get_mutated_strace())

  return automaton, dataword_objs





if __name__ == "__main__":
  main(sys.argv[1])
