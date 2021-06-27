
import numpy
import yaml
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




class Settings(object):

    def __init__(self):
        self.settings_dict = dict()

    def load(self, yaml_file):
        if yaml_file:
            res = yaml.load(open(yaml_file, "r"))
            if res:
                for name in res.keys():
                    setattr(self, name.lower(), res[name])
                print('Settings loaded from: ' + yaml_file)
                self.settings_dict = res
        else:
            raise IOError('Settings file not found. Please, provide some settings file.')


config = Settings()

def main():
    conf_file = None
    if len(sys.argv) > 1:
        conf_file = sys.argv[1]
    config.load(conf_file)
    fileName = getattr(config, 'name')

    Application(fileName).run()



class Application:
    def __init__(self, fileName):
        self.x_data = []
        self.y_data = []
        self.z_data = []
        self.data = []
        self.dataFileName = fileName
        self.fig = plt.figure()
        # self.ax = self.fig.add_subplot(111, projection = '3d')
        self.ax = Axes3D(self.fig)

    def run(self):
        self.data = numpy.loadtxt(self.dataFileName)
        # self.data = numpy.genfromtxt(self.dataFileName)
        for xyz in self.data:
            self.x_data.append(xyz[0])
            self.y_data.append(xyz[1])
            self.z_data.append(xyz[2])

        self.ax.scatter(self.x_data, self.y_data, self.z_data, s=1)
        plt.show()

        # input("\nPress Enter to continue.")

if __name__ == "__main__":
    sys.exit(main())
