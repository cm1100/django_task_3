import t5
import main2
import classifier
import backend
import sys

base_url=sys.argv[1]
links,base_url=t5.return_links(base_url)

list_results = main2.get_results(links)

results= classifier.classify_add(list_results)

backend.add_to_database(results,base_url)
