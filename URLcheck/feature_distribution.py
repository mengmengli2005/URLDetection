from __future__ import division

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle as pkl

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
featureSet = pd.read_csv("url_features.csv")

sns.set(style="darkgrid")

#Length_of_url
sns.distplot(featureSet[featureSet['malicious'] == 0]['Length_of_host'], color='blue', label='Benign URLs')
sns.distplot(featureSet[featureSet['malicious'] == 1]['Length_of_host'], color='red', label='Phishing URLs')
plt.title('Length_of_host Distribution')
plt.legend(loc='upper right')
plt.xlabel('Length_of_host')
plt.show()

# #Length_of_host
# sns.distplot(featureSet[featureSet['malicious'] == 0]['Length_of_host'], color='green', label='Benign URLs')
# sns.distplot(featureSet[featureSet['malicious'] == 1]['Length_of_host'], color='red', label='Phishing URLs')
# plt.title('Host Length Distribution')
# plt.legend(loc='upper right')
# plt.xlabel('Length of Host')
# plt.show()

# #IPaddress_presence
# sns.distplot(featureSet[featureSet['malicious'] == 0]['No_of_dots'], color='green', label='Benign URLs')
# sns.distplot(featureSet[featureSet['malicious'] == 1]['No_of_dots'], color='red', label='Phishing URLs')
# plt.title('No_of_delim Distribution')
# plt.legend(loc='upper right')
# plt.xlabel('No_of_delim')
# plt.show()


# # {0,1} features
# x = featureSet[featureSet['malicious'] == 0]['No_of_dots']
# y = featureSet[featureSet['malicious'] == 1]['No_of_dots']
# plt.hist(x, bins=8, alpha=0.9, label='Benign URLs', color='blue')
# # sns.distplot(x,bins=8,color='blue',label='Benign URLs')
# plt.hist(y, bins=10, alpha=0.6, label='Malicious URLs', color='red')
# # sns.distplot(y,bins=8,color='red',label='Malicious URLs')
# plt.legend(loc='upper right')
# plt.xlabel('Number of Dots')
# plt.title('Distribution of Number of Dots in URL')
# plt.show()


# # {0,1} features only with statistical information
# x = featureSet[featureSet['IPaddress_presence'] == 1][featureSet['malicious'] == 0]
# y = featureSet[featureSet['IPaddress_presence'] == 1][featureSet['malicious'] == 1]
# print("IPaddress_presence")
# print("Ratio of 0 : %f %%" % ((len(x)/len(featureSet)))*100)
# print("Ratio of 1 : %f %%" % ((len(y)/len(featureSet)))*100)
#
# x = featureSet[featureSet['Unicode_presence'] == 1][featureSet['malicious'] == 0]
# y = featureSet[featureSet['Unicode_presence'] == 1][featureSet['malicious'] == 1]
# print("Unicode_presence")
# print("Ratio of 0 : %f %%" % ((len(x)/len(featureSet)))*100)
# print("Ratio of 1 : %f %%" % ((len(y)/len(featureSet)))*100)
# print("No. of 0 : %f %%" % len(x))
# print("No. of 1 : %f %%" % len(y))
#
#
# x = featureSet[featureSet['Hyphen_presence'] == 1][featureSet['malicious'] == 0]
# y = featureSet[featureSet['Hyphen_presence'] == 1][featureSet['malicious'] == 1]
# print("Hyphen_presence")
# print("Ratio of 0 : %f %%" % ((len(x)/len(featureSet)))*100)
# print("Ratio of 1 : %f %%" % ((len(y)/len(featureSet)))*100)
#
# x = featureSet[featureSet['At_presence'] == 1][featureSet['malicious'] == 0]
# y = featureSet[featureSet['At_presence'] == 1][featureSet['malicious'] == 1]
# print("At_presence")
# print("Ratio of 0 : %f %%" % ((len(x)/len(featureSet)))*100)
# print("Ratio of 1 : %f %%" % ((len(y)/len(featureSet)))*100)
#
# x = featureSet[featureSet['SubDir_presence'] == 1][featureSet['malicious'] == 0]
# y = featureSet[featureSet['SubDir_presence'] == 1][featureSet['malicious'] == 1]
# print("SubDir_presence")
# print("Ratio of 0 : %f %%" % ((len(x)/len(featureSet)))*100)
# print("Ratio of 1 : %f %%" % ((len(y)/len(featureSet)))*100)

# # 统计phishing URL 和 benign URL 个数
# x = featureSet[featureSet['malicious'] == 0]
# y = featureSet[featureSet['malicious'] == 1]
# print("Ratio of Benign : %f %%" % ((len(x)/len(featureSet)))*100)
# print("Ratio of Phishing : %f %%" % ((len(y)/len(featureSet)))*100)