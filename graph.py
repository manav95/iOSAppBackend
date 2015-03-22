import matplotlib.pyplot as plt
# Fill the chart/background using chf, add axes to show bg
def plotter(datasets, filename):
  xList = [x for x in range(300)]
  i = 0
  plotList = []
  yawList = []
  pitchList = []
  rollList = []
  while i < 300:
      plotList.append(xList[i])
      yawList.append(datasets[0][i])
      pitchList.append(datasets[1][i])
      rollList.append(datasets[2][i])
      i = i + 25
  lines = plt.plot(plotList, yawList, plotList, pitchList, plotList, rollList)
  plt.setp(lines[0], color='r',linewidth=2.0)
  plt.setp(lines[1], color='g',linewidth=2.0)
  plt.setp(lines[2], color='b',linewidth=2.0)
  plt.ylabel('Errors')
  plt.xlabel('Time')
  plt.savefig(filename + ".png")
