import pandas
from pybaseball import batting_stats

def store_batting_stats(season: int, raw: bool=True, clean: bool=False) -> None:
    """
    Fetches and stores batting statistics from pybaseball.batting_stats
    
    Removes unecessary columns

    Adds BIP (Balls In Play)
    """
    def clean_data(df: pandas.DataFrame) -> None:
        # Apply PA cutoff
        df = df[df['PA'] >= 350]

        # Drop columns
        pitch_splits = ['FB% (Pitch)', 'SL%', 'CT%', 'CB%', 'CH%', 'SF%', 'KN%', 'XX%', 'PO%', 'FBv', 'SLv', 'CTv', 
                        'CBv', 'CHv', 'SFv', 'KNv']
        df = df.drop(columns=pitch_splits)

        value = ['Bat', 'Off', 'RAR', 'RE24', 'REW', 'WAR', 'Dol', 'WPA', '-WPA', '+WPA', 'WPA/LI', 'Clutch', 'L-WAR']
        value.extend([c for c in df.columns if c[0] == 'w' and c != 'wOBA'])
        df = df.drop(columns=value)

        statcast = [c for c in df.columns if '(sc)' in c]
        df = df.drop(columns=statcast)

        pitch_info = [c for c in df.columns if '(pi)' in c]
        df = df.drop(columns=pitch_info)

        plus = [c for c in df.columns if c[-1] == '+']
        plus.append('LD+%')
        df = df.drop(columns=plus)

        expected = [c for c in df.columns if c[0] == 'x']
        df = df.drop(columns=expected)

        pinch_hitting = ['pLI', 'phLI', 'PH']
        df = df.drop(columns=pinch_hitting)

        base_running = ['SB', 'CS', 'Spd', 'UBR', 'BsR']
        df = df.drop(columns=base_running)
        
        defense = ['Fld', 'FRM', 'Def']
        df = df.drop(columns=defense)

        component = ['Pitches', 'Balls', 'Strikes', 'Rep', 'Pos', 'Lg']
        df = df.drop(columns=component)

        other = ['Age Rng', 'G', 'R', 'RBI', 'SH', 'IBB', 'TTO%', 'Pace', 'Zone%', 'CStr%']
        df = df.drop(columns=other)

        # Add BIP 
        df.insert(loc=7, column='BIP', value=df['AB'] - df['SO'] - df['HR'] + df['SF'])

        # Save dataset
        df.to_csv(f'data/processed/{season}_batting_stats_cleaned.csv', index=False)

    df = batting_stats(season, qual=0)
    if raw:
        df.to_csv(f'data/raw/{season}_batting_stats.csv', index=False)
    if clean:
        clean_data(df)

if __name__ == '__main__':
    store_batting_stats(2024, raw=False, clean=True)
    store_batting_stats(2025, raw=False, clean=True)