from nlp_features import translate_comments, sentiment_analysis
from pre_process import clean_text
from data_transformations import transform_data, write_to_csv
import csv
from youtube_functions import initialize_youtube_api, get_comments

def main():
    # initialize youtube api
    apikey = "AIzaSyD10RbJBeRqp4at6Nn7GkdI2T7xowL3xZU"

    # get video id
    video_id = "khPhsLfUzUk"

    # initialize youtube api
    youtube = initialize_youtube_api(apikey)

    # get comments
    comments = get_comments(youtube, video_id, max_results=1000)

    # clean comments
    cleaned_comments = [clean_text(comment) for comment in comments]

    # translate comments
    translated_comments = [translate_comments(comment) for comment in cleaned_comments]

    # sentiment analysis
    sentiments = [sentiment_analysis(comment) for comment in translated_comments]

    # transform data
    tranformed_data = transform_data(translated_comments, sentiments)

    # write to csv
    write_to_csv(["Comment", "Polarity", "Subjectivity"], tranformed_data, "sentiments.csv")

    
main()

