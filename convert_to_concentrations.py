import pandas as pd


for i in range(1,5):
	df = pd.read_csv(f"trimmed/trial{i}.csv")

	# Divide all the absorptivities by the absorptivity constant obtained in the previous lab
	df.iloc[:, 1] = df.iloc[:, 1] / 244.54947

	df.to_csv(f"concentrations/trial{i}.csv", index=False)