import pandas as pd
import re
import string

STOPWORDS = {
    "is", "the", "and", "a", "to", "of", "in", "that", "it", "with", "as", "for",
    "was", "on", "by", "this", "are", "be", "or", "from", "at", "which", "but", "not", "all", "we", "they", "their", "has", "have", "if", "can", "do", "he", "she", "my", "your", "his", "her", "its"
}


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    words = [W for W in text.split() if W not in STOPWORDS]
    return " ".join(words)


def main():
    file_path_excel = "ReviewSense_Customer_Feedback_5000.xlsx"
    file_path_csv = "Milestone1_cleaned_feedback.csv"

    try:
        df = pd.read_excel(file_path_excel)
        print("Reading from excel file")
    except FileNotFoundError:
        print("Excel file not found. Attempting to read from existing CSV.")
        try:
            df = pd.read_csv(file_path_csv)
            if "clean_feedback" in df.columns:
                print("CSV already has cleaned feedback.Skipping cleaning")
                return
            elif "feedback" in df.columns:
                print("Re-cleaning feedback from CSV.")
            else:
                raise ValueError("'feedback' column not found in CSV file")
        except FileNotFoundError:
            raise ValueError(
                "Neither Excel nor CSV file found. please provide the input file.")

    if "feedback" not in df.columns:
        raise ValueError("'feedback' column not found in the input file.")
    df["clean_feedback"] = df["feedback"].apply(clean_text)
    df.to_csv("Milestone1_cleaned_feedback.csv", index=False)
    print("Milestone 1 completed successfully ")
    print(df[["feedback", "clean_feedback"]].head())


if __name__ == "__main__":
    main()
