# counties = ["Arapahoe", "Denver", "Jefferson"]

# if counties[1] == "Denver":
#     print(counties[1])

# if counties[3] != 'Jefferson':
#     print(counties[2])

# if "Arapahoe" in counties:
#     print("True")
# else:
#     print("False")

# if "El Paso" in counties: 
#     print("El Paso is in the list of counties")
# else:
#     print("El Paso is not in the list of counties")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and el Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties)


# -------------------------------------------------------------------------------------

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county, voters)

# voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, 
#                {"county": "Denver", "registered_voters": 463353},
#                {"county": "Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(counties_dict)):
#     print(voting_data[i])

# for county_dict in voting_data:
#     for value in counties_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict.values())

# for county_dict in voting_data:
#     for value in county_dict:
#         print(value)

# for county_dict in voting_data:
#     print(county_dict["registered_voters"])

# for county_dict in voting_data:
#     for key, value in county_dict.items():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['county'])


# -------------------------------------------------------------------------------------

# counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}

# for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# -------------------------------------------------------------------------------------

candidate_votes = int(input("How many cotes did the candidate get in the election?"))
total_votes = int(input("What s the total number of votes in the election"))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes."
#     f"The total number of votes in the election was {total_votes}."
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes")
print(message_to_candidate)



# -------------------------------------------------------------------------------------

