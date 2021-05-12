import pandas as pd
import numpy as np

lenN = input()
initListN = [None]*(len(lenN))
initListN = input().split()

lenM = input()
initListM = [None]*(len(lenM))
initLIstM = input().split()

df_m = pd.DataFrame(initLIstM)

df = df_m.isin(initListN).astype('int')

print(np.array(df[0].tolist()))