import pandas as pd
from collections import Counter
import re

# keyword cleaning


def extract_keywords(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    keywords = text.split()
    return keywords


# Main execution
if __name__ == "__main__":
    # input from milestone 2
    df = pd.read_csv("Milestone2_sentiment_results_new.csv")

    # extract keywords from clean feedback
    all_words = []
    df["clean_feedback"].apply(lambda x: all_words.extend(extract_keywords(x)))

    # count keyword frequencies
    keyword_frequencies = Counter(all_words)

    # convert to Dataframe
    keyword_df = pd.DataFrame(keyword_frequencies.items(), columns=[
                              "keyword", "frequency"]).sort_values(by="frequency", ascending=False)

    # save reults
    keyword_df.to_csv("Milestone3_Keyword_Insights.csv", index=False)

    print("Milestone 3 completed successfully!")
    print(keyword_df.head(10))
