def b():
    msg1 = str(input())
    msg2 = str(input())

    if msg1 == "it has beaten palms":
        msg1 = "clap your hands"
    if msg2 == "it has beaten palms":
        msg2 = "clap your hands"
    if msg1 == "aplauda suas maos":
        msg1 = "bata palmas"
    if msg2 == "aplauda suas maos":
        msg2 = "bata palmas"

    resultado = ("%s\n%s" % (msg1,msg2))
    print(resultado)


b()
