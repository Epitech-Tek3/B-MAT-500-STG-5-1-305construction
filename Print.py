def printv(self):
    print("Total duration of construction: {} week{}\n".format(
        self.dure, "s" if self.dure > 1 else ""))
    [print("{} must begin {}".format(i[0], ("between t=" + str(i[1]) + " and t=" + str(i[1] + self.dico[i[0]]["end"]))
                                     if self.dico[i[0]]["end"] != 0
                                     else "at t=" + str(i[1]))) for i in self.tmp]
    print()
    for i in self.tmp:
        print("{}\t({})\t{}{}".format(
            i[0], self.dico[i[0]]["end"], ' ' *
            i[1], '=' * self.dico[i[0]]["dure"]
        ))
