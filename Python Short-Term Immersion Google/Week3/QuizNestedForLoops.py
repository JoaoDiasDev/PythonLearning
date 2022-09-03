# What should be the next line to prevent two variables from being printed with the same value?

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:  # This line to prevent when variables has the same value
            print(home_team + " vs " + away_team)
