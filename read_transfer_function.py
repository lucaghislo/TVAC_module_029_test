import pandas as pd
import numpy as np


def read_transfer_function(filepath):
    fdt_data = pd.read_csv(filepath, sep="\t", comment="#")
    return fdt_data


# Get fdt data from raw fdt data file
def get_fdt(fdt_data, ch, pt):
    dac_inj_list = np.unique(fdt_data.iloc[:, 1].to_numpy())

    dac_inj_all = []
    fdt_out_all = []
    for dac_inj in dac_inj_list:
        fdt_data_subset = fdt_data[
            (fdt_data.iloc[:, 1] == dac_inj) & (fdt_data.iloc[:, 3] == ch)
        ]
        dac_inj_all.append(dac_inj)
        fdt_out_all.append(np.mean(fdt_data_subset.iloc[:, 4]))

    return dac_inj_all, fdt_out_all
