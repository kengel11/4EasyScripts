INPUT:
"Code me a Structure array of 6 window column panes spaced out multiples of 4 in the x dimension, and an array of 8 simple strings that are spaced out in base 2 starting from 25 going until 1600"  

Inputs:
    InitialXPosition(25), // Initial x-position for the first pane
    XSpacing(4); // Spacing between panes in the x-dimension

Vars:
    MyPanesArray[6], // Structure array to store window panes
    MyStringsArray[8]; // Array to store the simple strings

// Create the window panes
for i = 0 to 5 begin
    // Calculate the x-position for the current pane
    var currentXPosition = InitialXPosition + (i * XSpacing);

    // Create a new window pane and assign it to the structure array
    MyPanesArray[i].Pane = NewWindow("Pane " + NumToStr(i + 1), 
                                     Default, 
                                     Default, 
                                     currentXPosition, 
                                     Default);
end;

// Create the array of simple strings spaced out in base 2
Vars:
    Base2Spacing(1); // The base-2 spacing starting from 25

for i = 0 to 7 begin
    // Calculate the value for the current element in the array
    var currentValue = 25 + (Base2Spacing * i);

    // Convert the value to a string and store it in the array
    MyStringsArray[i] = NumToStr(currentValue);

    // Double the base-2 spacing for the next element
    Base2Spacing = Base2Spacing * 2;
end;