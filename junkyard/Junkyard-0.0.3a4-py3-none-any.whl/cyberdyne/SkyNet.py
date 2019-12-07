import multiprocessing
"""
THIS LIBRARY IS CURRENTLY EMPTY AND ONLY CONTAINS PLACEHOLDER CLASSES AND METHODS

IT IS INTENDED TO BE THE ROBOTICS AND ARTIFICIAL INTELLIGENCE SECTION OF THE JUNKYARD
IN THE NEAR TO NEVER-REALIZED FUTURE.
"""

# inform the user that this file is useless for the time being
if __name__ != "__main__":
    print("The cyberdyne module has yet to be fleshed out and currently contains zero functionality.")
    print("It is our hope that this will change in the near future -- Until then this file is useless")


# a class to act as the cyberdyne.SkyNet library's core handling class
class Core:
    # SkyNetCore() initialization method
    def __init__(self, name, designation, model=None):
        """

        :param name:
        :param designation:
        :param model:
        """
        self.models = ("Placeholder01", "Placeholder02")

        # give the core a personalized name
        self.name = name
        # give the core a designation
        self.designation = designation
        # establish our ai model
        self.model = model
        # get threads in a cpu
        self.cpu_thread_count = multiprocessing.cpu_count()


if __name__ == '__main__':
    # test SkyNetCore
    snc = Core("Ro-Bob", "B-DROID-01A")
