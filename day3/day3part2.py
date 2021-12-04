def get_reports():
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        reports = [int(line, 2) for line in lines]
        return reports


def find_most_common_bit(reports, pos):
    count = 0
    for report in reports:
        count += report >> pos & 1
    return 1 if count >= len(reports) / 2 else 0


def find_least_common_bit(reports, pos):
    count = 0
    for report in reports:
        count += report >> pos & 1
    return 0 if count >= len(reports) / 2 else 1


def filter_report(reports, pos, use_most_common_bit):
    result = []
    search_bit = find_most_common_bit(reports, pos) if use_most_common_bit else find_least_common_bit(reports, pos)
    for report in reports:
        if (report >> pos & 1) == search_bit:
            result.append(report)
    return result


def find_oxygen_generator_rating(reports):
    pos = 11
    while pos > 0:
        reports = filter_report(reports, pos, True)
        pos -= 1
        if len(reports) == 1:
            break
    print(reports)
    return reports[0]


def find_co2_scrubber_rating(reports):
    pos = 11
    while pos > 0:
        reports = filter_report(reports, pos, False)
        pos -= 1
        if len(reports) == 1:
            break
    print(reports)
    return reports[0]


def main():
    reports = get_reports()
    oxygen_rating = find_oxygen_generator_rating(reports)
    scrubber_rating = find_co2_scrubber_rating(reports)
    life_support_rating = oxygen_rating * scrubber_rating
    print(life_support_rating)


main()
