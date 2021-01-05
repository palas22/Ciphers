
import pandas as pd

text = 'WKH HDVLHVW PHWKRG RI HQFLSKHULQJ D WHAW PHVVDJH LV WR ' \
       'UHSODFH HDFK OHWWHU EB DQRWKHU XVLQJ D ILAHG UXOH, VR IRU ' \
       'HADPSOH HYHUB OHWWHU D PDB EH UHSODFHG EB G, DQG HYHUB ' \
       'OHWWHU E EB WKH OHWWHU H DQG VR RQ.'

dict_freq = {}
for char in text:
    if char != ' ':
        if char in dict_freq.keys():
            dict_freq[char] += text.count(char)
        else:
            # initialize count
            dict_freq[char] = text.count(char)

# Calculate dataframe that contains frequency of each letter
df_freq = pd.DataFrame(list(dict_freq.items()), columns = ['Letter', 'Count'])
df_freq.set_index('Letter', inplace = True)
df_freq.sort_values(by = 'Count', ascending = False, inplace = True)

# Create frequency percentage
df_freq['Count [%]'] = df_freq['Count'] / df_freq['Count'].sum() * 100

print(df_freq)