''' Created by Raymond Lui, 27 September 2021'''

import dbcs_demo_func as dbcs



# Original data (subset n=0)
dataset0, subset0 = dbcs.loadExampleData()
dbcs.plotChemicalSpace(dataset0, subset0, filename="plots/dbcs-demo_0-1.svg")



# Initialise subset (n=1)
dataset1, subset1 = dbcs.initialiseSubset(dataset0, subset0, method="most_dissimilar", plot=True, filename="plots/dbcs-demo_0-2.svg")
dbcs.plotChemicalSpace(dataset1, subset1, filename="plots/dbcs-demo_1-1.svg", distances=True, filename2="plots/dbcs-demo_1-2.svg")



# MaxSum selection (n=2-10)
dataset2_maxsum, subset2_maxsum = dbcs.selectCompound(dataset1, subset1, method="MaxSum", plot=True, filename="plots/dbcs-demo_1-3a.svg")
dbcs.plotChemicalSpace(dataset2_maxsum, subset2_maxsum, filename="plots/dbcs-demo_2-1a.svg", distances=True, filename2="plots/dbcs-demo_2-2a.svg")

dataset3_maxsum, subset3_maxsum = dbcs.selectCompound(dataset2_maxsum, subset2_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_2-3a.svg")
dbcs.plotChemicalSpace(dataset3_maxsum, subset3_maxsum, filename="plots/dbcs-demo_3-1a.svg", distances=True, filename2="plots/dbcs-demo_3-2a.svg")

dataset4_maxsum, subset4_maxsum = dbcs.selectCompound(dataset3_maxsum, subset3_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_3-3a.svg")
dbcs.plotChemicalSpace(dataset4_maxsum, subset4_maxsum, filename="plots/dbcs-demo_4-1a.svg", distances=True, filename2="plots/dbcs-demo_4-2a.svg")

dataset5_maxsum, subset5_maxsum = dbcs.selectCompound(dataset4_maxsum, subset4_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_4-3a.svg")
dbcs.plotChemicalSpace(dataset5_maxsum, subset5_maxsum, filename="plots/dbcs-demo_5-1a.svg", distances=True, filename2="plots/dbcs-demo_5-2a.svg")

dataset6_maxsum, subset6_maxsum = dbcs.selectCompound(dataset5_maxsum, subset5_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_5-3a.svg")
dbcs.plotChemicalSpace(dataset6_maxsum, subset6_maxsum, filename="plots/dbcs-demo_6-1a.svg", distances=True, filename2="plots/dbcs-demo_6-2a.svg")

dataset7_maxsum, subset7_maxsum = dbcs.selectCompound(dataset6_maxsum, subset6_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_6-3a.svg")
dbcs.plotChemicalSpace(dataset7_maxsum, subset7_maxsum, filename="plots/dbcs-demo_7-1a.svg", distances=True, filename2="plots/dbcs-demo_7-2a.svg")

dataset8_maxsum, subset8_maxsum = dbcs.selectCompound(dataset7_maxsum, subset7_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_7-3a.svg")
dbcs.plotChemicalSpace(dataset8_maxsum, subset8_maxsum, filename="plots/dbcs-demo_8-1a.svg", distances=True, filename2="plots/dbcs-demo_8-2a.svg")

dataset9_maxsum, subset9_maxsum = dbcs.selectCompound(dataset8_maxsum, subset8_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_8-3a.svg")
dbcs.plotChemicalSpace(dataset9_maxsum, subset9_maxsum, filename="plots/dbcs-demo_9-1a.svg", distances=True, filename2="plots/dbcs-demo_9-2a.svg")

dataset10_maxsum, subset10_maxsum = dbcs.selectCompound(dataset9_maxsum, subset9_maxsum, method="MaxSum", plot=True, filename="plots/dbcs-demo_9-3a.svg")
dbcs.plotChemicalSpace(dataset10_maxsum, subset10_maxsum, filename="plots/dbcs-demo_10-1a.svg")



# MaxMin selection (n=2-10)
dataset2_maxmin, subset2_maxmin = dbcs.selectCompound(dataset1, subset1, method="MaxMin", plot=True, filename="plots/dbcs-demo_1-3b.svg")
dbcs.plotChemicalSpace(dataset2_maxmin, subset2_maxmin, filename="plots/dbcs-demo_2-1b.svg", distances=True, filename2="plots/dbcs-demo_2-2b.svg")

dataset3_maxmin, subset3_maxmin = dbcs.selectCompound(dataset2_maxmin, subset2_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_2-3b.svg")
dbcs.plotChemicalSpace(dataset3_maxmin, subset3_maxmin, filename="plots/dbcs-demo_3-1b.svg", distances=True, filename2="plots/dbcs-demo_3-2b.svg")

dataset4_maxmin, subset4_maxmin = dbcs.selectCompound(dataset3_maxmin, subset3_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_3-3b.svg")
dbcs.plotChemicalSpace(dataset4_maxmin, subset4_maxmin, filename="plots/dbcs-demo_4-1b.svg", distances=True, filename2="plots/dbcs-demo_4-2b.svg")

dataset5_maxmin, subset5_maxmin = dbcs.selectCompound(dataset4_maxmin, subset4_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_4-3b.svg")
dbcs.plotChemicalSpace(dataset5_maxmin, subset5_maxmin, filename="plots/dbcs-demo_5-1b.svg", distances=True, filename2="plots/dbcs-demo_5-2b.svg")

dataset6_maxmin, subset6_maxmin = dbcs.selectCompound(dataset5_maxmin, subset5_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_5-3b.svg")
dbcs.plotChemicalSpace(dataset6_maxmin, subset6_maxmin, filename="plots/dbcs-demo_6-1b.svg", distances=True, filename2="plots/dbcs-demo_6-2b.svg")

dataset7_maxmin, subset7_maxmin = dbcs.selectCompound(dataset6_maxmin, subset6_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_6-3b.svg")
dbcs.plotChemicalSpace(dataset7_maxmin, subset7_maxmin, filename="plots/dbcs-demo_7-1b.svg", distances=True, filename2="plots/dbcs-demo_7-2b.svg")

dataset8_maxmin, subset8_maxmin = dbcs.selectCompound(dataset7_maxmin, subset7_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_7-3b.svg")
dbcs.plotChemicalSpace(dataset8_maxmin, subset8_maxmin, filename="plots/dbcs-demo_8-1b.svg", distances=True, filename2="plots/dbcs-demo_8-2b.svg")

dataset9_maxmin, subset9_maxmin = dbcs.selectCompound(dataset8_maxmin, subset8_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_8-3b.svg")
dbcs.plotChemicalSpace(dataset9_maxmin, subset9_maxmin, filename="plots/dbcs-demo_9-1b.svg", distances=True, filename2="plots/dbcs-demo_9-2b.svg")

dataset10_maxmin, subset10_maxmin = dbcs.selectCompound(dataset9_maxmin, subset9_maxmin, method="MaxMin", plot=True, filename="plots/dbcs-demo_9-3b.svg")
dbcs.plotChemicalSpace(dataset10_maxmin, subset10_maxmin, filename="plots/dbcs-demo_10-1b.svg")