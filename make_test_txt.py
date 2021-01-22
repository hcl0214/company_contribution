import pandas as pd
import numpy as np


lat_list = np.linspace(28,29,1000,endpoint=False)
lon_list = np.linspace(121.0,122.0,1000,endpoint=False)
test_df = pd.DataFrame(index=lat_list,columns=lon_list)
test_df = test_df.fillna(0)
output_df = test_df.stack()
for i in range(len(output_df)-1):
    output_df[i:i+1] = np.random.rand()
    print(i)
print(output_df)

output_df = output_df.append(output_df)
output_df = output_df.append(output_df)
print(output_df)
output_df.to_csv('test.txt',sep=' ',header=None)

