#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_user_input():
    candidates = ["Biden", "Trump"]
    states = ["California", "Texas", "Florida", "New York", "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Arizona", "Virginia"]
    votes = {}
    eligible_voters = {}

    for candidate in candidates:
        votes[candidate] = int(input(f"Enter the number of votes received by {candidate}: "))

    for state in states:
        eligible_voters[state] = int(input(f"Enter the total number of eligible voters in {state}: "))

    return votes, eligible_voters

def calculate_voter_turnout(votes, eligible_voters):
    voter_turnout = {}

    for state, voters in eligible_voters.items():
        turnout = (votes["Biden"] + votes["Trump"]) / voters * 100
        voter_turnout[state] = round(turnout, 2)

    return voter_turnout

def display_results(voter_turnout, votes):
    print("\nVoter Turnout and Candidate Performance in the 2020 US Presidential Election:")

    for state, turnout in voter_turnout.items():
        print(f"{state}: Voter Turnout: {turnout}%")

    print("\nCandidate Performance:")

    for candidate, vote in votes.items():
        print(f"{candidate}: {vote} votes")

def main():
    votes, eligible_voters = get_user_input()
    voter_turnout = calculate_voter_turnout(votes, eligible_voters)
    display_results(voter_turnout, votes)

if __name__ == "__main__":
    main()


# In[ ]:




