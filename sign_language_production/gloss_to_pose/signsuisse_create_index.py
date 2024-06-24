import pandas as pd
from text_to_gloss import text2gloss_module


df = pd.read_csv("datasets/signsuisse/index_German_SwissGermanSL.csv")
# Create path column
df["path"] = "de_dsgs_poses/" + df["id"].astype(str) + ".pose"

# Prepare words column
df.rename(columns={"name": "words"}, inplace=True)

# Create glosses column by simple glosser words in German
text2gloss = text2gloss_module(glosser="simple")
language = "de"
df["glosses"] = df["words"].apply(lambda text: text2gloss(text, language)[0][1] if text2gloss(text, language) else None)

# save files
df.to_csv("datasets/signsuisse/index.csv", index=False)
