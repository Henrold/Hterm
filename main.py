# Hterm 0.0.0 Build 0001
# HENROLD
import os
import platform
import sys

# resources
import resources.textassets as res

# modules that need to be installed from pip
try:
    from colorama import Fore, Back, Style
except:
    print("\ncolour module (colorama) not found")
    print("you could try running pip install colorama")
    print("\nError code 002")
    sys.exit()

# source error should be unreachable
def src_error(kill = True):
    print("\nThis error should be impossible to get to.")
    print("If you see this error it means that there")
    print("is a flaw in the source code or the compiler")
    print("\nError code 000")
    if kill:
        sys.exit()

def newpg():
    print("\n", end = "")

# Status
# 1 OKAY
# 2 FAIL
# 3 _MSG

# messages themed like plymouth
def msg(status: int, process: str, message: str):
    if status != 1 and status != 2 and status != 3:
        print("\nmsg.status is invalid (only 1, 2 or 3 are valid)")
        print("check the code for the application")
        print("\nError code 003")
    else:
        if status == 1:
            print("[", end = "")
            print(Fore.GREEN + "OKAY", end = "")
            print(Style.RESET_ALL, end = "")
            print("]", end = "")
        elif status == 2:
            print("[", end = "")
            print(Fore.RED + "FAIL", end = "")
            print(Style.RESET_ALL, end = "")
            print("]", end = "")
        elif status == 3:
            print("[", end = "")
            print(Fore.YELLOW + "_MSG", end = "")
            print(Style.RESET_ALL, end = "")
            print("]", end = "")
        else:
            src_error()
        print(f" <{process.upper()}>: {message}")

# lines
lineTypes = {1: res.thickLine,
             2: res.thinLine,
             3: res.hashLine,
             4: res.starLine,
             5: res.plusLine,
             6: res.wavyLine,
             7: res.dotLine}

# draw a line from textassets
def line(mode: int):
    try:
        print(lineTypes[mode])
    except:
        print("\nline function error: mode out of range (min 1, max 7)")
        print("\nError code 004")

# make your own line
def cline(char: str):
    if len(char) < 1:
        print("\ncline function error: len(cline.char) > 1")
        print("cline needs only one char, which gets printed 60 times")
        print("\nError code 005")
    else:
        for x in range(60):
            print(char, end = "")
        print("")

# questions

def ask(question: str, answers: list, lineType = 1, answerBeam = "", maximumAnswerLength = 1, answerKeySeperator = ":", allowMultipleAnswerUses = False, blockInvalidAnswers = False, invalidAnswerMessage = "invalid", newlineAfterAnswer = True):
    print("\n")
    line(lineType)
    print(f"\n{question}\n")

    loopedItems = []

    for i in answers:
        try:
            if len(i[0]) > maximumAnswerLength:
                print(f"\nYour answers cannot have more than {maximumAnswerLength} chars")
                print("\nError code 007")
            else:
                if i[0] in loopedItems and not allowMultipleAnswerUses:
                    print("\nallowMultipleAnswerUses is not enabled")
                    print("\nError code 008")
                else:
                    print(i[0], f"{answerKeySeperator} ", end = "")
                    print(i[1])
                    loopedItems.append(i[0])
        except:
            print("\nask function error (undefined)")
            print("\nError code 006")
    ans = input(answerBeam)
    # newline
    if newlineAfterAnswer:
        newpg()
    # check if answer is valid
    if ans not in loopedItems:
        ans = invalidAnswerMessage
    return ans

def askyn(question: str, lineType = 1, answerBeam = "", answerKeySeperator = ":", answerType = 1, returnNoAnswer = False, noAnswerMessage = "none", newlineAfterAnswer = True):
    if answerType == 1:
        answersList = [["y", "yes"], ["n", "no"]]
        maximumAnswerLength = 1
    elif answerType == 2:
        answersList = [["yes", ""], ["no", ""]]
        answerKeySeperator = ""
        maximumAnswerLength = 3
    elif answertype == 4:
        answersList = [["ok", ""], ["cancel", ""]]
        answerKeySeperator = ""
        maximumAnswerLength = 6
    else:
        print("\naskyn.answerType is invalid (1 or 2)")
        print("\nError code 009")
        return 0

    response = ask(question, answersList, lineType = lineType, answerBeam = answerBeam, answerKeySeperator = answerKeySeperator, maximumAnswerLength = maximumAnswerLength, newlineAfterAnswer = newlineAfterAnswer)
    if response == "yes" or response == "y" or response == "ok":
        return True
    elif response == "no" or response == "n" or response == "cancel":
        return False
    else:
        if returnNoAnswer:
            return noAnswerMessage
        else:
            return False

def asktext(question: str, lineType = 1, answerBeam = "", newlineAfterAnswer = True):
    print("\n")
    line(lineType)
    print(f"\n{question}\n")
    response = input(answerBeam)
    if newlineAfterAnswer:
        newpg()
    return response
