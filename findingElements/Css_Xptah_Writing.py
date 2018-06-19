
#Techniques to write CSS-
'''

tagName[attribute='name']
input[id='tabWindow']

#id
#tabWindow

tagname#id

input#tabWindow

button[class='class1']

.class1
button.class1

for elemment having  multiple classes

you can use either one single class name or can use the combination

.class1.class2.class3

input[class='class1']

<button id="openwindow" class="btn-style class1" onclick="openWindow()">Open Window</button>

for the combination of two classes

button[class='btn-style class1']
or
button[class='btn-style']

Use of * $ and ^

* means contains
^ means starts with
$ means ends with

<button id="openwindow" class="btn-style class1" onclick="openWindow()">Open Window</button>

button[class='btn-style class1']

button[class^='btn']- Gives four nodes ----Means match any element whose class name starts with btn
button[class^='btn-style'] -Gives one node

button[class$='class1']---Means match any element whose class name ends with style1


button[class*='style']--Means match any element whose class name contains style

Use of greater than sign--   >
>  this right arrow used for traversing from parent tag to child tag

for example-
fieldset>

fieldset>select

you can also use the combination of traversing and id or class locators

fieldset>select#multiple-select-example


'''


'''

CSS Selectors Cheat Sheet



Every element does not have an id -> static id, unique name, unique link text. For those elements we need to build xpath to find and then perform actions on them.

 
Whatever we use to find an element, id, name, xpath, css -> It should always be unique.

It should only find one matching node unless we want to capture a list of elements.

   
Syntax:

tag[attribute='value']

“#” -> Id

“.” -> Class



Element Displayed Example Text Box:

input[id=displayed-text]

#displayed-text

input#displayed-text

 
input[class=displayed-class]

.displayed-class

input.displayed-class

 
Appending Classes

.class1.class2.class3 -> Until we find a unique element



Using wildcards in CSS Selectors:

“^” -> Represents the starting text

“$” -> Represents the ending text

“*” -> Represents the text contained

Syntax:

tag[attribute<special character>=’value’]

Examples:
input[class='inputs'] -> Only 1 matching node

input[class^='inputs'] -> Two matching nodes

input[class='displayed-class'] - No matching nodes

input[class$='class'] -> One matching node

input[class*='displayed-class'] -> One matching node

Finding Children

fieldset -> 10 matching nodes

Fieldset>table

fieldset>#product -> One matching node

fieldset>button -> One matching node

Fieldset>a

fieldset>input#name
'''