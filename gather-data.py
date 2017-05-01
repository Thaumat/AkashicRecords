from pymongo import MongoClient
import requests
from watson_service import WatsonService
from data_service import DataService




def main():



    data_service = DataService()
    news_journals = data_service.get_known_online_news_journals()

    news_journal_articles = []
    for news_journal in news_journals:
        try:
            articles_of_journal_over_timeframe = data_service.get_articles_by_new_journal_over_timeframe(news_journal['url'])

        except Exception as query_failure:
            print('source name, source id, resulted in xmany articles or none at all within the timeframe')

    source_articles_by_source_id = {}
    for news_source in news_sources:
        articles = data_service.get_articles_from_online_news_journal_by_url(news_source['url'])
        source_articles_by_source_id[news_source['_id']] = articles
        if 'docs' in source_articles_by_source_id.keys():
            for article in source_articles_by_source_id['docs']['source']['enriched']['url']:
                pass





    # find the best possible news across one or more sources the most both singularly about a topic and with an
    # interesting or strong perspective
                # want news that is unique due to its paring of strange characters doing odd things, expressing a strong
                # and unique opinion towards common actions performed by a character in novel way


    # Hierarchy of boxes model, where the color of the lies of each rectange can convey different information, same as the
    # spacing between the rectangles

        stop_here = ""
    stop_here = ""









    query_url = 'https://topics.mediacloud.org/api/collections/9139458/stories'
    parameters = {
        'snapshotId': '1477',
        'timespandId': '39849',
        'sort': 'inlink',
        'limit': '5000'
    }
    # response = requests.get(query_url, params=parameters)
    # stop_here = ""

    client = MongoClient('localhost', 27017)
    database = client['AkashicRecords']
    articles = database['historic_political_article_data']
    cbt = database['cleaned_breitbart_test']

    articles_found = []
    for article in articles.find():
        articles_found.append(article)

    cleaned_articles = []
    for article in articles_found:
        if len(article['entities']) > 5:
            article['entities'] = article['entities'][:5]

            stop_here = ""

    for article in articles_found:
        relation_by_sent_id = {}
        for relation in article['relations']:
            try:
                sent_id = hash(relation['sentence'])
                if 'subject' in relation.keys():
                    if 'object' in relation.keys():
                        pass
                if 'object' in relation.keys():
                    pass
            except Exception as e:
                print(e.args)


    # watson_service = WatsonService()

    # articles_found = data_service.pull_from_source('http://www.breitbart.com')
    cleaned_articles = data_service.clean_source_articles('breitbart.com', articles_found)
    cbt.insert_many(cleaned_articles)


    article_data_list = []
    for article in articles.find():
        article_element_types = []
        relevance_threshold = 0.80

        for entity in article['entities']:
            if entity['relevance'] > relevance_threshold:
                if 'knowledgeGraph' in entity.keys():
                    if 'typeHierarchy' in entity['knowledgeGraph'].keys():
                        article_element_types.append(entity['knowledgeGraph']['typeHierarchy'].split('/')[1:])

        for keyword in article['keywords']:
            if keyword['relevance'] > relevance_threshold:
                if 'knowledgeGraph' in keyword.keys():
                    if 'typeHierarchy' in keyword['knowledgeGraph'].keys():
                        article_element_types.append(keyword['knowledgeGraph']['typeHierarchy'].split('/')[1:])

        article_data_list.append(article_element_types)

    stop_here = ""


if __name__ == '__main__':
    main()

