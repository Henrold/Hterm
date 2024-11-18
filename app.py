import main
import os
import time

main.msg(1,"henrold", "test")
main.line(1)
main.line(2)
main.line(3)
main.line(4)
main.line(5)
main.line(6)
main.line(7)
main.cline("H")

c = main.ask("don pollo", [["a", "dom pollo"],["b", "dim pollo"],["c", "dox pollo"]])
print(c)

if main.askyn("henrold"):
    print("good")

print(main.asktext("henrold"))
