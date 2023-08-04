#!/usr/bin/python3.11
"""
    @name GreedyAlgortihm.py
    @date 2023 03 21
    @description Demo a greedy algorithm and an approximation algorithm.
"""

"""
    Set-covering Problem

    Context: You are starting a radio segment and want to reach listeners in all 50 states. The challenge is deciding what stations to play on to reach the most listeners, but with mimimizing the number of stations you play on; reach the most listeners, be on an economical amount of stations.
"""

#
statesNeeded = set(["montana","washington","oregon","idaho","nevada","utah","california","arizona"])

# Empty hash of stations. Key is station-name linked to sets of lists.
stations = dict()
stations["kone"] = set( [ "idaho", "nevada", "utah" ] )
stations["ktwo"] = set( [ "washington", "idaho", "montana" ] )
stations["kthree"] = set( [ "oregon", "nevada", "california" ] )
stations["kfour"] = set( [ "nevada", "utah" ] )
stations["kfive"] = set( [ "california", "arizona" ] )

def stationCoverage( statesNeeded, stations):
    # Hold final set of stations.
    finalStations = set()
    while statesNeeded:
        bestStation = None
        statesCovered = set()
        for station, statesForStation in stations.items():
            covered = statesNeeded.intersection(statesForStation)
            if len(covered) > len(statesCovered) and station not in finalStations:
                bestStation = station
                statesCovered = covered
        if bestStation is not None:
            statesNeeded -= statesCovered
            finalStations.add(bestStation)
            stations.pop(bestStation)
        else:
            return None
    return finalStations

if __name__ == "__main__":
    print("The best stations to place the show on:")
    print( stationCoverage( statesNeeded, stations ) )