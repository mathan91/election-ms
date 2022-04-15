'''

service to persist data and retrieve back to model

'''

import json
import model.electionAggBO as model

def insert_data(app):

    f = open('C:/Users/I534329/git/election-ms/app-py/resources/election-data/model.json')
    data = json.load(f)    
    # print(data)
    # modeld = model.Data("india", "tamilnadu", "coimbatore", "dmk", 100, 200000)
    for state in data['country']:
        for electiontype in state['state1']:
            for year in electiontype['ELECTION_TYPE']:
                for city in year['YEAR']:
                    party = city['CITY1']
                    print(party)

insert_data(1)