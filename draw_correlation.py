# please install pandas, matplotlib.
import pandas as pd
import glob
import matplotlib.pyplot as plt
import os
from pylab import mpl
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

def main():
    file_list = glob.glob("*.xlsx")

    if len(file_list) == 0:
        print("please copy excel file to the current path. ")
        return
    else:
        print("\n" + "#-"*20 + "\n")
        for idx, ff in enumerate(file_list):
            print("Index: {}   file name : {}".format(idx, ff))
        print("\n")
        label = int(input("Please select the file index."))

    
    df = pd.read_excel(file_list[label])
    data = df.values
    label_list = data[0][2:]
    result = []
    
    for line in data:
        if '皮尔逊相关性' in line:
            new_list = []
            for ii in line[2:]:
                new_list.append(float(str(ii).strip("*")))
            result.append(new_list)

    length = len(result)
    for jj in range(length):
        for kk in range(jj, length):
            result[jj][kk] = -0.5

    _title = None
    while True:
        _title = input("\nplease input a Title, then press Enter\n")
        if _title is not None:
            break

    # plt.style.use('ggplot') 
    fig = plt.figure(dpi=320)
    ax = fig.add_subplot(111)
    
    ax.set_yticks(range(len(label_list)))
    ax.set_xticks(range(len(label_list)))
    ax.set_yticks(np.array(range(len(label_list)))+0.5, minor=True)
    ax.set_xticks(np.array(range(len(label_list)))+0.5, minor=True)
    
    im = ax.imshow(result, cmap=plt.cm.Oranges)
    plt.colorbar(im)
    plt.title(_title)
    plt.grid(which='minor', alpha=0.3)
    
    for num in range(length):
        plt.text(num-0.4, num+0.2, label_list[num], size=8)
    plt.yticks()
    plt.xticks()
    plt.savefig("./{}.png".format(_title))
    os.system("open {}.png".format(_title))
    
main()
