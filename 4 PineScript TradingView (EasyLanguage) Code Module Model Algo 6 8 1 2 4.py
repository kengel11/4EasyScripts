//@version=5
indicator("Structure Array and Strings", overlay=true)

// Function to generate the structure array of window column panes
generateWindowPanes(num_panes, spacing) =>
    windowPanes = array.new_float(num_panes)
    for i = 0 to num_panes - 1
        array.push(windowPanes, i * spacing)
    windowPanes

// Function to generate the array of strings spaced out in base 2
generateStringsInBase2(start, end, num_strings) =>
    step = (end - start) / (num_strings - 1)
    stringsArray = array.new_string(num_strings)
    for i = 0 to num_strings - 1
        array.push(stringsArray, tostring(start + i * step, format=format.fixed))

// Generate the window panes and strings
windowPanesArray = generateWindowPanes(6, 4)
stringsArray = generateStringsInBase2(25, 1600, 8)

// Output results
for i = 0 to 5
    label.new(x = windowPanesArray[i], y = high, text = tostring(windowPanesArray[i]), style = label.style_label_left)
    
for i = 0 to 7
    label.new(x = i * 200, y = high[1], text = stringsArray[i], style = label.style_label_center)
