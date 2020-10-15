import os
from runner import main as runner_main
from cslang import main as cslang_main


class TestRegisterExpressions():

  def test_assign(self):
    test_file = "test/registerassign.cslang"
    preamble, datawords, _, containerbuilder = cslang_main(test_file)
    automaton, datawords_after = runner_main(test_file)
    assert automaton.registers["assignstr"] == "hel"
    assert automaton.registers["assignnum"] == 5
    assert automaton.registers["assignidn"] == 4
    assert automaton.registers["assignids"] == "worked"

  def test_concat(self):
    test_file = "test/registerconcat.cslang"
    preamble, datawords, _, containerbuilder = cslang_main(test_file)
    automaton, datawords_after = runner_main(test_file)
    assert automaton.registers["numnum"] == "hello"
    assert automaton.registers["regnum"] == "hello"
    assert automaton.registers["numreg"] == "lohel"
    assert automaton.registers["regreg"] == "helhel"

  def test_add(self):
    test_file = "test/registeradd.cslang"
    preamble, datawords, _, containerbuilder = cslang_main(test_file)
    automaton, datawords_after = runner_main(test_file)
    assert automaton.registers["numnum"] == 7
    assert automaton.registers["regnum"] == 6
    assert automaton.registers["numreg"] == 6
    assert automaton.registers["regreg"] == 4

    assert automaton.registers["fnumnum"] == 7
    assert automaton.registers["fregnum"] == 5
    assert automaton.registers["fnumreg"] == 5
    assert automaton.registers["fregreg"] == 4.6

    assert automaton.registers["nnumnum"] == 0
    assert automaton.registers["nregnum"] == 0
    assert automaton.registers["nnumreg"] == 0
    assert automaton.registers["nregreg"] == -3


  def test_subtract(self):
    test_file = "test/registersub.cslang"
    preamble, datawords, _, containerbuilder = cslang_main(test_file)
    automaton, datawords_after = runner_main(test_file)
    assert automaton.registers["numnum"] == 1
    assert automaton.registers["regnum"] == 1
    assert automaton.registers["numreg"] == 1
    assert automaton.registers["regreg"] == 0

    assert automaton.registers["fnumnum"] == 0
    assert automaton.registers["fregnum"] == 0
    assert automaton.registers["fnumreg"] == 0
    assert automaton.registers["fregreg"] == 0

    assert automaton.registers["nnumnum"] == 0
    assert automaton.registers["nregnum"] == 0
    assert automaton.registers["nnumreg"] == 0
    assert automaton.registers["nregreg"] == 0


  def test_multiply(self):
    test_file = "test/registermul.cslang"
    preamble, datawords, _, containerbuilder = cslang_main(test_file)
    automaton, datawords_after = runner_main(test_file)
    assert automaton.registers["numnum"] == 12
    assert automaton.registers["regnum"] == 8
    assert automaton.registers["numreg"] == 8
    assert automaton.registers["regreg"] == 4

    assert automaton.registers["fnumnum"] == 7
    assert automaton.registers["fregnum"] == 5
    assert automaton.registers["fnumreg"] == 5
    assert automaton.registers["fregreg"] == 6.25

    assert automaton.registers["nnumnum"] == 1
    assert automaton.registers["nregnum"] == 1
    assert automaton.registers["nnumreg"] == 1
    assert automaton.registers["nregreg"] == 1

  def test_divide(self):
    test_file = "test/registerdiv.cslang"
    preamble, datawords, _, containerbuilder = cslang_main(test_file)
    automaton, datawords_after = runner_main(test_file)
    assert automaton.registers["numnum"] == 3
    assert automaton.registers["regnum"] == 1
    assert automaton.registers["numreg"] == 1
    assert automaton.registers["regreg"] == 1

    assert automaton.registers["fnumnum"] == 3.5
    assert automaton.registers["fregnum"] == 1.75
    assert automaton.registers["fnumreg"] == 3.125
    assert automaton.registers["fregreg"] == 1

    assert automaton.registers["nnumnum"] == -5
    assert automaton.registers["nregnum"] == -0.2
    assert automaton.registers["nnumreg"] == -5
    assert automaton.registers["nregreg"] == 5
