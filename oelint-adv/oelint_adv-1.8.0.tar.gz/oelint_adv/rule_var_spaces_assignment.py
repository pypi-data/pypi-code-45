from oelint_adv.cls_item import Variable
from oelint_adv.cls_rule import Rule


class VarSpacesOnAssignment(Rule):
    def __init__(self):
        super().__init__(id="oelint.vars.spacesassignment",
                         severity="warning",
                         message="Suggest spaces around variable assignment. E.g. 'FOO = \"BAR\"'")

    def check(self, _file, stash):
        res = []
        items = stash.GetItemsFor(
            filename=_file, classifier=Variable.CLASSIFIER)
        for i in items:
            if i.VarName == "inherit":
                continue
            needles = [" = ", " ?= ", " ??= ", " := ", " += "]
            if not any([x for x in needles if i.Raw.find(x) != -1]):
                res += self.finding(i.Origin, i.InFileLine)
        return res
