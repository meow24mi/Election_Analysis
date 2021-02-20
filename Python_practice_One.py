#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                #{"county":"Denver", "registered_voters": 463353},
                #{"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #print(county_dict)
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)
#for county_dict in voting_data:
    #print(county_dict['county'])
#for county_dict in voting_data:
     #print(county_dict['registered_voters'])


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
    #output = county + " county has " + str(voters) + " registered voters."
    #print(county,voters)
    #print(output)
    #print(county,"county has",voters,'registered voters.')
#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
    #f"You received {candidate_votes} number of votes. "
    #f"The total number of votes in the election was {total_votes}. "
    #f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)


#skills drill:
#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#               {"county":"Denver", "registered_voters": 463353},
#               {"county":"Jefferson", "registered_voters": 432438}]
#for county_data in voting_data:
#    print(f"{county_data['county']} county has {county_data['registered_voters']} registered voters.")

#skills drill:
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county,voters in counties_dict.items():
#    print(f"{county} county has{voters} registered voters.")

# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

with open('election_results.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')