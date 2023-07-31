# Structure array of 6 window column panes spaced out multiples of 4 in the x dimension
input numberOfPanes = 6;
def paneSpacing = 4;
def window_panes = if BarNumber() % paneSpacing == 0 then BarNumber() / paneSpacing else Double.NaN;

# Array of 8 simple strings spaced out in base 2 from 25 to 1600
def startValue = 25;
def endValue = 1600;
def numStrings = 8;
def base2Strings = new string[numStrings];
for (int i = 0; i < numStrings; i++) {
    base2Strings[i] = BinaryToString(startValue + i * (endValue - startValue) / (numStrings - 1));
}

# Print the arrays
AddLabel(yes, "Window Panes Array: " + Concat(",", window_panes), Color.CYAN);
AddLabel(yes, "Base 2 Strings Array: " + Concat(",", base2Strings), Color.MAGENTA);
