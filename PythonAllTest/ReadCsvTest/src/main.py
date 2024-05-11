import glob
import pandas as pd

source_path = "../data/source"
source_pd = pd.DataFrame()
for file_name in glob.glob(source_path + "/*.csv"):
    x = pd.read_csv(file_name)
    source_pd = pd.concat([source_pd, x], axis=0)

print(source_pd)

target_path = "../data/target"
target_pd = pd.DataFrame()
for file_name in glob.glob(target_path + "/*.csv"):
    x = pd.read_csv(file_name)
    target_pd = pd.concat([target_pd, x], axis=0)

target_pd = target_pd.rename(columns={"count_": "Number Of Requests"})
source_pd = source_pd.rename(columns={"count": "Number Of Inference Device"})
print(target_pd)

source_pd.to_csv("../data/result/source.csv", index=False)
target_pd.to_csv("../data/result/target.csv", index=False)

result = pd.merge(target_pd, source_pd, left_on="tenantId", right_on="aadtenantid", how="inner")
result = result.drop(columns=["aadtenantid", "intuneaccountid"])
result.to_csv("../data/result/result.csv")
