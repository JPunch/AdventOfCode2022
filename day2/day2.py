import typing as t
from enum import Enum


class RPS(Enum):  # Rock Paper Scissors
    Rock = "A"
    Paper = "B"
    Scissors = "C"


RPSValues = {RPS.Rock: 1, RPS.Paper: 2, RPS.Scissors: 3}


class RPSUnknown(Enum):
    X = "X"
    Y = "Y"
    Z = "Z"


class Outcomes(Enum):
    Win = 6
    Draw = 3
    Lose = 0


# This mapping is doing too much, should just return outcome but lazy
RPSMappings = {
    RPS.Rock: {
        RPS.Rock: Outcomes.Draw.value + RPSValues[RPS.Rock],
        RPS.Paper: Outcomes.Lose.value + RPSValues[RPS.Rock],
        RPS.Scissors: Outcomes.Win.value + RPSValues[RPS.Rock],
    },
    RPS.Paper: {
        RPS.Rock: Outcomes.Win.value + RPSValues[RPS.Paper],
        RPS.Paper: Outcomes.Draw.value + RPSValues[RPS.Paper],
        RPS.Scissors: Outcomes.Lose.value + RPSValues[RPS.Paper],
    },
    RPS.Scissors: {
        RPS.Rock: Outcomes.Lose.value + RPSValues[RPS.Scissors],
        RPS.Paper: Outcomes.Win.value + RPSValues[RPS.Scissors],
        RPS.Scissors: Outcomes.Draw.value + RPSValues[RPS.Scissors],
    },
}

RPSOutcomeMapping = {
    RPS.Rock: {
        Outcomes.Win: RPS.Paper,
        Outcomes.Draw: RPS.Rock,
        Outcomes.Lose: RPS.Scissors,
    },
    RPS.Paper: {
        Outcomes.Win: RPS.Scissors,
        Outcomes.Draw: RPS.Paper,
        Outcomes.Lose: RPS.Rock,
    },
    RPS.Scissors: {
        Outcomes.Win: RPS.Rock,
        Outcomes.Draw: RPS.Scissors,
        Outcomes.Lose: RPS.Paper,
    },
}


def get_input(filename: str) -> t.List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    return data


def parse_input(
    input_data: t.List[str],
) -> t.List[t.Tuple[RPS, RPSUnknown]]:
    parsed = []
    for line in input_data:
        known, unknown = line.split()
        parsed.append((RPS(known), RPSUnknown(unknown)))
    return parsed


def day1(input: t.List[t.Tuple[RPS, RPSUnknown]]) -> int:
    mapping = {
        RPSUnknown.X: RPS.Rock,
        RPSUnknown.Y: RPS.Paper,
        RPSUnknown.Z: RPS.Scissors,
    }
    outcomes = [RPSMappings[mapping[ours]][opponent] for opponent, ours in input]
    return sum(outcomes)


def day2(input: t.List[t.Tuple[RPS, str]]) -> int:
    mapping = {
        RPSUnknown.X: Outcomes.Lose,
        RPSUnknown.Y: Outcomes.Draw,
        RPSUnknown.Z: Outcomes.Win,
    }
    score_total = 0
    for opponent, the_outcome in input:
        outcome = mapping[the_outcome]
        our_choice = RPSOutcomeMapping[opponent][outcome]
        score_total += outcome.value + RPSValues[our_choice]

    return score_total


def main():
    input = get_input("day2/input.txt")
    parsed_input = parse_input(input)
    day1_result = day1(parsed_input)
    day2_result = day2(parsed_input)
    print(day1_result, day2_result)


if __name__ == "__main__":
    main()
