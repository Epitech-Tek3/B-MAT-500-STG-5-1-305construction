def recurse(self, original, name):
    for i in self.dico[name]["list"]:
        self.dico[original]["prereq"][-1].append(i)
        recurse(self, original, i)
    self.dico[original]["prereq"].append([])


def getDure(self, i):
    tmp = 0
    dure = 0
    for d in self.dico[i]["prereq"]:
        for e in d:
            dure += self.dico[e]["dure"]
        if dure > tmp:
            tmp = dure
        dure = 0
    self.dico[i]["beg"] = tmp


def getDeadline(self, key, tmp):
    deadline = self.dure

    for name in self.dico:
        if (deadline > tmp[name] and key in self.dico[name]["list"]):
            deadline = tmp[name]

    self.dico[key]["end"] = deadline - (
        self.dico[key]["beg"] + self.dico[key]["dure"])


def compute(self):
    for ky in self.dico.keys():
        recurse(self, ky, ky)
        self.dico[ky]["prereq"] = [
            i for i in self.dico[ky]["prereq"] if i]

    for i in self.dico:
        getDure(self, i)

    for i in self.dico:
        self.tmp[i] = self.dico[i]["beg"]

    self.tmp = [(k, self.tmp[k]) for k in sorted(self.tmp, key=self.tmp.get)]
    self.dure = max(i[1] + self.dico[i[0]]["dure"] for i in self.tmp)
    tmp = {}

    for i in self.tmp:
        tmp[i[0]] = i[1]

    for key in self.dico:
        getDeadline(self, key, tmp)
