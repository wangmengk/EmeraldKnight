import json
import ek_getchoice
import ek_getname
import ek_abstract


class ek_kernel:
    def __init__(self):
        self.scene = "0"
        self.paras = {
            "osl": 0,
            "bsl": 0,
            "ssl": 0,
            "sinl": 0,
            "sint": 0
        }
        ek_abstract.ek_choice.kernel = self

    def getChoice(self):
        return ek_getchoice.getChoice(self.scene)

    def load(self, name):
        with open("./save/"+name+".eks", "r") as f:
            self.scene = f.readline().strip()
            self.paras = json.loads(f.readline())

    def save(self, name):
        with open("./save/"+name+".eks", "w") as f:
            f.write(self.scene+"\n")
            f.write(json.dumps(self.paras)+"\n")

    def getSceneName(self, s):
        return ek_getname.getName(s)