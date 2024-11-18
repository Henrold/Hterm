Functions

newpg()

Args:
    none

print a new paragraph (used internally, same as print(""))

-----
msg()

Args:
    status: int
    process: str
    message: str

print a formatted terminal message

-----
line()

Args:
    mode: int

print an included line (1-7)

1 ============================================================
2 ------------------------------------------------------------
3 ############################################################
4 ************************************************************
5 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
7 ............................................................


-----
cline()

Args:
    char:str

make a line using a custom char

-----
ask()

Args:
    question: str
    answers: list
    lineType = 1
    answerBeam = ""
    maximumAnswerLength = 1
    answerKeySeperator = ":"
    allowMultipleAnswerUses = False
    blockInvalidAnswers = False
    invalidAnswerMessage = "invalid"
    newlineAfterAnswer = True

ask a question using a list llike this: [["answer1key", "answer1"], ["answer2key", "answer2"]]
returns the answer

-----
askyn()

Args:
    question: str
    lineType = 1
    answerBeam = ""
    answerKeySeperator = ":"
    answerType = 1
    returnNoAnswer = False
    noAnswerMessage = "none"
    newlineAfterAnswer = True

Ask a question with a yes/no answer

ansewrType
1: y/n
2: yes/no
3: ok/cancel

-----
asktext()

Args:
    question: str
    lineType = 1
    answerBeam = ""
    newlineAfterAnswer = True

ask a question with a text answer

-----

Error codes
000 | impossible (src_error())
001 | removed legacy error from v0.0.0 Build 0000
002 | colour error
003 | msg error: invalid status (developer caused)
004 | line error
005 | cline.char is too long
006 | undefined ask function error
007 | answers too long
008 | allowMultipleAnswerUses is not enabled
009 | invalid askyn type
